from datetime import date

import requests
from django.utils.text import slugify
from lxml import html

from .models import Club

BASE_URL = "https://www.worldclass.ro"


def get(url):
    resp = requests.get(f"{BASE_URL}{url}")
    resp.raise_for_status()
    return resp


def sync():
    if not Club.objects.exists():
        resp = get("/wp-json/clubs/v1/club")
        for row in resp.json():
            slug = row["post_name"]
            data = dict(
                name=row["post_title"],
                upfit_id=int(row["acf"]["upfit_club_id"]),
                level=row["acf"]["tip_club"],
            )
            Club.objects.update_or_create(slug=slug, defaults=data)

    for club in Club.objects.filter(sync=True):
        resp = get(f"/wp-admin/admin-ajax.php?clubid={club.upfit_id}&action=load_clubs")
        page = html.fromstring(resp.content.decode("utf8"))
        for day_node in page.cssselect(".day_group"):
            for class_node in day_node.cssselect(".schedule-class"):
                data = dict(
                    day=date.fromisoformat(day_node.attrib["data-date"]),
                    hours=class_node.cssselect(".class-hours")[0].text_content(),
                    title=class_node.cssselect(".class-title")[0].text_content(),
                    trainers=class_node.cssselect(".trainers")[0].text_content(),
                )
                slug = slugify(f"{club.slug} {data['day']} {data['hours']} {data['title']}")
                club.class_set.get_or_create(slug=slug, defaults=data)

import requests

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

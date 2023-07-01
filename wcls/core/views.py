from django.conf import settings
from django.shortcuts import render

from .models import Class


def homepage(request):
    context = dict(
        classes=Class.objects.filter(
            title__in=settings.WCLS_CLASSES,
        ).order_by("day", "hours"),
    )
    return render(request, "homepage.html", context)

from django.contrib import admin
from django.urls import path

from wcls.core.views import homepage

urlpatterns = [
    path("", homepage),
    path("admin/", admin.site.urls),
]

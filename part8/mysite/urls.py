from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path("", RedirectView.as_view(url="polls/", permanent=False)),
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]

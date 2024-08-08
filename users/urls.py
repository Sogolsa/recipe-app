from django.urls import path
from .views import Profile, signup_view, update_profile
from django.urls import re_path
from django.conf import settings
from django.views.static import serve


app_name = "users"

urlpatterns = [
    path("profile/", Profile.as_view(), name="profile"),
    path("update_profile/", update_profile, name="update_profile"),
    path("signup/", signup_view, name="signup"),
    # handle media file requests during development.
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
]

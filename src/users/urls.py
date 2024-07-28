from django.urls import path
from .views import Profile, signup_view
from django.urls import re_path
from django.conf import settings
from django.views.static import serve


app_name = "users"

urlpatterns = [
    path("profile/", Profile.as_view(), name="profile"),
    path("signup/", signup_view, name="signup"),
    # re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
]

from django.shortcuts import render
from .models import User


# Create your views here.
def profile(request):
    user = User.objects.first()
    context = {"user": user}
    return render(request, "users/user_profile.html", context)

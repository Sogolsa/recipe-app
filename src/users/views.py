from django.shortcuts import render
from .models import User
from django.contrib.auth.decorators import login_required  # To protect FBV


# Create your views here.
@login_required  # keep protected
def profile(request):
    user = User.objects.first()
    context = {"user": user}
    return render(request, "users/user_profile.html", context)

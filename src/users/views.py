from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from django.contrib.auth.models import User
from .forms import SignupForm
from django.contrib.auth import login, authenticate


# Create your views here.
class Profile(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = "users/user_profile.html"
    context_object_name = "current_user"

    def get_object(self, queryset=None):
        return CustomUser.objects.get(user=self.request.user)


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()

            CustomUser.objects.create(
                user=user,
                name=form.cleaned_data["name"],
                picture=form.cleaned_data["picture"] or "no_picture.jpg",
                bio=form.cleaned_data["bio"],
            )

            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password1"],
            )
            if user is not None:
                login(request, user)
                return redirect("users:profile")
        else:
            # Handle form errors
            return render(request, "auth/signup.html", {"form": form})
    else:
        form = SignupForm()
        return render(request, "auth/signup.html", {"form": form})

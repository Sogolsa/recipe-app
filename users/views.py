from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from django.contrib.auth.models import User
from .forms import ProfileUpdateForm, SignupForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.
class Profile(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = "users/user_profile.html"
    context_object_name = "current_user"

    # def get_object(self, queryset=None):
    #     return CustomUser.objects.get(user=self.request.user)
    def get_object(self, queryset=None):
        user = self.request.user
        # Check if a CustomUser instance exists for the logged-in user
        custom_user, created = CustomUser.objects.get_or_create(user=user)
        return custom_user


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            try:
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
            except Exception as e:
                return HttpResponse(f"An error occurred: {e}", status=500)
        else:
            return render(
                request,
                "auth/signup.html",
                {"form": form, "error_message": "There were errors in the form"},
            )
    else:
        form = SignupForm()
        return render(request, "auth/signup.html", {"form": form})


@login_required
def update_profile(request):
    user_profile = get_object_or_404(CustomUser, user=request.user)

    if request.method == "POST":
        form = ProfileUpdateForm(
            request.POST, request.FILES, instance=user_profile, user=request.user
        )
        if form.is_valid():
            form.save()
            # messages.success(request, "Profile was updated successfully.")
            messages.add_message(
                request,
                messages.SUCCESS,
                "Profile was updated successfully.",
                extra_tags="profile",
            )

            return redirect("users:profile")
    else:
        form = ProfileUpdateForm(instance=user_profile, user=request.user)

    return render(
        request, "users/user_profile.html", {"form": form, "current_user": user_profile}
    )

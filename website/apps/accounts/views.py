from django.views.generic.base import TemplateView
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from .forms import EditProfileForm


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"


def edit_profile(request: HttpRequest) -> HttpResponse:
    form = EditProfileForm(instance=request.user.profile)
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return render(request, "accounts/edit_profile.html", {"form": form, "success": True})
    return render(request, "accounts/edit_profile.html", {"form": form})
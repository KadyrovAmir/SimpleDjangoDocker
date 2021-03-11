from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.core.mail import send_mail

import bleach
from website import settings
from .forms import ContactForm


def contact(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = bleach.clean(form.cleaned_data["name"])
            email = bleach.clean(form.cleaned_data["email"])
            message = bleach.clean(form.cleaned_data["message"])
            send_mail(f"{name} sent a message.", message, email, [settings.DEFAULT_FROM_EMAIL])
            return render(request, "contact.html", {"form": ContactForm(), "success": True})
    form = ContactForm()
    return render(request, "contact.html", {"form": form})
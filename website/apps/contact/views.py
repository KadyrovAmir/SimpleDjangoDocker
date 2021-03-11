from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

import bleach
from .forms import ContactForm
from .tasks import send_mail_task


def contact(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = bleach.clean(form.cleaned_data["name"])
            email = bleach.clean(form.cleaned_data["email"])
            message = bleach.clean(form.cleaned_data["message"])
            send_mail_task.delay(name, email, message)
            return render(request, "contact.html", {"form": ContactForm(), "success": True})
    form = ContactForm()
    return render(request, "contact.html", {"form": form})
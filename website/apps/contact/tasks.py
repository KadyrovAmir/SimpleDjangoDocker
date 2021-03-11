from celery import shared_task
from django.core.mail import send_mail

from website import settings


@shared_task
def send_mail_task(name, email, message):
    send_mail(f"{name} sent a message.", message, email, [settings.DEFAULT_FROM_EMAIL])
    return 'Done!'

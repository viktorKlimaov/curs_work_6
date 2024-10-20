from datetime import datetime, timedelta
from smtplib import SMTPException

import pytz
from apscheduler.schedulers.background import BackgroundScheduler

from django.core.mail import send_mail
from django.db.models import Q

from config import settings
from mainapp.models import Mailing, Attempt


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_mailing, 'interval', seconds=20)
    scheduler.start()


def send_mailing():
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    # создание объекта с применением фильтра
    mailings = Mailing.objects.filter(Q(status__in=['created', 'started']) & Q(data_time__lte=current_datetime) & Q(
        next_data_time__lte=current_datetime) & Q(is_active=True))
    for mailing in mailings:

        try:
            server_response = send_mail(
                subject=mailing.message.subject_letter,
                message=mailing.message.body_letter,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[client.email for client in mailing.client.all()]
            )

            Attempt.objects.create(mailing=mailing, data_time=current_datetime, email_answer=server_response)
        except SMTPException as response:
            Attempt.objects.create(mailing=mailing, email_answer=str(response), is_attempt=False,
                                   data_time=current_datetime)

        finally:

            if mailing.periodicity == 'once_day':
                mailing.next_data_time += timedelta(days=1)
            elif mailing.periodicity == 'once_week':
                mailing.next_data_time += timedelta(weeks=1)
            elif mailing.periodicity == 'once_month':
                mailing.next_data_time += timedelta(weeks=4)

        mailing.save()

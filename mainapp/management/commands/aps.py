from django.core.management import BaseCommand

from mainapp.apscheduler_jop import send_mailing_hand


class Command(BaseCommand):

    def handle(self, *args, **options):
        send_mailing_hand()



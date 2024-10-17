from django.core.management import BaseCommand

from mainapp.apscheduler_jop import send_mailing


class Command(BaseCommand):

    def handle(self, *args, **options):
        send_mailing()

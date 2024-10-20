from time import sleep

from django.apps import AppConfig


class MainappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mainapp'

    def ready(self):
         from mainapp.apscheduler_jop import start
         sleep(2)
         start()
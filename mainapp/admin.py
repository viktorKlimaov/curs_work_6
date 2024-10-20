from django.contrib import admin

from mainapp.models import Client, Mailing, Message


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'father_name', 'comment')
    list_filter = ('last_name',)

admin.site.register(Mailing)

admin.site.register(Message)

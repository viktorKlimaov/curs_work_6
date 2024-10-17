from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from mainapp.apps import MainappConfig
from mainapp.views import BaseView, ClientDetailView, ClientCreateView, ClientDeleteView, ClientUpdateView, \
    ClientListView, MailingListView, MailingDetailView, MailingCreateView, MailingDeleteView, MailingUpdateView, \
    MessageDetailView, MessageCreateView, MessageDeleteView, MessageUpdateView, AttemptListView, MessageListView

app_name = MainappConfig.name




urlpatterns = [
    path('',BaseView.as_view(), name='home'),

    path('client/', ClientListView.as_view(), name='client_list'),
    path('client/detail/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client/create/', ClientCreateView.as_view(), name='client_form'),
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
    path('client/update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),

    path('mailing/', MailingListView.as_view(), name='mailing_list'),
    path('mailing/detail/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailing/create/', MailingCreateView.as_view(), name='mailing_form'),
    path('mailing/delete/<int:pk>/', MailingDeleteView.as_view(), name='mailing_delete'),
    path('mailing/update/<int:pk>/', MailingUpdateView.as_view(), name='mailing_update'),

    path('message/', MessageListView.as_view(), name='message_list'),
    path('message/detail/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('message/create/', MessageCreateView.as_view(), name='message_form'),
    path('message/delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),
    path('message/update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),

    path('attempt/', AttemptListView.as_view(), name='attempt_list'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
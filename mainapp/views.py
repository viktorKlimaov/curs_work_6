from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView
from formset.calendar import CalendarResponseMixin

from mainapp.forms import ClientForm, MailingForm, MessageForm
from mainapp.models import Client, Mailing, Message, Attempt


class BaseView(TemplateView):
    template_name = 'mainapp/base.html'

##############################################

class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    context_object_name = 'clients'
    template_name = 'mainapp/client_list.html'

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Client.objects.all()
        else:
            return Client.objects.filter(user=user)


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'mainapp/client_detail.html'


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'mainapp/client_form.html'
    success_url = reverse_lazy('mainapp:client_list')

    def form_valid(self, form):
        product = form.save()
        product.user = self.request.user
        product.save()
        return super().form_valid(form)


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = 'mainapp/client_confirm_delete.html'
    success_url = reverse_lazy('mainapp:client_list')


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'mainapp/client_form.html'
    success_url = reverse_lazy('mainapp:client_list')


#############################################

class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing
    context_object_name = 'mailing_list'
    template_name = 'mainapp/mailing_list.html'

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Mailing.objects.all()
        else:
            return Mailing.objects.filter(user=user)


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing
    template_name = 'mainapp/mailing_detail.html'

class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mainapp/mailing_form.html'
    success_url = reverse_lazy('mainapp:mailing_list')

    def form_valid(self, form):
        product = form.save()
        product.user = self.request.user
        product.save()
        return super().form_valid(form)


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    template_name = 'mainapp/mailing_confirm_delete.html'
    success_url = reverse_lazy('mainapp:mailing_list')

class MailingUpdateView(CalendarResponseMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mainapp/mailing_form.html'
    success_url = reverse_lazy('mainapp:mailing_list')

#############################################

class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    context_object_name = 'messages'
    template_name = 'mainapp/message_list.html'

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Message.objects.all()
        else:
            return Message.objects.filter(user=user)


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    template_name = 'mainapp/message_detail.html'

class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'mainapp/message_form.html'
    success_url = reverse_lazy('mainapp:mailing_list')

    def form_valid(self, form):
        product = form.save()
        product.user = self.request.user
        product.save()
        return super().form_valid(form)


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    template_name = 'mainapp/message_confirm_delete.html'
    success_url = reverse_lazy('mainapp:mailing_list')

class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    template_name = 'mainapp/message_form.html'
    success_url = reverse_lazy('mainapp:mailing_list')

#################################################

class AttemptListView(LoginRequiredMixin, ListView):
    model = Attempt
    context_object_name = 'attempt_list'
    template_name = 'mainapp/attempt_list.html'

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Attempt.objects.all()
        else:
            return Client.objects.filter(user=user)
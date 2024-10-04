from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView

from mainapp.forms import ClientForm, MailingForm, MessageForm
from mainapp.models import Client, Mailing, Message


class BaseView(TemplateView):
    template_name = 'mainapp/base.html'

##############################################

class ClientListView(ListView):
    model = Client
    context_object_name = 'clients'
    template_name = 'mainapp/client_list.html'

class ClientDetailView(DetailView):
    model = Client
    template_name = 'mainapp/client_detail.html'

class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'mainapp/client_form.html'
    success_url = reverse_lazy('mainapp:client_list')

class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'mainapp/client_confirm_delete.html'
    success_url = reverse_lazy('mainapp:client_list')

class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'mainapp/client_form.html'
    success_url = reverse_lazy('mainapp:client_list')

#############################################

class MailingListView(ListView):
    model = Mailing
    context_object_name = 'mailing_list'
    template_name = 'mainapp/mailing_list.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["messages"] = Message.objects.all()
        return context


class MailingDetailView(DetailView):
    model = Mailing
    template_name = 'mainapp/mailing_detail.html'

class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mainapp/mailing_form.html'
    success_url = reverse_lazy('mainapp:mailing_list')

class MailingDeleteView(DeleteView):
    model = Mailing
    template_name = 'mainapp/mailing_confirm_delete.html'
    success_url = reverse_lazy('mainapp:mailing_list')

class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mainapp/mailing_form.html'
    success_url = reverse_lazy('mainapp:mailing_list')

#############################################

class MessageDetailView(DetailView):
    model = Message
    template_name = 'mainapp/message_detail.html'

class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'mainapp/message_form.html'
    success_url = reverse_lazy('mainapp:mailing_list')

class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'mainapp/message_confirm_delete.html'
    success_url = reverse_lazy('mainapp:mailing_list')

class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    template_name = 'mainapp/message_form.html'
    success_url = reverse_lazy('mainapp:mailing_list')
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView
from formset.calendar import CalendarResponseMixin

from blog.models import Blog
from mainapp.forms import ClientForm, MailingForm, MessageForm, MailingModeratorForm
from mainapp.models import Client, Mailing, Message, Attempt
from mainapp.services import get_blogs_from_cache


class BaseView(TemplateView):
    template_name = 'mainapp/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count_mailing"] = len(Mailing.objects.all())
        context["count_active_mailing"] = len(Mailing.objects.filter(is_active=True))
        context["count_unique_client"] = len(Client.objects.distinct('first_name'))  # .distinct('first_name')
        # получение случайных статей из кеша
        context['random_blogs'] = get_blogs_from_cache()
        return context


##############################################

class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    context_object_name = 'clients'
    template_name = 'mainapp/client_list.html'

    # Список клиентов могут видеть только их владельцы
    def get_queryset(self):
        user = self.request.user
        return Client.objects.filter(user=user)


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'mainapp/client_detail.html'


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'mainapp/client_form.html'
    success_url = reverse_lazy('mainapp:client_list')

    # Автоматическое заполнение поля владельца
    def form_valid(self, form):
        owner = form.save()
        owner.user = self.request.user
        owner.save()
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

    # Список рассылок могут видеть только их владельцы и модератор
    def get_queryset(self):
        user = self.request.user
        if user.has_perm('mainapp.can_view_mailing'):
            return Mailing.objects.all()
        else:
            return Mailing.objects.filter(user=user)


class MailingDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Mailing
    template_name = 'mainapp/mailing_detail.html'

    # Предоставление прав модератору для просмотра рассылки
    def test_func(self):
        obj = self.get_object()
        user = self.request.user
        obj.save()
        user.save()
        if obj.user == user:
            return True
        elif user.has_perm('mainapp.can_view_mailing'):
            return True
        return False


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mainapp/mailing_form.html'
    success_url = reverse_lazy('mainapp:mailing_list')

    # Автоматическое заполнение поля владельца
    def form_valid(self, form):
        product = form.save()
        product.user = self.request.user
        product.save()
        return super().form_valid(form)


class MailingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Mailing
    template_name = 'mainapp/mailing_confirm_delete.html'
    success_url = reverse_lazy('mainapp:mailing_list')

    # Удалять рассылку может только владелец
    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mainapp/mailing_form.html'
    success_url = reverse_lazy('mainapp:mailing_list')

    # Предоставление прав модератору на блокировку рассылок
    def get_form_class(self):
        user = self.request.user
        user.save()
        if user == self.object.user:
            return MailingForm
        if user.has_perm('mainapp.can_disable_mailing') and user.has_perm('mainapp.can_view_mailing'):
            return MailingModeratorForm
        raise PermissionDenied

    # # Обновлять рассылку может только владелец
    # def test_func(self):
    #     obj = self.get_object()
    #     return obj.user == self.request.user


#############################################

class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    context_object_name = 'messages'
    template_name = 'mainapp/message_list.html'

    # Список сообщений могут видеть только их владельцы
    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(user=user)


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    template_name = 'mainapp/message_detail.html'


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'mainapp/message_form.html'
    success_url = reverse_lazy('mainapp:mailing_list')

    # Автоматическое заполнение поля владельца
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

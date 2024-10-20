import secrets

from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, UserModeratorForm
from users.models import User


class UserLoginView(LoginView):
    template_name = 'user/login.html'

class UserLogoutView(LogoutView):
    pass

class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'user/user_form.html'
    success_url = reverse_lazy('users:login')



    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}'
        send_mail(
            subject='Подтверждение почты',
            message=f'Для подтверждения регистрации перейдите по ссылке: {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.token = None
    user.save()
    return redirect(reverse('users:login'))


class NewPasswordView(PasswordResetView):
    template_name = 'user/new_password_form.html'
    form_class = PasswordResetForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        user = User.objects.get(email=email)
        if user:
            password = secrets.token_urlsafe(10)
            send_mail(
                subject="Новый пароль",
                message=f"Твой новый пароль: {password}",
                from_email=EMAIL_HOST_USER,
                recipient_list=[user.email]
            )
            user.set_password(password)
            user.save()

            return redirect(reverse('users:login'))

        else:
            return redirect(reverse('users/new_password_form.html'))


class UserListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = User
    context_object_name = 'users'
    template_name = 'user/user_list.html'
    permission_required = 'users.can_view_list_users'


class UserUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = User
    form_class = UserModeratorForm
    template_name = 'user/user_form.html'
    success_url = reverse_lazy('users:user_list')
    permission_required = 'users.can_block_users'











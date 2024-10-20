from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from users.models import User


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'avatar', 'country', 'phone', 'password1', 'password2')



class UserModeratorForm(ModelForm):
    class Meta:
        model = User
        fields = ('is_active',)
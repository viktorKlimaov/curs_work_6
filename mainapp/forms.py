
from formset.widgets import DateTimeInput
from django import forms

from mainapp.models import Client, Mailing, Message

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ClientForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Client
        fields = ('email', 'first_name', 'last_name', 'father_name', 'comment')


class MailingForm(forms.ModelForm):

    class Meta:
        model = Mailing
        fields = ('data_time', 'periodicity', 'status', 'client', 'message')
        widgets = {
            'data_time': DateTimeInput
        }

class MailingModeratorForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ('is_active',)


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('subject_letter', 'body_letter')

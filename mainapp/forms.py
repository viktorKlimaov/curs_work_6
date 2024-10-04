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
        fields = '__all__'


class MailingForm(forms.ModelForm):

    class Meta:
        model = Mailing
        fields = '__all__'


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = '__all__'
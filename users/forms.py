from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=False, help_text="Необязательное поле, введите номер телефона.")
    username = forms.CharField(max_length=50, required=False)

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите свою почту'
        })
        self.fields['phone_number'].widget.attrs.update({
            'class': 'form-select'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-select'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-select'
        })
        self.fields['username'].widget.attrs.update({
            'class': 'form-select'
        })

    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2',)

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError("Номер телефона должен состоять только из цифр!")
        return phone_number

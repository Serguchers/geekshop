from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from .models import ShopUser


class ShopUserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(ShopUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

    def clean_password(self):
        password = self.cleaned_data.get('password')
        user = ShopUser.objects.get(username=self.cleaned_data.get('username'))
        if not check_password(password, user.password):
            raise ValidationError('Вы ввели неверный пароль!')
        return password


    class Meta:
        model = ShopUser
        fields = ("username", "password")


class ShopUserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(ShopUserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.help_text = ""

    def clean_age(self):
        data = self.cleaned_data["age"]
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")
        return data


    class Meta:
        model = ShopUser
        fields = ("username", "first_name", "password1", "password2", "email", "age", "avatar")


class ShopUserEditForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(ShopUserEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.help_text = ""

    def clean_age(self):
        data = self.cleaned_data["age"]
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")

        return data

    class Meta:
        model = ShopUser
        fields = ("username", "first_name", "email", "age", "avatar")

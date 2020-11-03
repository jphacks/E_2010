from django.forms import Form
from django.forms import fields
from django import forms
from django.core.exceptions import ValidationError

class RegisterForm(Form):
    username = fields.CharField(
        required=True,
        min_length=3,
        max_length=100,
        error_messages={
            "required":"USER NAME EMPTY",
            "min_length":"TOO SHORT",
            "max_length":"TOO LONG"
        }
    )
    password = fields.CharField(
        required=True,
        widget=forms.PasswordInput,
        min_length=3,
        max_length=18,
        error_messages={
            "required":"PASSWORD CAN NOT EMPTY",
            "min_length": "PASSWORD TOO SHORT",
            "max_length": "PASSWORD TOO LONG"
        }
    )
    # password_2 = fields.CharField(required=False)
    email = fields.EmailField(
        required=True,
        error_messages={"required":"MAIL ERROR"},
    )

    def clean_password2(self):
        if not self.errors.get("password"):
            if self.cleaned_data["password2"] != self.cleaned_data["password1"]:
                raise ValidationError("NEED SAME PASSWORD")
            return self.cleaned_data

class LoginForm(Form):
    email = fields.EmailField(
        required=True,
        error_messages={"required":"MAIL ERROR"},
    )
    password = fields.CharField(
        required=True,
        widget=forms.PasswordInput,
        error_messages={
            "required":"NOT EMPTY PASSWORD",
        }
    )
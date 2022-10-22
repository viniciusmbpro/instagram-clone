from django import forms
from django.contrib.auth.models import User
from django.forms import ValidationError

from utils.django_forms import strong_password


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'username',
        }),
        label='Username',
        help_text=(
            'Username must have letters, numbers or one of those @.+-_. '
            'The length should be between 4 and 150 characters.'
        ),
        error_messages={
            'required': 'This field must not be empty',
            'min_length': 'Username must have at least 4 characters',
            'max_length': 'Username must have less than 150 characters',
        },
        min_length=4, max_length=150,
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'First name',
        }),
        error_messages={'required': 'Write your first name'},
        label='First name'
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Last name',
        }),
        error_messages={'required': 'Write your last name'},
        label='Last name'
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'example@email.com',
        }),
        error_messages={'required': 'E-mail is required'},
        label='E-mail',
        help_text='The e-mail must be valid.',
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
        }),
        error_messages={
            'required': 'Password must not be empty'
        },
        help_text=(
            'Password must have at least one uppercase letter, '
            'one lowercase letter and one number. The length should be '
            'at least 8 characters.'
        ),
        validators=[strong_password],
        label='Password'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repeat your password',
        }),
        label='Password2',
        error_messages={
            'required': 'Please, repeat your password'
        },
    )

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        exists = User.objects.filter(email=email).exists()

        if exists:
            raise ValidationError(
                'User e-mail is already in use', code='invalid',
            )

        return email

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            password_confirmation_error = ValidationError(
                'Password and password2 must be equal',
                code='invalid'
            )
            raise ValidationError({
                'password': password_confirmation_error,
                'password2': [
                    password_confirmation_error,
                ],
            })

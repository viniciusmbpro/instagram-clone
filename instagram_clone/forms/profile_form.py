from django import forms
from django.contrib.auth.models import User

from instagram_clone.models import Profile


class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
        ]


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Profile
        fields = [
            'bio',
            'phone',
            'photo',
            'gender',
            'website',
        ]

    photo = forms.ImageField(
        widget=forms.FileInput(attrs={
            'onchange': 'preview()',
        }),
        label='Photo',
        error_messages={'required': 'This field must not be empty'},
    )

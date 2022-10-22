from django import forms


class LoginForm(forms.Form):
    def __init__(*args, **kwargs):
        super().__init__(*args, **kwargs)

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Your username',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Your password',
        })
    )

from django import forms

from instagram_clone.models import Post


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Post
        fields = [
            'photo',
            'caption',
        ]

    caption = forms.Textarea()
    photo = forms.ImageField(
        widget=forms.FileInput(attrs={
            'onchange': 'preview()',
        }),
        label='Photo',
        error_messages={'required': 'This field must not be empty'},
    )

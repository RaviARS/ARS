from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import PostArticle, CATEGORY


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    dob = forms.DateField()
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    article_category = forms.TypedChoiceField(choices=CATEGORY)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class PostArticleForm(forms.ModelForm):
    """ POST Article Form. """
    name = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'comment_input', 'name': 'Name',
                   'placeholder': 'Article Name'}
        )
    )

    # images = forms.FileField(
    #     label='',
    #     required=True,
    #     widget=forms.FileField(
    #         attrs={'class': 'comment_input', 'name': 'images'}
    #     )
    # )

    img_captions = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'comment_input', 'name': 'img_captions',
                   'placeholder': 'Image Caption'}
        )
    )

    description = forms.CharField(
        label='',
        required=True,
        widget=forms.Textarea(
            attrs={'class': 'comment_input', 'name': 'description',
                   'placeholder': 'Article Description'}
        )
    )

    # category = forms.CharField(
    #     label='',
    #     required=True,
    #     widget=forms.TextInput(
    #         attrs={'class': 'comment_input', 'name': 'category'}
    #     )
    # )

    tags = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'comment_input', 'name': 'tags',
                   'placeholder': 'Add Tag optional'}
        )
    )

    class Meta:
        model = PostArticle
        fields = ['name', 'images', 'img_captions', 'description', 'category', 'tags']
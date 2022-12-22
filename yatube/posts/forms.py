from django.utils.translation import gettext_lazy as _
from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group', "image")
        help_texts = {
            'text': _('Текст поста'),
            'group': _('Вы можете указать группу к посту'),
            'image': _('Прикрепить фото')
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
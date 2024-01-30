from django import forms
from movies.models import Comment


class CommentForm(forms.ModelForm):

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'id': 'add-comment', 'class': 'add-comment-field'})
        self.user = user

    class Meta:
        model = Comment
        fields = ['text']

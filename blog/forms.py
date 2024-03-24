from django import forms
from .models import Comment

FORM_CLASS = 'w-full px-6 py-4 border border-slate-300 rounded-xl'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ('text', )
        widgets = {
            'text': forms.Textarea(attrs={
                'class': FORM_CLASS
            })
        }

    

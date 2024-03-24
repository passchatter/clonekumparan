from django import forms
from blog.models import Blogs

FORM_CLASS = 'w-full px-6 py-4 border border-slate-300 rounded-xl'

class NewBlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ('title', 'subtitle', 'category', 'content', 'image')
        widgets = {
            'title':forms.TextInput(attrs={
                'class':FORM_CLASS
            }),
            'subtitle':forms.TextInput(attrs={
                'class':FORM_CLASS
            }),
            'category':forms.Select(attrs={
                'class':FORM_CLASS
            }),
            'content':forms.Textarea(attrs={
                'class':FORM_CLASS
            }),
            'image':forms.FileInput(attrs={
                'class':FORM_CLASS
            })
        }
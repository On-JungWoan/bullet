from django import forms
from .models import Post

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'url', 'site', 'keyword', 'date']
    
    def __str__(self):
        return str([self.title, self.content, self.url, self.site, self.keyword, self.date])
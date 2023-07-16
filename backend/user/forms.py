from django import forms
from .models import User

class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'keywordCount']

    def __str__(self):
        return str([self.name, self.email, self.password, self.keywordCount])
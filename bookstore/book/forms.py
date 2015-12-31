from django import forms
from django.contrib.auth.models import User

class SearchForm(forms.Form):
    #Categories for search
    searchChoices = (
        ('title', 'Title'),
        ('author', 'Author'),
        ('publisher', 'Publisher'),
        ('language', 'Language'),
        ('isbn', 'ISBN'),
    )

    category = forms.ChoiceField(choices=searchChoices)
    name = forms.CharField(label='search', max_length=40)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

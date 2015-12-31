from django import forms

class SearchForm(forms.Form):
    #Categories for search
    searchChoices = (
        ('title', 'Title'),
        ('author', 'Author'),
        ('publisher', 'Publisher'),
        ('language', 'Language'),
        ('isbn', 'ISBN'),
    )

    categories = forms.ChoiceField(choices=searchChoices)
    name = forms.CharField(label='search', max_length=40)


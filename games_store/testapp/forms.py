from django import forms

class NumbInPage(forms.Form):
    posts_in_page = forms.CharField(max_length=3, label='Кличество страниц на стр.')
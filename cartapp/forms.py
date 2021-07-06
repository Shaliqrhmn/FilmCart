from django import forms
from .models import FilmDetail


class film_form(forms.ModelForm):
    class Meta:
        model = FilmDetail
        fields = ['film_name', 'film_desc', 'film_year', 'film_icon']
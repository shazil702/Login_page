from django.forms.models import ModelForm
from .models import Movie
class MovieModelForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

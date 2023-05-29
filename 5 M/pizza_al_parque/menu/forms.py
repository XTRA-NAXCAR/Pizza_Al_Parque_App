from django import forms
from .models import Type, Food

class TypeForm(forms.ModelForm):
    title = forms.CharField(label='Título', widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(label='Imagen', widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = Type
        fields = ('title', 'image')
class FoodForm(forms.ModelForm):
    title = forms.CharField(label='Título', widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Descripción', widget=forms.Textarea(attrs={'class': 'form-control'}))
    price = forms.FloatField(label='Precio', widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Food
        fields = ('title', 'description', 'price')
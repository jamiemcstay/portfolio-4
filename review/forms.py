from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Review

class ReviewForm(forms.ModelForm):

    score = forms.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
        widget=forms.NumberInput(attrs={
            'min': 1,
            'max': 5,
            'placeholder': 'Enter a score between 1 and 5'
        })
    )
    class Meta:
        model = Review
        fields = [
            'album_name', 
            'artist_name', 
            'genre', 
            'content', 
            'score',
            'image',
        ]
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
        }
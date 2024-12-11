from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
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
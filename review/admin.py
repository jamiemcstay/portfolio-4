from django.contrib import admin
from .models import Review
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    list_display = ('album_name', 'genre', 'score', 'date_created', 'author', 'slug')
    search_fields = ['album_name', 'artist_name', 'genre', 'author_username']
    list_filter = ('genre', 'score', 'date_created')
    summernote_fields = ('content', 'excerpt')

# Register your models here.


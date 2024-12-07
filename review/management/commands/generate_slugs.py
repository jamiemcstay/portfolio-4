from django.core.management.base import BaseCommand
from review.models import Review
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Generate slugs for existing records'

    def handle(self, *args, **kwargs):
        reviews = Review.objects.all()

        updated_count = 0
        for review in reviews:
            if not review.slug:
                review.slug = slugify(f"{review.artist_name} {review.album_name}")
                review.save()
                updated_count += 1
        self.stdout.write(self.style.SUCCESS(f'Successfully updated {updated_count} slugs'))
        
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Q, CheckConstraint

# Create your models here.


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews", null=False)
    album_name = models.CharField(max_length=255, blank=False)
    genre = models.CharField(max_length=50, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=False)
    excerpt = models.TextField(blank=True)
    score = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        blank=False
    )

    class Meta:
        constraints = [
            CheckConstraint(
                check=Q(score__gte=1) & Q(score__lte=5),
                name="score_between_1_and_5"
            )
        ]


# Generated by Django 4.2.16 on 2024-12-03 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_review_score_between_1_and_5'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='excerpt',
            field=models.TextField(blank=True),
        ),
    ]

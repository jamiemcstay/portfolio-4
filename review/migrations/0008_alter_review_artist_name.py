# Generated by Django 4.2.16 on 2024-12-03 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0007_review_artist_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='artist_name',
            field=models.CharField(default='Unknown Artist', max_length=255),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.16 on 2024-12-03 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0004_review_excerpt'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

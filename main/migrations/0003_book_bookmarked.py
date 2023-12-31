# Generated by Django 4.2.6 on 2023-10-27 08:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_load_book_fixture'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='bookmarked',
            field=models.ManyToManyField(blank=True, default=None, related_name='bookmark', to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-26 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='nickname',
            field=models.CharField(default=None, max_length=255),
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-27 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0005_alter_userprofile_bookmarkedbooks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(max_length=400),
        ),
    ]
# Generated by Django 4.2.8 on 2023-12-18 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_profile", "0007_alter_userprofile_profile_picture"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="isAdmin",
            field=models.BooleanField(default=False),
        ),
    ]
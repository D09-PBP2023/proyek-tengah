# Generated by Django 4.2.6 on 2023-10-28 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_profile", "0006_alter_userprofile_bio"),
        ('user_profile', '0006_alter_userprofile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="profile_picture",
            field=models.ImageField(
                blank=True, null=True, upload_to="profile_pictures/"
            ),
        ),
    ]

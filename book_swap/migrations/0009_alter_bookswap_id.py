# Generated by Django 4.2.7 on 2023-12-17 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_swap', '0008_alter_bookswap_from_user_alter_bookswap_to_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookswap',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
# Generated by Django 4.2.7 on 2023-12-17 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_swap', '0009_alter_bookswap_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookswap',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

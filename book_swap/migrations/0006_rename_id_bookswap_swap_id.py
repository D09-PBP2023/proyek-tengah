# Generated by Django 4.2.7 on 2023-12-17 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_swap', '0005_alter_bookswap_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookswap',
            old_name='id',
            new_name='swap_id',
        ),
    ]

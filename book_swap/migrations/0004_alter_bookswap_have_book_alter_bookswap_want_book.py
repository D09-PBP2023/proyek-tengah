# Generated by Django 4.2.7 on 2023-12-17 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_swap', '0003_alter_bookswap_have_book_alter_bookswap_to_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookswap',
            name='have_book',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='bookswap',
            name='want_book',
            field=models.TextField(max_length=500),
        ),
    ]

# Generated by Django 4.2.7 on 2023-12-17 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_swap', '0006_rename_id_bookswap_swap_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookswap',
            name='swap_id',
        ),
        migrations.AddField(
            model_name='bookswap',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]

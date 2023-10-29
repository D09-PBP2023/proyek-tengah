# Generated by Django 4.2.6 on 2023-10-29 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookSwap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=150)),
                ('acc_user', models.CharField(max_length=150)),
                ('name', models.CharField(default='', max_length=200)),
                ('message', models.TextField(max_length=500)),
                ('swapped', models.BooleanField(default=False)),
            ],
        ),
    ]

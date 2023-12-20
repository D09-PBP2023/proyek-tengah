# Generated by Django 4.2.7 on 2023-12-15 13:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0006_merge_0005_merge_20231029_1355_0005_review'),
        ('book_swap', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookswap',
            old_name='message',
            new_name='from_message',
        ),
        migrations.RemoveField(
            model_name='bookswap',
            name='acc_user',
        ),
        migrations.RemoveField(
            model_name='bookswap',
            name='name',
        ),
        migrations.RemoveField(
            model_name='bookswap',
            name='user',
        ),
        migrations.AddField(
            model_name='bookswap',
            name='from_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookswap',
            name='have_book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='have_book', to='main.book'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookswap',
            name='processed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bookswap',
            name='to_message',
            field=models.TextField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookswap',
            name='to_user',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookswap',
            name='want_book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='want_book', to='main.book'),
            preserve_default=False,
        ),
    ]

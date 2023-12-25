# Generated by Django 5.0 on 2023-12-24 23:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forumtopic',
            name='game',
        ),
        migrations.RemoveField(
            model_name='forumtopic',
            name='genre',
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('text', models.TextField(verbose_name='Текст')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.game', verbose_name='Игра')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.genre', verbose_name='Жанр')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Пост на форуме',
                'verbose_name_plural': 'Посты на форуме',
            },
        ),
        migrations.DeleteModel(
            name='ForumPost',
        ),
        migrations.DeleteModel(
            name='ForumTopic',
        ),
    ]
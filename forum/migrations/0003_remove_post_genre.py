# Generated by Django 5.0 on 2023-12-25 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_remove_forumtopic_game_remove_forumtopic_genre_post_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='genre',
        ),
    ]
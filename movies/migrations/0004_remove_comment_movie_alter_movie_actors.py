# Generated by Django 5.0.1 on 2024-01-29 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_movie_actors_alter_movie_director'),
        ('users', '0002_alter_actor_biography_alter_director_biography'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='movie',
        ),
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(blank=True, to='users.actor', verbose_name='actors'),
        ),
    ]

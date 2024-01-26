# Generated by Django 5.0.1 on 2024-01-25 20:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_initial'),
        ('users', '0002_alter_actor_biography_alter_director_biography'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(blank=True, null=True, to='users.actor', verbose_name='actors'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='directed_movies', to='users.director'),
        ),
    ]
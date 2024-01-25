# Generated by Django 5.0.1 on 2024-01-25 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='user',
        ),
        migrations.RemoveField(
            model_name='director',
            name='user',
        ),
        migrations.AddField(
            model_name='actor',
            name='name',
            field=models.CharField(blank=True, db_index=True, max_length=150, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='director',
            name='name',
            field=models.CharField(blank=True, db_index=True, max_length=150, verbose_name='name'),
        ),
    ]

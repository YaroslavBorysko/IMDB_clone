# Generated by Django 5.0.1 on 2024-01-25 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='biography',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='biography'),
        ),
        migrations.AlterField(
            model_name='director',
            name='biography',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='biography'),
        ),
    ]

# Generated by Django 5.1.6 on 2025-04-07 16:13

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('age', models.IntegerField(default=1)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('fav_toy', models.CharField(blank=True, default='', max_length=64)),
            ],
        ),
    ]

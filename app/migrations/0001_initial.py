# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 19:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=30)),
                ('player_position', models.CharField(max_length=10)),
                ('jersey_number', models.IntegerField()),
                ('plays_from_scrimmage', models.IntegerField()),
                ('yards_from_scrimmage', models.IntegerField()),
                ('ave_yards_per_play_from_scrimmage', models.FloatField()),
                ('tds_from_scrimmage', models.IntegerField()),
            ],
        ),
    ]

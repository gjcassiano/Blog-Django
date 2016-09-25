# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-19 01:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('texto', models.CharField(max_length=255)),
                ('date', models.DateField()),
            ],
        ),
    ]

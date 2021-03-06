# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-26 01:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.CharField(default='English', max_length=30),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='image_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.CharField(max_length=50),
        ),
    ]

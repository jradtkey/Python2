# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-19 23:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('migrationProject', '0002_author_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default='null'),
            preserve_default=False,
        ),
    ]
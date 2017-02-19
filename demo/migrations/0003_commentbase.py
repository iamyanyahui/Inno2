# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-19 02:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20170115_0814'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_date', models.CharField(max_length=10)),
                ('comment_content', models.CharField(max_length=500)),
                ('comment_movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.MovieBase')),
            ],
        ),
    ]
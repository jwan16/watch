# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-06 04:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=250)),
                ('brand_des', models.CharField(max_length=500)),
                ('brand_origin', models.CharField(max_length=100)),
                ('brand_logo', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='watch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watch_name', models.CharField(max_length=50)),
                ('watch_year', models.CharField(max_length=10)),
                ('watch_pic', models.FileField(upload_to='')),
                ('watch_large_pic', models.FileField(upload_to='')),
                ('watch_brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watch.Brand')),
            ],
        ),
    ]
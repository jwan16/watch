# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 03:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0007_auto_20170525_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watch',
            name='bracelet_color',
            field=models.CharField(max_length=30, verbose_name='Bracelet Color'),
        ),
        migrations.AlterField(
            model_name='watch',
            name='bracelet_length',
            field=models.CharField(max_length=30, verbose_name='Bracelet Length'),
        ),
        migrations.AlterField(
            model_name='watch',
            name='bracelet_material',
            field=models.CharField(max_length=30, verbose_name='Bracelet Material'),
        ),
        migrations.AlterField(
            model_name='watch',
            name='case_material',
            field=models.CharField(max_length=30, verbose_name='Case Material'),
        ),
        migrations.AlterField(
            model_name='watch',
            name='code',
            field=models.CharField(max_length=20, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='watch',
            name='movement',
            field=models.CharField(choices=[('automatic', 'Automatic'), ('manual', 'Manual'), ('quartz', 'Quartz')], max_length=50, verbose_name='Movement'),
        ),
        migrations.AlterField(
            model_name='watch',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='watch',
            name='price',
            field=models.CharField(max_length=15, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='watch',
            name='ref_no',
            field=models.CharField(max_length=30, verbose_name='Ref. No.'),
        ),
        migrations.AlterField(
            model_name='watch',
            name='type',
            field=models.CharField(choices=[('all', 'All'), ('men', "Men's"), ('women', "Women's")], max_length=50, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='watch',
            name='watch_brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watch.Brand', verbose_name='Brand'),
        ),
        migrations.AlterField(
            model_name='watch',
            name='year',
            field=models.CharField(max_length=10, verbose_name='Year'),
        ),
    ]

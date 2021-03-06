# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-15 01:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.CharField(max_length=1000)),
                ('recipe', models.CharField(max_length=500)),
                ('group', models.CharField(default='Ingredientes', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='DataWayCooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('recipe', models.CharField(max_length=500)),
                ('group', models.CharField(default='Modo de Fazer', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='IgnoredWords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(db_index=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='IngredientSpec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(db_index=True, max_length=500)),
                ('count', models.IntegerField(default=0)),
                ('type', models.CharField(max_length=1)),
            ],
        ),
    ]

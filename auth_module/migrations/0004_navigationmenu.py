# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-26 13:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_module', '0003_auto_20161129_0204'),
    ]

    operations = [
        migrations.CreateModel(
            name='NavigationMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('slug', models.TextField(max_length=100)),
                ('level', models.IntegerField(default=1)),
                ('status', models.BooleanField(default=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_module.NavigationMenu')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name_plural': 'Navigation Menu',
            },
        ),
    ]

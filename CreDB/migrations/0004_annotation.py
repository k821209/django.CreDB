# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-10 09:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CreDB', '0003_final_comp'),
    ]

    operations = [
        migrations.CreateModel(
            name='annotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genename', models.CharField(max_length=50)),
                ('annotation', models.TextField()),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]

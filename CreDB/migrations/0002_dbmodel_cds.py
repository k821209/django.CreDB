# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-02 21:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CreDB', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dbmodel',
            name='CDS',
            field=models.TextField(default='ATG'),
            preserve_default=False,
        ),
    ]

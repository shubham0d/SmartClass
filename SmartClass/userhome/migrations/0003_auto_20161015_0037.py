# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userhome', '0002_auto_20161014_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='Path',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='notice',
            name='Topic',
            field=models.CharField(default=b'New Update', max_length=100),
        ),
    ]

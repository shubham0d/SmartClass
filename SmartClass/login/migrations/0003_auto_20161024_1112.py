# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20161022_1019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logininfo',
            name='id',
        ),
        migrations.AlterField(
            model_name='logininfo',
            name='rollno',
            field=models.CharField(max_length=8, serialize=False, primary_key=True),
        ),
    ]

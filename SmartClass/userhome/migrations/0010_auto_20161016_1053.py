# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userhome', '0009_auto_20161016_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='Path',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

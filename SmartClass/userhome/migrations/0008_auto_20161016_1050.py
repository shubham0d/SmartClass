# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userhome', '0007_auto_20161016_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='Path',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

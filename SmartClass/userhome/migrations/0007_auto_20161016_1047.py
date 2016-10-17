# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userhome', '0006_auto_20161016_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='date',
            field=models.DateTimeField(),
        ),
    ]

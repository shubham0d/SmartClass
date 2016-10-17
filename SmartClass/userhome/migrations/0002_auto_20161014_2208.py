# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userhome', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='lastdate',
            field=models.DateField(null=True),
        ),
    ]

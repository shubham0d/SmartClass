# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logininfo',
            name='uname',
            field=models.CharField(max_length=20, unique=True, null=True),
        ),
    ]

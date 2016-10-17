# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userhome', '0005_quiz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='date',
            field=models.DateField(),
        ),
    ]

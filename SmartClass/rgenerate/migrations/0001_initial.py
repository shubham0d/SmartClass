# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='rgrades',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rollno', models.CharField(max_length=10)),
                ('submit', models.BooleanField(default=False)),
                ('st1', models.CharField(max_length=10, null=True)),
                ('st2', models.CharField(max_length=10, null=True)),
                ('st3', models.CharField(max_length=10, null=True)),
                ('grd1', models.CharField(max_length=2, null=True)),
                ('grd2', models.CharField(max_length=2, null=True)),
                ('grd3', models.CharField(max_length=2, null=True)),
            ],
        ),
    ]

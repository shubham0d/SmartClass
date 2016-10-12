# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uname', models.CharField(max_length=20, null=True)),
                ('passwd', models.CharField(max_length=40, null=True)),
                ('name', models.CharField(max_length=40, null=True, blank=True)),
                ('rollno', models.CharField(unique=True, max_length=8)),
            ],
        ),
    ]

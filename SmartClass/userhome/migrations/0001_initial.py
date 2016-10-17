# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='notice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activity', models.CharField(max_length=20, choices=[(b'C', b'Comment'), (b'U', b'Upload')])),
                ('typeof', models.CharField(max_length=40, null=True, choices=[(b'L', b'Link'), (b'N', b'Notes'), (b'V', b'Videos'), (b'A', b'Assingnment')])),
                ('date', models.DateTimeField()),
                ('lastdate', models.DateField()),
                ('comment', models.CharField(max_length=500, null=True, blank=True)),
            ],
        ),
    ]

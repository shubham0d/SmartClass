# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userhome', '0004_auto_20161016_0917'),
    ]

    operations = [
        migrations.CreateModel(
            name='quiz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quizno', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('Topic', models.CharField(max_length=100)),
                ('lastdate', models.DateField()),
                ('Path', models.CharField(default=b'Offline', max_length=200)),
            ],
        ),
    ]

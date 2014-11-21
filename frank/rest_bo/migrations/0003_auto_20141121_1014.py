# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_bo', '0002_auto_20141121_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(unique=True, max_length=50),
            preserve_default=True,
        ),
    ]

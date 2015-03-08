# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0002_auto_20150228_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='ethnicity',
            field=models.CharField(default=b'W', max_length=1, choices=[(b'W', b'White'), (b'B', b'Black'), (b'L', b'Latino'), (b'M', b'Middle Eastern'), (b'A', b'Asian'), (b'O', b'Other/Unknown')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='guest',
            name='gender',
            field=models.CharField(default=b'M', max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='segment',
            name='pub_date',
            field=models.DateField(verbose_name=b'airdate'),
            preserve_default=True,
        ),
    ]

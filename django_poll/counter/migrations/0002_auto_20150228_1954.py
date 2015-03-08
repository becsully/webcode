# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=11)),
                ('ethnicity', models.CharField(max_length=14)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='segment',
            name='order_in_show',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='segment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 1, 3, 54, 20, 640814, tzinfo=utc), verbose_name=b'airdate'),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nicedit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NicEditImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'nicedit/%Y/%m/%d')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

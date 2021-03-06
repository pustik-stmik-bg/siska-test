# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('jurusan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tahun_akademik',
            name='created_by',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tahun_akademik',
            name='updated_by',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]

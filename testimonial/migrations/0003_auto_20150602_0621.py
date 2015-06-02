# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testimonial', '0002_auto_20150602_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='published',
            field=models.BooleanField(default=False, verbose_name=b'published'),
        ),
    ]

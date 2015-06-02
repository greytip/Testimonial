# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('customer_name', models.CharField(max_length=50, verbose_name=b'Customer')),
                ('company_name', models.CharField(max_length=50, verbose_name=b'Company')),
                ('text_snippet', models.CharField(max_length=200, verbose_name=b'Summary')),
                ('text_body', models.TextField(verbose_name=b'Body')),
                ('image_logo', models.ImageField(upload_to=b'media/logos/', null=True, verbose_name=b'Logo', blank=True)),
                ('image_person', models.ImageField(upload_to=b'media/photos', null=True, verbose_name=b'Photo', blank=True)),
                ('designation', models.CharField(max_length=50, verbose_name=b'Designation')),
                ('published', models.BooleanField(verbose_name=b'published')),
                ('category', models.CharField(max_length=20, verbose_name=b'Category')),
                ('pub_date', models.DateTimeField(verbose_name=b'Published date')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

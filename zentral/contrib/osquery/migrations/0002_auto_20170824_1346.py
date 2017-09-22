# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-24 13:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import zentral.contrib.osquery.models


class Migration(migrations.Migration):

    dependencies = [
        ('probes', '0009_auto_20161212_1358'),
        ('osquery', '0001_squashed_0008_auto_20161111_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarveBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_id', models.IntegerField()),
                ('file', models.FileField(upload_to=zentral.contrib.osquery.models.carve_session_block_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarveSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_serial_number', models.CharField(db_index=True, max_length=255)),
                ('session_id', models.CharField(db_index=True, max_length=255)),
                ('carve_guid', models.CharField(db_index=True, max_length=255)),
                ('carve_size', models.BigIntegerField()),
                ('block_size', models.IntegerField()),
                ('block_count', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('probe_source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='probes.ProbeSource')),
            ],
        ),
        migrations.AddField(
            model_name='carveblock',
            name='carve_session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='osquery.CarveSession'),
        ),
    ]
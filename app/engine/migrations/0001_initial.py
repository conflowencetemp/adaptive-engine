# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 00:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Learner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.PositiveIntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engine.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engine.Activity')),
                ('learner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engine.Learner')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engine.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='TagGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TagLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('tag_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engine.TagGroup')),
            ],
        ),
        migrations.AddField(
            model_name='tag',
            name='tag_label',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engine.TagLabel'),
        ),
        migrations.AddField(
            model_name='activity',
            name='collection',
            field=models.ManyToManyField(to='engine.Collection'),
        ),
        migrations.AlterUniqueTogether(
            name='learner',
            unique_together=set([('course', 'identifier')]),
        ),
    ]
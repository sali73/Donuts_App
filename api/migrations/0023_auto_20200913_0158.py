# Generated by Django 3.0.7 on 2020-09-13 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_auto_20200913_0138'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='product',
            unique_together=set(),
        ),
    ]

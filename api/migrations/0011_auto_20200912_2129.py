# Generated by Django 3.0.7 on 2020-09-12 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20200912_2129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='totel',
            new_name='total',
        ),
    ]

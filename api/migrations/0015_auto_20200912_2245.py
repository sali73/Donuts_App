# Generated by Django 3.0.7 on 2020-09-12 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20200912_2240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='total',
            new_name='totle',
        ),
    ]

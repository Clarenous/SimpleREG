# Generated by Django 2.0 on 2018-03-30 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exeats', '0004_auto_20180320_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaveinfo',
            name='isLeaving_bool',
            field=models.BooleanField(default=True),
        ),
    ]
# Generated by Django 2.0 on 2018-03-20 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180320_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='StuClass',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='StuName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='StuNumber',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='StuQQ',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
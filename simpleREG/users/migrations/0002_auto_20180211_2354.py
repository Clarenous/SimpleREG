# Generated by Django 2.0 on 2018-02-11 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='StuClass',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='StuName',
            field=models.CharField(default='blank', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='StuNumber',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='StuQQ',
            field=models.IntegerField(default=0),
        ),
    ]

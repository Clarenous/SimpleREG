# Generated by Django 2.0 on 2018-03-17 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exeats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holiday',
            name='HolidayEndDate',
            field=models.DateField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='holiday',
            name='HolidayStartDate',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='leaveinfo',
            name='BackTime_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='leaveinfo',
            name='ContactPhone_bigint',
            field=models.BigIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='leaveinfo',
            name='Contact_text',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='leaveinfo',
            name='Destination_text',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='leaveinfo',
            name='LeaveTime_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='leaveinfo',
            name='StuName_text',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='leaveinfo',
            name='StuPhone_bigint',
            field=models.BigIntegerField(blank=True),
        ),
    ]

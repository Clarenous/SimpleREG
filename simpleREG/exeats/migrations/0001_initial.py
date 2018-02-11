# Generated by Django 2.0 on 2018-02-11 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='LeaveInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('StuClass_int', models.IntegerField(default=0)),
                ('StuNumber_int', models.IntegerField(default=0)),
                ('StuName_text', models.CharField(default='blank', max_length=50)),
                ('LeaveTime_date', models.DateField()),
                ('Destination_text', models.CharField(default='留校', max_length=50)),
                ('BackTime_date', models.DateField()),
                ('StuPhone_bigint', models.BigIntegerField(default=0)),
                ('Contact_text', models.CharField(default='blank', max_length=50)),
                ('ContactPhone_bigint', models.BigIntegerField(default=0)),
                ('holiday', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exeats.Holiday')),
            ],
        ),
    ]

# Generated by Django 2.0 on 2018-01-02 17:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('llegada', '0003_auto_20171222_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='race',
            name='init_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='date',
            field=models.DateField(default=datetime.date(2018, 1, 2)),
        ),
        migrations.AlterField(
            model_name='race',
            name='length',
            field=models.IntegerField(default=1000),
        ),
    ]

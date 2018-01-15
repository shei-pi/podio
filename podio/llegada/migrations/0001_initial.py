# Generated by Django 2.0 on 2018-01-14 22:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='F', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('C', 'Children'), ('O', 'Other')], default='F', max_length=1)),
                ('low_age', models.IntegerField()),
                ('high_age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('place', models.CharField(max_length=200)),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('init_time', models.DateTimeField(blank=True, null=True)),
                ('length', models.IntegerField(default=1000)),
                ('ended', models.BooleanField(default=False)),
                ('available_categories', models.ManyToManyField(to='llegada.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Registered_Athlete',
            fields=[
                ('reg_id', models.AutoField(primary_key=True, serialize=False)),
                ('athlete', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='llegada.Athlete')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='llegada.Category')),
            ],
        ),
        migrations.CreateModel(
            name='TimeRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_record', models.DurationField(default=datetime.timedelta(0))),
                ('athlete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='llegada.Athlete')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='llegada.Category')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='llegada.Race')),
            ],
        ),
        migrations.AddField(
            model_name='race',
            name='reg_athletes',
            field=models.ManyToManyField(to='llegada.Registered_Athlete'),
        ),
    ]

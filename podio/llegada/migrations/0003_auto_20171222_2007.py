# Generated by Django 2.0 on 2017-12-22 20:07

from datetime import date, datetime
from django.db import migrations
import llegada.handler.handler as hd

def athletes(apps, schema_editor):
    df = hd.init_dataframe()

    list_athletes = hd.get_athletes(df)
    athlete_model = apps.get_model('llegada', 'Athlete')
    for ath in list_athletes:
        ath_obj = athlete_model.objects.create(first_name = ath['first_name'],
                                               last_name=ath['last_name'],
                                                gender = ath['gender'],
                                               age = ath['age']
                                               )
        ath_obj.save()
def init_race(apps, schema_editor):

    race_model = apps.get_model('llegada', 'Race')
    ath_model  = apps.get_model('llegada', 'Athlete')

    ath_obj = ath_model.objects.all()

    race_obj = race_model.objects.create(
                                        name = "Gesell 2018",
                                         place = 'Villa Gessell',
                                         date = date.today(),
                                         length = 4000,
                                         )
    for ath in ath_obj:
        race_obj.reg_athletes.add(ath)

    race_obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('llegada', '0002_auto_20171222_0019'),
    ]

    operations = [
                   migrations.RunPython(athletes),
                   migrations.RunPython(init_race),
    ]

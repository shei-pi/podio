# Generated by Django 2.0 on 2017-12-22 00:19

import llegada.handler.handler as hd

from datetime import date, datetime
from django.db import migrations
from django.contrib.auth.admin import User
import re


def create_superuser(apps, schema_editor):
    superuser = User()
    superuser.is_active = True
    superuser.is_superuser = True
    superuser.is_staff = True
    superuser.username = 'juan'
    superuser.email = 'jprabino@gmail.com'
    superuser.set_password('garfunkel')
    superuser.save()

def categories(apps, schema_editor):
    df = hd.init_dataframe()

    categories = hd.get_categories(df)
    Category = apps.get_model('llegada', 'Category')
    for cat in categories:
        same_cat = re.match(r'(Master\s[A-Z])\s?:\s?(\d*)\s[aA]\s(\d*)', cat) or \
                   re.match(r'(Juveniles\s[a-z])\s?:\s?(\d*)\s[aA]\s(\d*)', cat) or \
                   re.match(r'(Pre-m\wster):\s?(\d*)\s[aA]\s(\d*)', cat)
        menores_cat = re.match(r'Hasta\s(\d*)', cat)
        general_cat = re.match(r'General', cat)


        if same_cat:
            cat = Category.objects.create(description=same_cat.group(1), gender='M', low_age=int(same_cat.group(2)),
                                          high_age=int(same_cat.group(3)))
            cat.save()
            cat = Category.objects.create(description=same_cat.group(1), gender='F', low_age=int(same_cat.group(2)),
                              high_age=int(same_cat.group(3)))
            cat.save()
        elif menores_cat:
            cat = Category.objects.create(description='Menores', gender='C', low_age=0, high_age=int(menores_cat.group(1)))
            cat.save()
        elif general_cat:
            cat = Category.objects.create(description='General', gender='O', low_age=0, high_age=120)
            cat.save()

def athletes(apps, schema_editor):
    df = hd.init_dataframe()

    list_athletes = hd.get_athletes(df)
    athlete_model = apps.get_model('llegada', 'Athlete')
    result_model = apps.get_model('llegada', 'TimeRecord')
    race_model = apps.get_model('llegada', 'Race')
    race_obj = race_model.objects.get(id=1)

    for ath in list_athletes:
        ath_obj = athlete_model.objects.create(first_name = ath['first_name'],
                                               last_name=ath['last_name'],
                                                gender = ath['gender'],
                                               age = ath['age']
                                               )
        ath_obj.save()
        ath_category = race_obj.get_category(ath_obj.age, ath_obj.gender)
        result_obj = result_model.objects.create(athlete = ath_obj,
                                                 race = race_obj,
                                                 category = ath_category,
                                                 time_record = ath['result'])
        result_obj.save()

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
        ('llegada', '0001_initial'),
    ]

    operations = [ migrations.RunPython(categories),
                   migrations.RunPython(init_race),
                   migrations.RunPython(athletes),
                   migrations.RunPython(create_superuser),
    ]

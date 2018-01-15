

from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


from .models import Registered_Athlete, Race, Category, TimeRecord, Athlete
# Create your views here.


def index(request):

    return render(request, 'llegada/index.html')

def race(request, race_id):

    race_obj = get_object_or_404(Race, id=race_id)
    try:
        reg_athletes = Registered_Athlete.objects.filter(race=race_obj)

    except ObjectDoesNotExist:
        return HttpResponse('No Reg Athletes for race {}'.format(race_obj.name))

    return render(request, 'llegada/race.html', {'race': race_obj, 'reg_athletes': reg_athletes})

def results_summary_per_category(request, race_id):
    return

def results_per_category(request, race_id, category_id):
    """
    Returns the view of all the results given a race and a category
    :param request:
    :param race_id:
    :param category_id:
    :return:
    """
    race_obj = get_object_or_404(Race, id=race_id)
    category_obj = get_object_or_404(Category, id=category_id)

    reg_athletes = Registered_Athlete.objects.filter(race=race_obj, category=category_obj)

    if not reg_athletes:
        return HttpResponse('No registered athletes for category "{}" in race: "{}"'.format(category_obj, race_obj))

    time_records = TimeRecord.objects.filter(result_athlete__in=reg_athletes)

    return render(request, 'llegada/results.html',{'results':time_records, 'category': category_obj})

def register_new_athlete(request, athlete_id, race_id):
    """
    Adds the Athlete to a Race, assigning a category 
    :param request: 
    :param athlete_id: Integer, id of the athelte
    :param race_id: Integer, id of the race.
    :return: 
    """

    athlete = Athlete.objects.get(id=athlete_id)
    race = Race.objects.get(id=race_id)

    category = race.get_category(athlete.age, athlete.gender)

    try:
        registered_athlete = Registered_Athlete.objects.create(athlete=athlete,race=race,category=category)
        registered_athlete.save()
        race.reg_athletes.add(registered_athlete)
        race.save()

    except IntegrityError:
        registered_athlete = Registered_Athlete.objects.get(athlete = athlete)
        return render(request, 'llegada/new_register.html', {'new_register': False,
                                                             'reg_ath': registered_athlete, 'race':race})
    return render(request, 'llegada/new_register.html', {'new_register': True,
                                                         'reg_ath': registered_athlete, 'race':race})

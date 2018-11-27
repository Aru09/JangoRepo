from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from main.models import Achievements
from django.http import HttpResponse, JsonResponse
import json
from main.models import Person, Achievements, Category


# Create your views here.
@csrf_exempt
def ahievements_list(request):
    if request.method=='GET':
        achievements = Achievements.objects.all()
        achievements = [a.to_json() for a in achievements]
        return JsonResponse(achievements, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        #achievements = Achievements (id = data['id'])
        achievements = Achievements (person = data[ 'person'])
        achievements = Achievements (category = data ['category'])
        #achievements = Achievements (Date = data ['Date'])
        achievements = Achievements (title = data ['title'])
        achievements.save()
        return  JsonResponse(achievements.to_json())

@csrf_exempt
def persons_list(request):
    if request.method=='GET':
        persons = Person.objects.all()
        persons = [p.to_json() for p in persons]
        return JsonResponse(persons, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        persons = Person (FullName = data [ 'FullName'])
        persons = Person (Gender = data ['Gender'])
        persons.save()
        return  JsonResponse(persons.to_json())







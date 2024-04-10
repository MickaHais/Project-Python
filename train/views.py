from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Train
import random

def accueil(request):
    trains = Train.objects.all()
    print(trains)
    context = {'trains': trains}
    return render(request, 'accueil.html', context)

def detail(request, train_ID):
    myTrain = Train.objects.get(trainID=train_ID)
    return render(request, 'detail.html', {
        "nom": myTrain.type,
        "destination": myTrain.destination,
        "depart": myTrain.depart,
        "plan": myTrain.plan
    })

def getrandom(request):
    TousTrains = Train.objects.all()
    select_train = random.choice(TousTrains)
    return render(request, 'random.html', {
        "nom": select_train.type,
        "destination": select_train.destination,
        "depart": select_train.depart,
        "plan": select_train.plan,
    })
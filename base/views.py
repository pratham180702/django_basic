from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse
from .models import Room

# Create your views here.

rooms = Room.objects.all()

def home(request):
    print("Entered home function")
    print(rooms)
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context=context)

def room(request, pk):
    final_room = Room.objects.get(id=pk)
    context = {'room':  final_room}
    return render(request, 'base/room.html', context)




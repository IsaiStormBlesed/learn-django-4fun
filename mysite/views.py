from django.http import HttpResponse
from django.shortcuts import render

def index(request):
  return HttpResponse("Hello, world. You're at the polls index")

def tweets(request, id):
  return HttpResponse(f"Your post: {id}")

def template(request):
  return render(request, 'index.html', {})

def dynamic(request, name):
  pokemons = [
    {
      "id": 1,
      "name": "Charizard"
    },
    {
      "id": 2,
      "name": "Bulbasur"
    },
  ]
  context = {
    "name": name,
    "pokemons": pokemons
  }
  return render(request, 'dynamic.html', context)
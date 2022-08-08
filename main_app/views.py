from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cheese

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cheeses_index(request):
  cheeses = Cheese.objects.all()
  return render(request, 'cheeses/index.html', { 'cheeses' : cheeses })

def cheese_details(request, cheese_id):
  cheese = Cheese.objects.get(id=cheese_id)
  return render(request, 'cheeses/details.html', { 'cheese': cheese })

class CheeseCreate(CreateView):
  model = Cheese
  fields = '__all__'

class CheeseUpdate(UpdateView):
  model = Cheese
  fields = ['brand', 'age', 'description']


class CheeseDelete(DeleteView):
  model = Cheese
  success_url = '/cheeses/'
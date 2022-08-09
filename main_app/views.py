from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Cheese, Pairing
from .forms import ReviewForm

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cheeses_index(request):
  cheeses = Cheese.objects.all()
  return render(request, 'cheeses/index.html', { 'cheeses' : cheeses })

def cheese_details(request, cheese_id):
  cheese = Cheese.objects.get(id=cheese_id)
  pairings_cheese_doesnt_have = Pairing.objects.exclude(id__in = cheese.pairings.all().values_list('id'))
  review_form = ReviewForm()
  return render(request, 'cheeses/details.html', { 
    'cheese': cheese, 'review_form': review_form, 'pairings': pairings_cheese_doesnt_have 
  })

def add_review(request, cheese_id):
  form = ReviewForm(request.POST)
  if form.is_valid():
    new_review = form.save(commit=False)
    new_review.cheese_id = cheese_id
    new_review.save()
  return redirect('cheese_details', cheese_id=cheese_id)

def assoc_pairing(request, cheese_id, pairing_id):
  Cheese.objects.get(id=cheese_id).pairings.add(pairing_id)
  return redirect('cheese_details', cheese_id=cheese_id)

class CheeseCreate(CreateView):
  model = Cheese
  fields = ['name', 'brand', 'age', 'description']

class CheeseUpdate(UpdateView):
  model = Cheese
  fields = ['brand', 'age', 'description']


class CheeseDelete(DeleteView):
  model = Cheese
  success_url = '/cheeses/'

class PairingCreate(CreateView):
  model = Pairing
  fields = '__all__'

class PairingList(ListView):
  model = Pairing

class PairingDetail(DetailView):
  model = Pairing

class PairingUpdate(UpdateView):
  model= Pairing
  fields = ['name', 'type']

class PairingDelete(DeleteView):
  model = Pairing
  success_url = '/pairings/'
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Cheese, Pairing
from .forms import ReviewForm
from django.contrib.auth.views import LoginView

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def cheeses_index(request):
  cheeses = Cheese.objects.all()
  return render(request, 'cheeses/index.html', { 'cheeses' : cheeses })
@login_required
def cheese_details(request, cheese_id):
  cheese = Cheese.objects.get(id=cheese_id)
  pairings_cheese_doesnt_have = Pairing.objects.exclude(id__in = cheese.pairings.all().values_list('id'))
  review_form = ReviewForm()
  return render(request, 'cheeses/details.html', { 
    'cheese': cheese, 'review_form': review_form, 'pairings': pairings_cheese_doesnt_have 
  })
@login_required
def add_review(request, cheese_id):
  form = ReviewForm(request.POST)
  if form.is_valid():
    new_review = form.save(commit=False)
    new_review.cheese_id = cheese_id
    new_review.user = request.user
    new_review.save()
  return redirect('cheese_details', cheese_id=cheese_id)
@login_required
def assoc_pairing(request, cheese_id, pairing_id):
  Cheese.objects.get(id=cheese_id).pairings.add(pairing_id)
  return redirect('cheese_details', cheese_id=cheese_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('cheeses_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

class CheeseCreate(LoginRequiredMixin, CreateView):
  model = Cheese
  fields = ['name', 'brand', 'age', 'description']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class CheeseUpdate(LoginRequiredMixin, UpdateView):
  model = Cheese
  fields = ['brand', 'age', 'description']


class CheeseDelete(LoginRequiredMixin, DeleteView):
  model = Cheese
  success_url = '/cheeses/'

class PairingCreate(LoginRequiredMixin, CreateView):
  model = Pairing
  fields = '__all__'

class PairingList(LoginRequiredMixin, ListView):
  model = Pairing

class PairingDetail(LoginRequiredMixin, DetailView):
  model = Pairing

class PairingUpdate(LoginRequiredMixin, UpdateView):
  model= Pairing
  fields = ['name', 'type']

class PairingDelete(LoginRequiredMixin, DeleteView):
  model = Pairing
  success_url = '/pairings/'
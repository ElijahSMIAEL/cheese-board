from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

class Cheese:

  def __init__(self, name, brand, age, description):
    self.name = name
    self.brand = brand
    self.age = age
    self.description = description

cheeses = [
  Cheese('Cheddar', 'Kraft', 0, 'A cheap ordinary cheddar cheese'),
  Cheese('Pepper-Jack', 'Great Value', 0, 'A plain, yet delicious, pepper packed cheese'),
  Cheese('Merlot BellaVitano', 'Sartori', 2, 'A rich, creamy cheese with berry and plum merlot notes')
]

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cheeses_index(request):
  return render(request, 'cheeses/index.html', { 'cheeses' : cheeses })
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


RATINGS = (
  ('S', 'Incredible'),
  ('A', 'Very Good' ),
  ('B', 'Pretty Good'),
  ('C', 'Good'),
  ('D', 'Decent'),
  ('F', 'Bad'),
)

PAIRINGS = (
  ('W', 'Wine'),
  ('F', 'Fruit'),
  ('C', 'Crackers'),
  ('Ch', 'Chocolate'),
)

class Pairing(models.Model):
  name = models.CharField(max_length=60)
  type = models.CharField(
    max_length=2,
    choices=PAIRINGS,
    default=PAIRINGS[0][0]
  ) 
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f'Name: {self.name} Type: {self.get_type_display()}'

  def get_absolute_url(self):
      return reverse("pairing_detail", kwargs={"pk": self.id})
  
class Cheese(models.Model):
  name = models.CharField(max_length=60)
  brand = models.CharField(max_length=60)
  age = models.IntegerField()
  description = models.TextField(max_length=250)
  pairings = models.ManyToManyField(Pairing)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse("cheese_details", kwargs={"cheese_id": self.id})
  
class Review(models.Model):
  content = models.TextField(max_length=150)
  rating = models.CharField(
    max_length=1,
    choices=RATINGS,
    default=RATINGS[3][0]
  )
  cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f'Rating: {self.get_rating_display()} Review: {self.content}'

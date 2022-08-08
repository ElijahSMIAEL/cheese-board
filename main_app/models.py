from django.db import models
from django.urls import reverse

RATINGS = (
  ('S', 'Incredible'),
  ('A', 'Very Good' ),
  ('B', 'Pretty Good'),
  ('C', 'Good'),
  ('D', 'Decent'),
  ('F', 'Bad'),
)

class Cheese(models.Model):
  name = models.CharField(max_length=60)
  brand = models.CharField(max_length=60)
  age = models.IntegerField()
  description = models.TextField(max_length=250)

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

  def __str__(self):
    return f'Rating: {self.get_rating_display()} Review: {self.content}'
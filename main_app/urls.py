from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('cheeses/', views.cheeses_index, name='cheeses_index'),
  path('cheeses/<int:cheese_id>/', views.cheese_details, name='cheese_details'),
  path('cheeses/create/', views.CheeseCreate.as_view(), name='cheeses_create'),
  path('cheeses/<int:pk>/update/', views.CheeseUpdate.as_view(), name='cheeses_update'),
  path('cheeses/<int:pk>/delete/', views.CheeseDelete.as_view(), name='cheeses_delete'),
]
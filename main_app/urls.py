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
  path('cheeses/<int:cheese_id>/add_review', views.add_review, name='add_review'),
  path('pairings/create/', views.PairingCreate.as_view(), name='pairings_create'),
  path('pairings/<int:pk>/', views.PairingDetail.as_view(), name='pairing_detail'),
  path('pairings/', views.PairingList.as_view(), name='pairings_index'),
  path('pairings/<int:pk>/update/', views.PairingUpdate.as_view(), name='pairings_update'),
  path('pairings/<int:pk>/delete/', views.PairingDelete.as_view(), name='pairings_delete'),
  path('cheeses/<int:cheese_id>/assoc_pairing/<int:pairing_id>/', views.assoc_pairing, name='assoc_pairing')
]
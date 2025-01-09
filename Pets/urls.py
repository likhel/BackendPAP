from django.urls import path
from .views import *

urlpatterns = [
    path('petsList/', PetListView.as_view(), name='pets-list'),
    path('petsCreate/', PetCreateView.as_view(), name='pets-create'),
    path('petsRetrieve/<int:pk>/', PetRetrieveView.as_view(), name='pets-retrieve'),
    path('petsUpdate/<int:pk>/', PetUpdateView.as_view(), name='pets-update'),
    path('petsDelete/<int:pk>/', PetDeleteView.as_view(), name='pets-delete'),
    
    path('petsCategory/', PetCategoryListView.as_view(), name='pets-category-list'),
    path('petsCategoryRetrieve/<int:pk>/', PetCategoryRetrieveView.as_view(), name='pets-category-retrieve'),
    path('petsCategoryUpdate/<int:pk>/', PetCategoryUpdateView.as_view(), name='pets-category-update'),
    path('petsCategoryDelete/<int:pk>/', PetCategoryDeleteView.as_view(), name='pets-category-delete'),
]

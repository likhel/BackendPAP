from django.urls import path, include
from .views import *

urlpatterns = [
    path('adoptersView', AdopterProfileView.as_view(), name='adopters'),
    path('adoptersCreate',AdopterProfileCreateView.as_view(), name='adopters'),
    path('adoptersRetrieve',AdopterProfileRetrieveView.as_view(), name='adopters'),
    path('adoptersUpdate',AdopterProfileUpdateView.as_view(), name='adopters'),
    path('adoptersDelete',AdopterProfileDeleteView.as_view(), name='adopters'),

    path('ad_appView',AdoptionApplicationView.as_view(), name='adopters'),
    path('ad_appCreate',AdoptionApplicationCreateView.as_view(), name='adopters'),
    path('ad_appUpdate',AdoptionApplicationUpdateView.as_view(), name='adopters'),
    path('ad_appDelete',AdoptionApplicationDeleteView.as_view(), name='adopters'),

    path('ad_reference',AdopterReferenceView.as_view(), name='adopters'),
]
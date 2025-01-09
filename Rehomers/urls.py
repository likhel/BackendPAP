from django.urls import path, include
from .views import *

urlpatterns = [
    path('rehomerView', RehomerProfileView.as_view(), name='rehomer'),
    path('rehomerCreate',RehomerProfileCreateView.as_view(), name='rehomer'),
    path('rehomerUpdate',RehomerProfileUpdateView.as_view(), name='rehomer'),
    path('rehomerDelete',RehomerProfileDeleteView.as_view(), name='rehomer'),

    path('re_appView',RehomerApplicationView.as_view(), name='rehomer'),
    path('re_appCreate',RehomerApplicationCreateView.as_view(), name='rehomer'),
    path('re_appUpdate',RehomerApplicationUpdateView.as_view(), name='rehomer'),
    path('re_appDelete',RehomerApplicationDeleteView.as_view(), name='rehomer'),

    # path('re_reference',RehomerReferenceView.as_view(), name='rehomer'),
]
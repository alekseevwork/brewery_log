from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeBrewery.as_view(), name='home'),
    # path('tank/<int:pk>/', AllTanks.as_view(), name='tanks'),
    path('tank/<int:pk>/', DetailTank.as_view(), name='tanks'),
    path('add-measuring/', CreateMeasuring.as_view(), name='add_measuring'),
    path('add_tank/', AddTanks.as_view(), name='add_tank'),
    path('tank/<int:pk>/delete_tank/', DeleteTank.as_view(), name='delete_tank'),
]
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('sData/', s_Data, name='sData'),
    path('UsData/', u_Data, name='UsData'),
    path('iUrl/', iUrl, name='iUrl'),
    path('nUrls/', nUrl, name='nUrls'),
]

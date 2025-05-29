from django.urls import path
from .views import *

urlpatterns = [

                #ОСНОВА
    path('main_page/',main_page),
    path('amo_crm/',amo_crm)

]
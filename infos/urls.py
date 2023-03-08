from django.urls import path
from .views import main, me, contact


urlpatterns = [
   path('infos/', main, name = "main"),
   path('infos/me', me, name = "me"),
   path('infos/contact', contact, name = "contact"),

]
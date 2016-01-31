# coding: utf-8
from rest_framework import routers
from application_openpaste.api import InsetViewSet

router = routers.DefaultRouter() #Definiuje domyślny router

router.register(r'Insets', InsetViewSet)#Podpinam router, czyli pod ścieżką 'przedmioty' będą wpisy z bazy
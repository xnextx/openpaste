#coding: utf-8
# Tutaj są klasy przekształcające obiekty z bazy do postaci w Rest Frameworku
from rest_framework import serializers
from .models import Inset


class InsetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inset
        #fields = ('name_sheet', 'Pricing_for_the_selected_date') #Widoczne pola


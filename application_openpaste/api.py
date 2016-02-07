from rest_framework import viewsets, permissions, filters
from application_openpaste.models import *
from .serializers import InsetSerializer
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated

from django.contrib.auth.models import User
from rest_framework import filters
from rest_framework import generics

import datetime
import random, string
from django.contrib.auth.models import User


# class Show_One_Inset(APIView):
#     # permission_classes = (IsAuthenticated,)
#
#     def show(self, url):
#
#
#     def get(self, request, *args, **kw):
#         # Any URL parameters get passed in **kw
#         myClass = Conecting_procost_base(*args, **kw)
#         result = myClass.show_all_categories_index()
#         show_inset = self.show(self, )
#         response = Response(result, status=status.HTTP_200_OK)
#         return response




class InsetViewSet(viewsets.ModelViewSet):
    queryset = Inset.objects.all()
    model = Inset
    serializer_class = InsetSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('id', )
    # permission_classes = (DjangoModelPermissions, )


    def random_string(self, length):
        hash = ""
        while(True):
            generate_string = ''.join(random.choice(string.lowercase) for i in range(length))

            if(Inset.objects.filter(url_private=generate_string).count() == 0):
                hash = generate_string
                break

        return hash


    def perform_create(self, serializer):
        if(self.request.user.id != None):
            serializer.save(owner=self.request.user, date_added=datetime.datetime.today(), url_private=self.random_string(20))
        else:
            serializer.save(date_added=datetime.datetime.today(), url_private=self.random_string(20))

    # def perform_update(self, serializer):
    #     if(self.request.user.id != None):
    #         serializer.save(owner=self.request.user, date_added=datetime.datetime.today())
    #     else:
    #         serializer.save(date_added=datetime.datetime.today())


    # Developer mode :D
    def get_queryset(self):
        queryset = Inset.objects.filter(private=False)
        return queryset
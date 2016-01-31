from rest_framework import viewsets, permissions, filters
from application_openpaste.models import *
from .serializers import InsetSerializer
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated



class InsetViewSet(viewsets.ModelViewSet):
    queryset = Inset.objects.all()
    model = Inset
    serializer_class = InsetSerializer
    permission_classes = (DjangoModelPermissions, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = Inset.objects.filter(owner=self.request.user)
        return queryset
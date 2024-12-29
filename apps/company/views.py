from rest_framework import viewsets
from .models import *
from .serializers import *


class CompanyInformationViewSet(viewsets.ModelViewSet):
    queryset = CompanyInformation.objects.all()
    serializer_class = CompanyInformationSerializer


class CompanyBrandViewSet(viewsets.ModelViewSet):
    queryset = CompanyBrand.objects.all()
    serializer_class = CompanyBrandSerializer
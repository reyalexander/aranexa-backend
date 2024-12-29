from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r"company_information", CompanyInformationViewSet)
router.register(r"company_brand", CompanyBrandViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
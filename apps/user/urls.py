from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")
router.register(r"account", AccountViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("summary/", summary_view, name="summary_json"),
    path("summary/pdf/", summary_pdf_view, name="summary_pdf"),
]
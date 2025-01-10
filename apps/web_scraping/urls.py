from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WebScrapingView

router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("web-scraping/", WebScrapingView.as_view(), name="web-scraping"),
]
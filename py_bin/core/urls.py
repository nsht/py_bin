from django.urls import path
from rest_framework import routers

from core import views

router = routers.DefaultRouter()
router.register("api/bin", views.BinViewSet, "bin")

urlpatterns = router.urls

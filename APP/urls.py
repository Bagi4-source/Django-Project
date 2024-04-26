from django.urls import path, include
from rest_framework import routers

from APP.views import DocumentViewSet, FormsViewSet, TariffViewSet

router = routers.DefaultRouter()
router.register(r'documents', DocumentViewSet)
router.register(r'forms', FormsViewSet)
router.register(r'tariff', TariffViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

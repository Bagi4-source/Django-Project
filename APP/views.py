from rest_framework import viewsets
from APP.models import Document, Forms, Tariff
from APP.permissions import IsAdminUser
from APP.serializers import DocumentSerializer, FormsSerializer, TariffSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = DocumentSerializer


class TariffViewSet(viewsets.ModelViewSet):
    queryset = Tariff.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = TariffSerializer


class FormsViewSet(viewsets.ModelViewSet):
    queryset = Forms.objects.all()
    serializer_class = FormsSerializer

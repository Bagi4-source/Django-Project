from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Document, Forms, Tariff


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'title', 'display_title', 'display_on_main_page', 'file', 'updated_at', 'created_at']


class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = ['id', 'name', 'cost', 'updated_at', 'created_at']


class FormsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forms
        fields = [
            'id',
            'first_name',
            'last_name',
            'patronymic',
            'gender',
            'date_of_birth',
            'registration_address',
            'insurance_policy_number',
            'passport_series',
            'passport_number',
            'test_type',
            'trip_number',
            'updated_at',
            'created_at'
        ]


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['is_admin'] = user.is_superuser
        token['email'] = user.username
        return token

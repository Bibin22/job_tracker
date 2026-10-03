from rest_framework.serializers import ModelSerializer

from .models import Company

class CompanySerializer(ModelSerializer):

    class Meta:
        model = Company
        fields = ['name', 'description', 'website', 'logo']
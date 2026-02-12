
from rest_framework import serializers

class RegisterCompanySerializer(serializers.Serializer):
    registerd_company_name = serializers.CharField(max_length=255)
    registerd_company_address = serializers.CharField(max_length=500)
    registerd_company_phone = serializers.CharField(max_length=20)
    registerd_company_email = serializers.EmailField()  
    
    
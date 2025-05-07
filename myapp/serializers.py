from rest_framework import serializers
from .models import UploadedFile, User

class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = '__all__'


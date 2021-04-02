from rest_framework import serializers
from .models import GeneralQuestion

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralQuestion
        fields = '__all__'

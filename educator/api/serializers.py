from rest_framework import serializers
from .models import Eductor

class EductorSerializer(serializers.ModelSerializer):
 class Meta:
  model = Eductor
  fields = ['id', 'name', 'number', 'city']
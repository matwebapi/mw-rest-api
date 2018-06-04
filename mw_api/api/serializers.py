from .models import Campus

from rest_framework import serializers

class CampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campus
        fields = ('name', )

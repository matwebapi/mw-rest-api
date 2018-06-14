from .models import (Campus, Course, )

from rest_framework import serializers


class CampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campus
        fields = ('name', 'pk')


class CourseSerializer(serializers.ModelSerializer):
    genre = serializers.CharField(source='get_genre_display')
    shift = serializers.CharField(source='get_shift_display')
    campus = serializers.ReadOnlyField(source='campus.name')
    campus_id = serializers.ReadOnlyField(source='campus.pk')

    class Meta:
        model = Course
        fields = '__all__'

from .models import (Campus, Course, Department, Subject, )

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


class DepartmentSerializer(serializers.ModelSerializer):
    campus = serializers.ReadOnlyField(source='campus.get_name_display')
    campus_id = serializers.ReadOnlyField(source='campus.pk')
    class Meta:
        model = Department
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    department = serializers.ReadOnlyField(source='department.name')
    department_id = serializers.ReadOnlyField(source='department.code')
    class Meta:
        model = Subject
        fields = '__all__'

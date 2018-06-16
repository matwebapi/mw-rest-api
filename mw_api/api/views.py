from rest_framework import viewsets

from .models import (Campus, Course, Department, )
from .serializers import (CampusSerializer, CourseSerializer,
            DepartmentSerializer,)


class CampiViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows campi to be viewed.
    """
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer
    http_method_names = ['get']


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows departments to be viewed.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    http_method_names = ['get']

class CoursesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    http_method_names = ['get']

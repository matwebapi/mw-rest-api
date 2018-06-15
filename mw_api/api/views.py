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


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows departments to be viewed.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class CoursesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

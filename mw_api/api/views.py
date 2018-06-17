from rest_framework import viewsets

from .models import (Campus, Course, Department, Subject, )
from .serializers import (CampusSerializer, CourseSerializer,
            DepartmentSerializer, SubjectSerializer, )


class CampiViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows campi to be viewed.

    Response example:

    {
        "DEPARTAMENTOS_FGA":
        {
            "CODIGO": "650",
            "SIGLA": "FGA",
            "DENOMINACAO": "UnB - Faculdade do Gama"
        }
    }
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


class SubjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows subjects to be viewed.
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    http_method_names = ['get']

class CoursesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    http_method_names = ['get']

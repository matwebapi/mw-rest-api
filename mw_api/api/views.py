from rest_framework import viewsets

from .models import (Campus, Course, Department, Subject, )
from .serializers import (CampusSerializer, CourseSerializer,
DepartmentSerializer, SubjectSerializer, )


class CampiViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows campi to be viewed.

        Path example:

        http://127.0.0.1:8000/api/campi/

        Response example:

        [
            {
            "name": "FGA",
            "pk": 1
            }
        ]

    """
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer
    http_method_names = ['get']

    def retrieve(self, request, pk=None):
        """
        API endpoint that allows select campi to be viewed.

            Path example:

            http://127.0.0.1:8000/api/campi/2

            Response example:

            [
                {
                "name": "FCE",
                "pk": 2
                }
            ]
        ---
        """
        response = super(CampiViewSet, self).retrieve(request, pk)
        return response

class DepartmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows departments to be viewed.

        Path example:

        http://127.0.0.1:8000/api/departments/

        Response example:

        [
            {
                "code": 3,
                "name": "",
                "initials": ""
            }
        ]

    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    http_method_names = ['get']

    def retrieve(self, request, pk=None):
        """
        API endpoint that allows select departments to be viewed.

            Path example:

            http://127.0.0.1:8000/api/departments/3

            Response example:

            [
                {
                  "code": 3,
                  "campus": "Darcy Ribeiro",
                  "campus_id": 3,
                  "name": "DEG",
                  "initials": "DECANATO DE ENSINO DE GRADUACAO"
                }
            ]

        """
        response = super(DepartmentViewSet, self).retrieve(request, pk)
        return response

class SubjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows subjects to be viewed.
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    http_method_names = ['get']

    def retrieve(self, request, pk=None):
        """
        API endpoint that allows select subjects to be viewed.

            Path example:

            http://127.0.0.1:8000/api/subjects/100439

            Response example:

            [
                {
                    "code": 100439,
                    "department": "FCE",
                    "department_id": 660,
                    "name": "SURDEZ: CULTURA, LINGUA E SOCIEDADE"
                }
            ]

        """
        response = super(SubjectViewSet, self).retrieve(request, pk)
        return response

class CoursesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    http_method_names = ['get']

    def retrieve(self, request, pk=None):
        """
        API endpoint that allows select subjects to be viewed.

            Path example:

            http://127.0.0.1:8000/api/courses/1635

            Response example:

            [
                {
                    "code": 1635,
                    "department": "FGA",
                    "name": "ENGENHARIA DE SOFTWARE",
                    "genre": "PRESENCIAL",
                    "shift": "DIURNO"
                }
            ]

        """
        response = super(CoursesViewSet, self).retrieve(request, pk)
        return response

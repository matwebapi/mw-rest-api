from rest_framework import viewsets

from .models import (Campus, Course)
from .serializers import (CampusSerializer, CourseSerializer)


class CampiViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows campi to be viewed.
    """
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer

class CoursesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

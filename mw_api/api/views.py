from rest_framework import viewsets

from .models import (Campus, )
from .serializers import (CampusSerializer, )


class CampiViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows campi to be viewed.
    """
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer

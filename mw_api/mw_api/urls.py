from django.contrib import admin
from django.urls import include, path

from rest_framework import routers

from api import views as api_views

router = routers.DefaultRouter()
router.register('campi', api_views.CampiViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(router.urls)),
]

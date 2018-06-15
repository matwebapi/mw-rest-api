from django.contrib import admin
from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view

from rest_framework import routers

from api import views as api_views

schema_view = get_swagger_view(title="MatriculaWeb API")
router = routers.DefaultRouter()
router.register('campi', api_views.CampiViewSet)
router.register('courses', api_views.CoursesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view),
    path('', include(router.urls)),
]

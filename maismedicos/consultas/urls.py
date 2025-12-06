from django.urls import path, include
from rest_framework import routers
from .views import PacienteViewSet, MedicoViewSet


router = routers.DefaultRouter()
router.register(r'pacientes', viewset=PacienteViewSet)
router.register(r'medicos', viewset=MedicoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

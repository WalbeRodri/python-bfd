from rest_framework import serializers
from .models import Paciente, Medico

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['nome', 'cpf', 'email', 'genero']

class MedicoSerializer(serializers.ModelSerializer):
    atendimentos = serializers.StringRelatedField(many=True)
    class Meta:
        model = Medico
        fields = ['nome', 'crm', 'especialidade', 'atendimentos']

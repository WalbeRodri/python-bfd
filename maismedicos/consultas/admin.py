from django.contrib import admin
from .models import Paciente, Medico, Atendimento

# Register your models here.
@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ['cpf', 'nome', 'genero', 'email']


@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ['crm', 'nome', 'especialidade']

@admin.register(Atendimento)
class AtendimentoAdmin(admin.ModelAdmin):
    list_display = ['idMedico', 'idPaciente', 'turno', 'anamnese']

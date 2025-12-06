from django.db import models

GENDER_OPTIONS = [
    ("M", "Masculino"),
    ("F", "Feminino"),
    ("Não Informado", "Não Informado")
]

SHIFT_OPTIONS = [
    ("1","MORNING"),
    ("2","AFTERNOON"),
    ("3", "EVENING"),
    ("4", "NIGHT"),
]

class Paciente(models.Model):
    nome = models.CharField(max_length=200, null=False)
    cpf = models.CharField(max_length=11, null=False)
    email = models.EmailField()
    genero = models.CharField(max_length=20,choices=GENDER_OPTIONS)
    def __str__(self):
        return f'nome = {self.nome}, cpf = {self.cpf}'
    
class Medico(models.Model):
    nome = models.CharField(max_length=200)
    crm = models.IntegerField(null=False)
    especialidade = models.CharField(max_length=50)
    atendimentos = models.ManyToManyField(Paciente, through="Atendimento")
    def __str__(self):
        return f'nome = {self.nome} crm = {self.crm}'


class Atendimento(models.Model):
    idMedico = models.ForeignKey(Medico, related_name='atendente', on_delete = models.CASCADE)
    idPaciente = models.ForeignKey(Paciente, related_name='atendido', on_delete= models.CASCADE)
    turno = models.CharField(max_length=10, choices=SHIFT_OPTIONS)
    anamnese = models.TextField(max_length=6000)
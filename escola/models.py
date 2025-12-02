from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=30, null=False)
    email = models.CharField(max_length=20, unique=True, null=False)
    cpf = models.CharField(max_length=11, unique=True, null=False)
    data_ingresso = models.DateField(null=False)


STATUS_CURSO = [
    ("ativo", "Ativo"),
    ("inativo", "Inativo"),
]

class Curso(models.Model):
    nome = models.CharField(max_length=30, null=False)
    carga_horaria = models.IntegerField(default=0, null=False)
    valor_inscricao = models.FloatField(default=0.0, null=False)
    status = models.CharField(max_length=10, choices=STATUS_CURSO, default="ativo")


STATUS_MATRICULA = [
    ("pago", "Pago"),
    ("pendente", "Pendente"),
]

class Matricula(models.Model):
    data = models.DateField(null=False)
    status = models.CharField(max_length=15, choices=STATUS_MATRICULA, default="pendente")
    aluno_id = models.OneToOneField(Aluno, on_delete=models.CASCADE)
    curso_id = models.ForeignKey(Curso, on_delete=models.CASCADE)


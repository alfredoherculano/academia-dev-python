from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Aluno, Curso, Matricula
from .serializers import AlunoSerializer, CursoSerializer, MatriculaSerializer

from django.http import HttpResponse


# Root
def welcome(request):
    return HttpResponse("Bem vindo ao Sistema de Gerenciamento Escolar")


# Alunos
class AlunoList(generics.ListCreateAPIView): # ListCreateAPIView is for a collection of model instances
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class AlunoDetail(generics.RetrieveUpdateDestroyAPIView): # RetriveUpdateDestroy is for a single model instance
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


# Cursos
class CursoList(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class CursoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


# Matrículas
class MatriculaList(generics.ListCreateAPIView):
    serializer_class = MatriculaSerializer

    def get_queryset(self):
        qs = Matricula.objects.all()

        aluno = self.request.query_params.get("aluno")
        status = self.request.query_params.get("status")

        if aluno:
            qs = qs.filter(aluno=aluno)

        if status:
            qs = qs.filter(status=status)

        return qs

class MatriculaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
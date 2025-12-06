from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Aluno, Curso, Matricula
from .helper_functions import totais_por_aluno, gerar_historico
from .serializers import AlunoSerializer, CursoSerializer, MatriculaSerializer

from django.http import HttpResponse
from django.shortcuts import render


# Root
def welcome(request):
    return HttpResponse("Bem vindo ao Sistema de Gerenciamento Escolar")


# Alunos
class AlunoList(generics.ListCreateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class AlunoDetail(generics.RetrieveUpdateDestroyAPIView):
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
    
class MatriculasPorStatus(generics.ListAPIView):
    serializer_class = MatriculaSerializer

    def get_queryset(self):
        status = self.request.query_params.get("status")

        qs = Matricula.objects.filter(status=status)

        return qs

class MatriculaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


# Totais
class TotaisPorAluno(APIView):
    def get(self, request):
        aluno_id = request.query_params.get("aluno")
        if not aluno_id:
            return Response({"erro": "parametro aluno requerido"}, status=400)

        data = totais_por_aluno(aluno_id)
        return Response(data)
    

# Relatórios
# Histórico JSON
class HistoricoAluno(APIView):
    def get(self, request):
        aluno_id = request.query_params.get("aluno")
        if not aluno_id:
            return Response({"erro":"parametro aluno requerido"})
        
        data = gerar_historico(aluno_id)
        return Response(data)
    
# Histórico HTML
def historico_aluno(request):
    aluno_id = request.GET.get("aluno")
    if not aluno_id:
        return render(request, "erro.html", {"mensagem": "parametro aluno requerido"})
    
    data = gerar_historico(aluno_id)
    return render(request, "escola/historico.html", data)
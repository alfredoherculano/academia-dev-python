from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Aluno, Curso, Matricula
from .serializers import AlunoSerializer, CursoSerializer, MatriculaSerializer

from django.http import HttpResponse
from django.db import connection


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


# Totais

class TotaisPorAluno(APIView):
    def get(self, request):
        aluno_id = request.query_params.get("aluno")
        if not aluno_id:
            return Response({"erro":"parametro aluno requerido"}, status=400)
        
        sql = """
            SELECT
                aluno_id,
                SUM(CASE WHEN m.status = 'pago' THEN c.valor_inscricao ELSE 0 END) AS total_pago,
                SUM(CASE WHEN m.status = 'pendente' THEN c.valor_inscricao ELSE 0 END) AS total_devido
            FROM matricula m
            JOIN curso c ON m.curso_id = c.id
            WHERE aluno_id = %s
            GROUP BY aluno_id;
        """

        with connection.cursor() as cursor:
            cursor.execute(sql, [aluno_id])
            row = cursor.fetchone()

        if row is None:
            return Response({"aluno_id": aluno_id, "total_pago": 0, "total_devido": 0})
        
        return Response({
            "aluno_id": row[0],
            "total_pago": row[1],
            "total_devido": row[2]
        })
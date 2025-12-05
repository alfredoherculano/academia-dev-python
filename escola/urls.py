from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    # Endpoints Aluno
    path("alunos/", views.AlunoList.as_view(), name="alunos-lista"),
    path("alunos/<int:pk>/", views.AlunoDetail.as_view(), name="alunos-detalhes"),

    # Endpoints Curso
    path("cursos/", views.CursoList.as_view(), name="cursos-lista"),
    path("cursos/<int:pk>/", views.CursoDetail.as_view(), name="cursos-detalhes"),

    # Endpoints Matrículas
    path("matriculas/", views.MatriculaList.as_view(), name="matriculas-lista"),
    path("matriculas/<int:pk>/", views.MatriculaDetail.as_view(), name="matriculas-detalhes"),
    path("matriculas/totais/", views.TotaisPorAluno.as_view(), name="matriculas-totais"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
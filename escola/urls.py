from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from escola.views import historico_aluno
from . import views

urlpatterns = [
    # Endpoints alunos
    path("alunos/", views.AlunoList.as_view(), name="alunos-lista"),
    path("alunos/<int:pk>/", views.AlunoDetail.as_view(), name="alunos-detalhes"),

    # Endpoints cursos
    path("cursos/", views.CursoList.as_view(), name="cursos-lista"),
    path("cursos/<int:pk>/", views.CursoDetail.as_view(), name="cursos-detalhes"),

    # Endpoints matrículas
    path("matriculas/", views.MatriculaList.as_view(), name="matriculas-lista"),
    path("matriculas/<int:pk>/", views.MatriculaDetail.as_view(), name="matriculas-detalhes"),

    # Endpoints financeiro
    path("financeiro/totais/", views.TotaisPorAluno.as_view(), name="totais-aluno"),
    path("financeiro/status/", views.MatriculasPorStatus.as_view(), name="matriculas-status"),

    # Endpoints relatórios
    path("historico/", views.HistoricoAluno.as_view(), name="historico-json"),
    path("relatorios/historico/", historico_aluno, name="historico-html"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
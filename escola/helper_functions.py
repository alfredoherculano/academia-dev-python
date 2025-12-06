from .models import Matricula
from django.db import connection


# Calcular total pago e total devido para cada aluno
def totais_por_aluno(aluno_id):
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
        return {"aluno_id": aluno_id, "total_pago": 0, "total_devido": 0}

    return {
        "aluno_id": row[0],
        "total_pago": row[1],
        "total_devido": row[2]
    }


# Gerar histórico para cada aluno
def gerar_historico(aluno_id):
    matriculas = Matricula.objects.filter(aluno=aluno_id).select_related("curso")

    cursos = [{
        "curso_id": m.curso_id,
        "curso_nome": m.curso.nome,
        "status": m.status,
    } for m in matriculas]

    totais = totais_por_aluno(aluno_id)

    inadimplente = any(m.status == "pendente" for m in matriculas)

    return {
        "aluno_id": aluno_id,
        "cursos": cursos,
        "totais": totais,
        "inadimplente": inadimplente,
    }
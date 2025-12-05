CREATE TABLE aluno (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(40) NOT NULL,
    email VARCHAR(40) UNIQUE NOT NULL,
    cpf VARCHAR(11) UNIQUE NOT NULL,
    data_ingresso DATE NOT NULL
);

CREATE TABLE curso (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(30) NOT NULL,
    carga_horaria INTEGER NOT NULL DEFAULT 0,
    valor_inscricao DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    status VARCHAR(10) DEFAULT 'ativo'
);

CREATE TABLE matricula (
    id SERIAL PRIMARY KEY,
    data DATE NOT NULL,
    status VARCHAR(15) DEFAULT 'pendente',
    aluno_id INTEGER NOT NULL REFERENCES aluno(id) ON DELETE CASCADE,
    curso_id INTEGER NOT NULL REFERENCES curso(1d) ON DELETE CASCADE,
    UNIQUE (aluno_id, curso_id)
);
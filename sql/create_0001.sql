-- Table: public.estudante 

-- DROP TABLE public.estudante;

CREATE TABLE public.estudante
(
    codigo_inscricao bigint NOT NULL,
    idade smallint,
    sexo "char",
    cod_nacionalidade smallint,
    cod_escola integer,
    cod_municipio_nasc integer,
    cod_uf_nasc integer,
    cod_municipio_resid integer,
    cod_conclusao_em smallint,
    ano_conclusao_em smallint,
    estado_civil smallint,
    raca smallint,
    CONSTRAINT estudante_pkey PRIMARY KEY (codigo_inscricao)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.estudante
    OWNER to postgres;
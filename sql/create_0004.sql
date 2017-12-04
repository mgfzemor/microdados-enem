-- Table: public.prova_redacao

-- DROP TABLE public.prova_redacao;

CREATE TABLE public.prova_redacao
(
    id ,
    codigo_inscricao ,
    nota ,
    status smallint,
    lingua_estrangeira smallint,
    nota_comp1 real,
    nota_comp2 real,
    nota_comp3 real,
    nota_comp4 real,
    nota_comp5 real
)
    INHERITS (public.prova)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.prova_redacao
    OWNER to postgres;
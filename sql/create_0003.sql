-- Table: public.prova_objetiva 

-- DROP TABLE public.prova_objetiva;

CREATE TABLE public.prova_objetiva
(
    id ,
    codigo_inscricao ,
    nota ,
    presenca smallint,
    cor_caderno smallint,
    tipo smallint,
    respostas character varying(100) COLLATE pg_catalog."default",
    gabarito character varying(100) COLLATE pg_catalog."default"
)
    INHERITS (public.prova)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.prova_objetiva
    OWNER to postgres;
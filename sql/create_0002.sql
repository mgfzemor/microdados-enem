-- Table: public.prova

-- DROP TABLE public.prova;

CREATE TABLE public.prova
(
    id integer NOT NULL DEFAULT nextval('prova_id_seq'::regclass),
    codigo_inscricao integer NOT NULL,
    nota real,
    CONSTRAINT prova_pkey PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.prova
    OWNER to postgres;
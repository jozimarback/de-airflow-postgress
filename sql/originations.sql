CREATE TABLE IF NOT EXISTS public.originations
(
    "originationId" character varying(50) COLLATE pg_catalog."default" NOT NULL,
    "clientId" character varying(50) COLLATE pg_catalog."default" NOT NULL,
    "registerDate" date NOT NULL,
    CONSTRAINT originations_pkey PRIMARY KEY ("originationId")
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.originations
    OWNER to postgres;
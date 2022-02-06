CREATE TABLE IF NOT EXISTS public.installments
(
    "installmentId" character varying(50) COLLATE pg_catalog."default" NOT NULL,
    "originationId" character varying(50) COLLATE pg_catalog."default" NOT NULL,
    "dueDate" date NOT NULL,
    "installmentValue" real NOT NULL,
    CONSTRAINT installments_pkey PRIMARY KEY ("installmentId"),
    CONSTRAINT fk_origination FOREIGN KEY ("originationId")
        REFERENCES public.originations ("originationId") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.installments
    OWNER to postgres;
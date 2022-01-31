CREATE TABLE IF NOT EXISTS public.payments
(
    "paymentId" character varying(100) COLLATE pg_catalog."default" NOT NULL,
    "installmentId" character varying(100) COLLATE pg_catalog."default" NOT NULL,
    "paymentDate" date NOT NULL,
    "paymentValue" real NOT NULL DEFAULT 0
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.payments
    OWNER to postgres;
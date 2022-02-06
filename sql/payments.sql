CREATE TABLE IF NOT EXISTS public.payments
(
    "installmentId" text COLLATE pg_catalog."default",
    "paymentDate" timestamp without time zone,
    "paymentId" text COLLATE pg_catalog."default",
    "paymentValue" double precision,
    CONSTRAINT fk_installment FOREIGN KEY ("installmentId")
        REFERENCES public.installments ("installmentId") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.payments
    OWNER to postgres;
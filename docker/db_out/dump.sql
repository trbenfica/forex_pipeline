CREATE DATABASE "FOREX";

\c FOREX;

CREATE TABLE "FOREX" (
   "timestamp" TIMESTAMP PRIMARY KEY,
   "EUR" NUMERIC,
   "GBP" NUMERIC,
   "BRL" NUMERIC,
   "JPY" NUMERIC,
   "KRW" NUMERIC,
   "SAR" NUMERIC,
   "SGD" NUMERIC,
   "RUB" NUMERIC,
   "CAD" NUMERIC,
   "CHF" NUMERIC,
   "DKK" NUMERIC,
   "HKD" NUMERIC,
   "CUP" NUMERIC,
   "FKP" NUMERIC,
   "MXN" NUMERIC,
   "NOK" NUMERIC,
   "PHP" NUMERIC,
   "ARS" NUMERIC
);

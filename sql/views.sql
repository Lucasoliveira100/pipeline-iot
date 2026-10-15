-- View 1: média de temperatura por dispositivo e por local (interno/externo)
CREATE OR REPLACE VIEW avg_temp_por_dispositivo AS
SELECT id_dispositivo,
       local,
       ROUND(AVG(temperatura), 2) AS avg_temp,
       COUNT(*) AS total_leituras
FROM leituras_temperatura
GROUP BY id_dispositivo, local;

-- View 2: quantidade de leituras (e temperatura média) em cada hora do dia
CREATE OR REPLACE VIEW leituras_por_hora AS
SELECT EXTRACT(HOUR FROM data_hora)::int AS hora,
       COUNT(*) AS contagem,
       ROUND(AVG(temperatura), 2) AS avg_temp
FROM leituras_temperatura
GROUP BY EXTRACT(HOUR FROM data_hora)
ORDER BY hora;

-- View 3: temperatura máxima e mínima de cada dia
CREATE OR REPLACE VIEW temp_max_min_por_dia AS
SELECT CAST(data_hora AS date) AS data,
       MAX(temperatura) AS temp_max,
       MIN(temperatura) AS temp_min
FROM leituras_temperatura
GROUP BY CAST(data_hora AS date)
ORDER BY data;

# Mostra no terminal os números principais, para usar nos insights do relatório
import pandas as pd
from conexao import criar_conexao

engine = criar_conexao()

geral = pd.read_sql("""
    SELECT COUNT(*) AS total, MIN(data_hora) AS inicio, MAX(data_hora) AS fim,
           MIN(temperatura) AS minima, MAX(temperatura) AS maxima,
           ROUND(AVG(temperatura), 2) AS media
    FROM leituras_temperatura""", engine)
print(geral.T, "\n")

print(pd.read_sql("SELECT * FROM avg_temp_por_dispositivo", engine), "\n")
print(pd.read_sql("SELECT * FROM leituras_por_hora", engine), "\n")
print(pd.read_sql("SELECT * FROM temp_max_min_por_dia ORDER BY temp_max DESC LIMIT 5", engine))

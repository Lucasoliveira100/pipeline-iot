# Lê o CSV do Kaggle, trata os dados e grava no PostgreSQL.
# Depois cria as views SQL (arquivo sql/views.sql).
import os
import pandas as pd
from sqlalchemy import text
from conexao import criar_conexao

PASTA_PROJETO = os.path.join(os.path.dirname(__file__), "..")
ARQUIVO_CSV = os.path.join(PASTA_PROJETO, "data", "IOT-temp.csv")
ARQUIVO_VIEWS = os.path.join(PASTA_PROJETO, "sql", "views.sql")


def ler_csv(caminho):
    df = pd.read_csv(caminho)
    print("Linhas lidas do CSV:", len(df))

    # O CSV vem com nomes em inglês e com "/" no meio, então renomeei tudo
    df = df.rename(columns={
        "id": "id_leitura",
        "room_id/id": "id_dispositivo",
        "noted_date": "data_hora",
        "temp": "temperatura",
        "out/in": "local",
    })

    # A data vem como dia-mês-ano hora:minuto (ex: 08-12-2018 09:30)
    df["data_hora"] = pd.to_datetime(df["data_hora"], format="%d-%m-%Y %H:%M", errors="coerce")

    # Tira linhas sem data/temperatura e as repetidas
    df = df.dropna(subset=["data_hora", "temperatura"])
    antes = len(df)
    df = df.drop_duplicates(subset="id_leitura")
    print("Duplicadas removidas:", antes - len(df))

    # Troca In/Out por texto em português
    df["local"] = df["local"].str.strip().str.lower().map({"in": "Interno", "out": "Externo"})
    return df


def main():
    engine = criar_conexao()
    df = ler_csv(ARQUIVO_CSV)

    with engine.begin() as conexao:
        # CASCADE apaga as views junto, assim dá pra rodar o script várias vezes
        conexao.execute(text("DROP TABLE IF EXISTS leituras_temperatura CASCADE"))

    df.to_sql("leituras_temperatura", engine, index=False, chunksize=5000)
    print("Dados inseridos no PostgreSQL:", len(df))

    with open(ARQUIVO_VIEWS, encoding="utf-8") as f:
        sql_views = f.read()
    with engine.begin() as conexao:
        conexao.exec_driver_sql(sql_views)
    print("Views criadas.")

    # Conferência rápida
    with engine.connect() as conexao:
        total = conexao.execute(text("SELECT COUNT(*) FROM leituras_temperatura")).scalar()
    print("Total de registros na tabela:", total)


if __name__ == "__main__":
    main()

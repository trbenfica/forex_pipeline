
import pandas as pd
from sqlalchemy import create_engine
import scripts.consts as consts

# Carrega dados do input gerado por process_data para a tabela FOREX do postgres destino.
# Para efetivamente carregar os dados, verifica se o último dado do input ainda não está
# na tabela. Se estiver, nada acontece
def load_data_to_postgres():
    engine = create_engine(consts.db_url)
    connection = engine.connect()

    input_file = consts.working_dir + '/RESULT/'
    df = pd.read_parquet(input_file)
    input_last_date = df['timestamp'].max()

    # verfica se o último dado do input já está presente na tabela
    query = connection.execute(f"select timestamp from \"FOREX\" where timestamp = '{input_last_date}'")
    query = query.fetchone()
    
    print(f'Dado mais recente do input: {input_last_date}')
    print(f'Dado mais recente do banco de dados {query}')

    if query == None:
        print('@@@@ Inserindo dado na tabela')
        df.to_sql('FOREX', engine, if_exists='append', index=False)
    else:
        print('@@@@ Resultado já está presente na tabela')

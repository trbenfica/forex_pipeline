
import pandas as pd
from sqlalchemy import create_engine
import scripts.consts as consts

# Carrega dados do input gerado por process_data para a tabela FOREX do postgres destino.
# Para efetivamente carregar os dados, verifica se o último dado do input ainda não está
# na tabela. Se estiver, nada acontece
def load_data_to_postgres():

    engine = create_engine(consts.db_url)
    
    with engine.connect() as connection:
        df = pd.read_parquet(consts.working_dir + '/RESULT/')
        df.to_sql('FOREX', engine, if_exists='append', index=False)

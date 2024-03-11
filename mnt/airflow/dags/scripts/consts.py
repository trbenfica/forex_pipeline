from datetime import datetime, date
import pytz

# moedas a serem importadas. Pode-se adicionar e remover moedas à vontade, porém é
# preciso alterar também o esquema do banco de dados destino.
coin_codes = ['EUR', 'GBP', 'BRL', 'JPY', 'KRW', 'SAR', 'SGD', 'RUB', 'CAD', 'CHF',
              'DKK', 'HKD', 'FKP', 'CUP', 'MXN', 'NOK', 'PHP', 'ARS']

# data atual, define o diretório de trabalho
# current_date = datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%Y-%m-%d')
current_date = '2024-03-08'

# pasta de trabalho, onde se encontram os arquivos
working_dir = '/opt/airflow/dags/files/' + current_date + '/'

# chave da API Alphavantage. A API permite apenas 25 requisições/dia. Caso deseje usar uma
# chave própria, altere esta variável
api_key = 'NCL7QMJBR8HRYGTU'



###############################
#                             #
#   Banco de dados destino:   #
#                             #
###############################

# formato da URL: 'user:password@server_name:port/table'
db_url = 'postgresql://postgres:postgres@db_out:5432/FOREX'



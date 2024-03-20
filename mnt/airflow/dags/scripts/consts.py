import datetime
import pytz

# chave da API Alphavantage. A API permite apenas 25 requisições/dia. Caso deseje usar uma
# chave própria, altere esta variável
api_key = 'NCL7QMJBR8HRYGTU'

# moedas a serem importadas. Pode-se adicionar e remover moedas à vontade, porém é
# preciso alterar também o esquema do banco de dados destino.
coin_codes = ['EUR', 'GBP', 'BRL', 'JPY', 'KRW', 'SAR', 'SGD', 'RUB', 'CAD', 'CHF',
              'DKK', 'HKD', 'CUP', 'MXN', 'NOK', 'PHP', 'ARS']

# data atual, define o diretório de trabalho
today = datetime.datetime.now(pytz.timezone('America/Sao_Paulo'))
current_date = today.strftime('%Y-%m-%d')
day_of_week = today.strftime('%A')

# pasta de trabalho, onde se encontram os arquivos
working_dir = '/opt/airflow/dags/files/' + current_date + '/'



###############################
#                             #
#   Banco de dados destino:   #
#                             #
###############################

# formato da URL: 'user:password@server_name:port/table'
db_url = 'postgresql://postgres:postgres@db_out:5432/FOREX'



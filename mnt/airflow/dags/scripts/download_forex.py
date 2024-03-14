from urllib.request import urlretrieve
import os
import scripts.consts as consts

def download_forex():

    if os.path.exists(consts.working_dir) == False:
        if consts.day_of_week == 'Saturday' or consts.day_of_week == 'Sunday':
            print('O mercado de câmbio funciona apenas em dias úteis. Nada será processamento no momento')
        else:
            os.makedirs(consts.working_dir)
        
            print(f'# As seguintes moedas serão processadas: {consts.coin_codes}')

            for coin in consts.coin_codes:
                print(f'# Processando {coin}')
                url = f'https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=USD&to_symbol={coin}&apikey={consts.api_key}&outputsize=compact&datatype=csv'
                filename = f'{coin}.csv'
                urlretrieve(url, consts.working_dir + filename)

    else:
        print('O diretório do dia atual já existe. Entende-se que o processamento já ocorreu')
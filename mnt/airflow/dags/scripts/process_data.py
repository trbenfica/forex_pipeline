import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import desc
from pyspark.sql.functions import col
import os
import re
import consts

spark = SparkSession.builder.master("local[1]") \
                    .appName('FOREX_pipeline') \
                    .getOrCreate()

spark.sparkContext.setLogLevel('WARN')
result_dir = consts.working_dir + '/RESULT/'
if os.path.exists(result_dir) == False:
    print(f'@ Processando com PySpark: {consts.coin_codes}')

    # lê csv e processa, removendo colunas e linhas desnecessárias
    dataframes = []
    for i in range(len(consts.coin_codes)):
        dataframes.insert(i, spark.read.csv(f'{consts.working_dir}/{consts.coin_codes[i]}.csv', header=True, inferSchema=True))
        dataframes[i] = dataframes[i].select(['timestamp', 'close']).filter(dataframes[i].timestamp == consts.current_date)
        dataframes[i] = dataframes[i].withColumnRenamed('close', consts.coin_codes[i])

    # une todas colunas no dataframe final
    result = dataframes[0]
    for i in range(1, len(consts.coin_codes)):
        result = result.join(dataframes[i], 'timestamp')

    # escreve resultado num csv
    result.write.parquet(result_dir)
else:
    print('@ Resultado já processado anteriormente')




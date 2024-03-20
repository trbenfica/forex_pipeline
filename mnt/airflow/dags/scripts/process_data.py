import pyspark
from pyspark.sql import SparkSession
from sqlalchemy import create_engine
import os
import consts

spark = SparkSession.builder.master("local[1]") \
                    .appName('FOREX_pipeline') \
                    .getOrCreate()

spark.sparkContext.setLogLevel('WARN')
result_dir = consts.working_dir + '/RESULT/'

if os.path.exists(result_dir) == False:
    print(f'@ Processando com PySpark: {consts.coin_codes}')

    # recupera informações do banco de dados
    db_data = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://db_out:5432/FOREX") \
    .option("query", "select * from \"FOREX\"") \
    .option("user", "postgres") \
    .option("password", "postgres") \
    .option("driver", "org.postgresql.Driver") \
    .load()

    # lê CSVs da API e processa, removendo colunas e linhas desnecessárias
    dataframes = []
    for i in range(len(consts.coin_codes)):
        dataframes.insert(i, spark.read.csv(f'{consts.working_dir}/{consts.coin_codes[i]}.csv', header=True, inferSchema=True))
        dataframes[i] = dataframes[i].select(['timestamp', 'close'])
        dataframes[i] = dataframes[i].withColumnRenamed('close', consts.coin_codes[i])

    # une todas colunas dos CSVs num dataframe
    new_data = dataframes[0]
    for i in range(1, len(consts.coin_codes)):
        new_data = new_data.join(dataframes[i], 'timestamp', how='full_outer')

    # une informações já existentes no banco de dados com as novas (da API)
    result = db_data.union(new_data)

    # remove duplicatas
    result = result.distinct()

    # escreve resultado no disco
    result.write.parquet(result_dir)
else:
    print('@ Resultado já processado anteriormente')




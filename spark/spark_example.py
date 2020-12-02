import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StringType, IntegerType
from pyspark.sql.types import TimestampType


HOME = '/usr/local/airflow/spark'
spark = SparkSession.builder.appName('Example').getOrCreate()

schema = StructType() \
    .add('uid', IntegerType(), True) \
    .add('page_name', StringType(), True) \
    .add('page_url', StringType(), True) \
    .add('time', TimestampType(), True)

df = spark.read.format('csv').schema(schema).load(f'{HOME}/hitlog.csv')

df.createOrReplaceTempView("hitlog")
result_data = spark.sql("""With registered as ( select uid, time from hitlog
    where page_name == '/register')
    select t.page_name, t.page_url, count(*) as hits from hitlog t join registered r on t.uid==r.uid
    where t.page_url like '%/article%' 
    and t.time <= r.time
    group by t.page_name, t.page_url
    order by hits desc
    LIMIT 3
    """)

result_data.write.format('csv').mode('overwrite').option('sep', ',').save(f'{HOME}/output.csv')

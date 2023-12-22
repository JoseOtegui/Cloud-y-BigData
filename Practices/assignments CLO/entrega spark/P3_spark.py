from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.types import IntegerType

from pyspark.sql import functions as F
from pyspark.sql.functions import udf
from datetime import datetime, timedelta

import sys
import re
# Import PySpark

def get_year(date):
    array=date.split('-')
    year=array[0]
    return year

getYear = udf(get_year)


conf = SparkConf().setAppName('AvgClosePrice')
sc = SparkContext(conf = conf)
spark =  SparkSession(sc)

path="./GOOGLE.csv"
df = spark.read.option("header", "true").csv(path)

df = df.withColumn("Close", df.Close.cast('float'))
yearDf = df.withColumn("Year", getYear(F.col("Date")))
dfClose = yearDf.groupBy("Year")
avgClose = dfClose.avg("Close")
avgClose = avgClose.withColumnRenamed("avg(Close)", "avgClose")
avgClose.sort("Year").show()
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.types import IntegerType
from pyspark.sql import functions as F
from pyspark.sql.functions import udf


conf = SparkConf().setAppName('Ratings')
sc = SparkContext(conf=conf)
spark = SparkSession(sc)

path = "./ratings.csv"
DF = spark.read.option("header", "true").csv(path)


def get_range(r):
    if r < 1:
        return  1
    elif 1 < r <= 2:
        return 2
    elif 2 < r <= 3:
        return 3
    elif 3 < r <= 4:
        return 4
    elif 4 < r <= 5:
        return 5

    
getRange = udf(get_range, IntegerType())

auxDF = DF.withColumn("rating", DF.rating.cast('float'))
movieDF = auxDF.groupBy("movieId")
avgDF = movieDF.avg("rating")

resDF = avgDF.withColumn("avgRating", F.col("avg(rating)").cast('float'))
rangeDF = resDF.withColumn("Range", getRange(F.col("avgRating")))
rangeDF =rangeDF.drop('avg(rating)')
rangeDF.show()

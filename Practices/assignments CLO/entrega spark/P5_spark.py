from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.types import IntegerType
from pyspark.sql import functions as F
from pyspark.sql.functions import udf
import sys
import re

conf = SparkConf().setAppName('Meteorites')
sc = SparkContext(conf = conf)
spark = SparkSession(sc)

path="./Meteorite_Landings.csv"
meteoritesDF = spark.read.option("header", "true").csv(path)

auxDF = meteoritesDF.withColumnRenamed("mass (g)", "mass")
castDF = auxDF.withColumn("mass", auxDF.mass.cast('float'))

classDF = castDF.groupBy("recclass")
avgMass = classDF.avg("mass")
avgMass = avgMass.withColumnRenamed("avg(mass)", "avgMass")

avgMass.show()


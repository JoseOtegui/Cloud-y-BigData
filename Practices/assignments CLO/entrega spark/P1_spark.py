from pyspark import SparkConf, SparkContext
import sys
import re

conf = SparkConf().setAppName('FindWord')
sc = SparkContext(conf = conf)


word = sys.argv[1]
rdd = sc.textFile(sys.argv[2]).filter(lambda x: word in x)
print(rdd.collect())
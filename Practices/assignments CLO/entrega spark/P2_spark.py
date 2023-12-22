from pyspark import SparkConf, SparkContext
import sys
import re

conf = SparkConf().setAppName('AccesURL')
sc = SparkContext(conf = conf)


rdd = sc.textFile('./access_log')\
    .map(lambda x: x.split('"'))\
    .map(lambda x: x[1])\
    .filter(lambda x: len(x) >1)\
    .map(lambda x: x.split(' '))\
    .map(lambda x: x[1])\
    .countByValue()

for url, AccesURL in rdd.items():
    print("{} : {}".format(url, AccesURL))
# Author : 
# Created : 24. May 2018 2:06 PM
from pyspark import SparkConf, SparkContext

'''
Create Context
'''
conf = SparkConf().setAppName("spark_config").setMaster("localhost")
sc = SparkContext(conf=conf)
'''
Create RDDs
'''
words = sc.parallelize(
	["scala",
	 "java",
	 "hadoop",
	 "spark",
	 "akka",
	 "spark vs hadoop",
	 "pyspark",
	 "pyspark and spark"]
)


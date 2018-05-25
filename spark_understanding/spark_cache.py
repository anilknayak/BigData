# Author : 
# Created : 24. May 2018 3:18 AM
from pyspark import SparkContext

'''
Create Context
'''
sc = SparkContext("local", "spark_cache")
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

words.cache()
caching = words.persist().is_cached
print("Words got chached > %s" % (caching))

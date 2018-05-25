# Author : 
# Created : 24. May 2018 2:01 PM
from pyspark import SparkContext

'''
Create Context
'''
sc = SparkContext("local", "spark_Broadcast")
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

words_new = sc.broadcast(["scala", "java", "hadoop", "spark", "akka"])
data = words_new.value
print("Stored data -> %s" % (data))
elem = words_new.value[2]
print(elem)


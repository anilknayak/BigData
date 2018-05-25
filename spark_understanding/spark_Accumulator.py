# Author : 
# Created : 24. May 2018 2:03 PM
from pyspark import SparkContext

'''
Create Context
'''
sc = SparkContext("local", "spark_Accumulator")
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

num = sc.accumulator(10)
def f(x):
   global num
   num+=x
rdd = sc.parallelize([20,30,40,50])
rdd.foreach(f)
final = num.value
print("Accumulated value is -> %i" % (final))

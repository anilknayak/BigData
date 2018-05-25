# Author : Anil Kumar Nayak
# Created : 24. May 2018 3:05 AM
from pyspark import SparkContext

'''
Create Context
'''
sc = SparkContext("local", "spark_loop")
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
'''
Loop in Spark
'''


def f(x):
 print(x)
fore = words.foreach(f)



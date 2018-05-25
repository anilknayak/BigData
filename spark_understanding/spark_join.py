# Author : 
# Created : 24. May 2018 3:14 AM
from pyspark import SparkContext

'''
Create Context
'''
sc = SparkContext("local", "spark_join")
'''
Create RDDs
'''
x = sc.parallelize([("spark", 1), ("hadoop", (4,2)), ("Shreya", "A")])
y = sc.parallelize([("spark", 2), ("hadoop", 5), ("Shreya", "S")])
joined = x.join(y,numPartitions=1)
final = joined.collect()
print("Join RDD -> %s" % (final))



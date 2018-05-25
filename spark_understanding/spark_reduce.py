# Author : Anil Kumar Nayak
# Created : 24. May 2018 3:12 AM
from pyspark import SparkContext
from operator import add

'''
Create Context
'''
sc = SparkContext("local", "spark_reduce")
'''
Create RDDs
'''
nums = sc.parallelize([1, 2, 3, 4, 5])
adding = nums.reduce(add)
print("Adding all the elements -> %i" % (adding))


#-------------------------------------------------------------------
# @author 
# @copyright (C) 2018, 
# @doc
#
# @end
# Created : 24. May 2018 2:33 AM
#-------------------------------------------------------------------

from pyspark import SparkContext


class Context():
    def __init__(self):
        '''
        Create Spark Context
        '''
        sc = SparkContext("local", "First App")
        sc.setLogLevel(logLevel="ERROR")
        file = "input.txt"
        data = sc.textFile(file).cache()
        numAs = data.filter(lambda s: 'a' in s).count()
        numBs = data.filter(lambda s: 'b' in s).count()
        print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

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
        Actions Collect(), Count()
        '''
        counts = words.count()
        coll = words.collect()
        print("Number of elements in RDD -> %i" % (counts))
        print("Elements in RDDs ", coll)




        '''
        Filter in Spark
        '''
        words_filter = words.filter(lambda x: 'spark' in x)
        filtered = words_filter.collect()
        print("Fitered RDD -> %s" % (filtered))





    def f(self, x):
        print(x)

if __name__ == '__main__':
    Context()
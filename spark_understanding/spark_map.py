#-------------------------------------------------------------------
# @author 
# @copyright (C) 2018, 
# @doc
#
# @end
# Created : 24. May 2018 2:56 AM
#-------------------------------------------------------------------

from pyspark import SparkContext


class Sample():
    def __init__(self):
        sc = SparkContext("local", "First App")
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
        Map in Spark
        '''
        words_map = words.map(lambda x: (x, 1), preservesPartitioning=True)
        mapping = words_map.collect()
        print("Key value pair -> %s" % (mapping))


if __name__ == '__main__':
    Sample()
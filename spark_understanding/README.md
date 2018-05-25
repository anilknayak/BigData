# Machine Learning with PySpark

Apache Spark is known as a fast, easy-to-use and general engine for 
big data processing that has built-in modules for 
- Streaming,
- SQL 
- Machine Learning (ML)
- Graph Processing

This also helps researcher for following activities
- Exploratory Data Analysis (EDA) 
- Feature extraction 
- ML

**This Tutorial is for PySpark in Python**
Tutorial covers

- Installing PySpark
- Exploring PySpark Concepts
- Loading real time data set
- Pre processing
- Learning Regression in PySpark
- Evaluating Machine Learning Model

**Credit:** This tutorial is inspired from
  https://www.datacamp.com/community/tutorials/apache-spark-tutorial-machine-learning

## Installing PySpark
Spark is written in Scala Programming Language and runs on Java Virtual Machine (JVM) environment
####Prerequisites
- Java Run time Environment and Development Kit (JRE & JDK)
- Installing PySpark in python run following command 
```python
# pip install
pip install pyspark
```

```python
# conda install
conda install -c conda-forge pyspark
```

Following packages will get installed after executing ```pip command```
```commandline
Love:BigData anilnayak$ pip install pyspark
Collecting pyspark
  Downloading https://files.pythonhosted.org/packages/58/49/45370cc153a6adcf2c304a3c06e801ed3c9650d0f852e7fde04bd8ffb534/pyspark-2.3.0.tar.gz (211.9MB)
    100% |████████████████████████████████| 211.9MB 106kB/s 
Collecting py4j==0.10.6 (from pyspark)
  Downloading https://files.pythonhosted.org/packages/4a/08/162710786239aa72bd72bb46c64f2b02f54250412ba928cb373b30699139/py4j-0.10.6-py2.py3-none-any.whl (189kB)
    100% |████████████████████████████████| 194kB 25.1MB/s 
Building wheels for collected packages: pyspark
  Running setup.py bdist_wheel for pyspark ... done
  Stored in directory: /Users/anilnayak/Library/Caches/pip/wheels/d9/db/ff/e6f3a8a564163ea64bc2072357e77b3404d10f91be48352796
Successfully built pyspark
Installing collected packages: py4j, pyspark
Successfully installed py4j-0.10.6 pyspark-2.3.0
```
Note: for other operating system refer to this tutorial
https://www.datacamp.com/community/tutorials/apache-spark-tutorial-machine-learning

####Exploring PySpark Concepts
 - Apache Spark 
 - Apache Hadoop 
 - Scala Programming Language
 - Hadoop Distributed File System (HDFS)
 - Python
 - RDDs (Resilient Distributed Dataset)
   1. elements that run and operate on multiple nodes to do parallel processing on a cluster
   2. RDDs are immutable elements
   3. RDDs are fault tolerant as well. They recover automatically
   4. Operation on RDDs are Transformation and Action
   5. Transformation : applied on a RDD to create a new RDD example, Filter, groupBy and map
   6. Action : which instructs Spark to perform computation and send the result back to the driver
   
 - Data-Driven Documents
 - Hadoop MapReduce
   1. batch processing
   2. 
 - Spark supports interactive queries and iterative algorithms
 - own cluster manager, where it can host its application 
 - It leverages Apache Hadoop for both storage and processing
 
#####IPython Shell Usage
IPython shell instead of the Spark shell, you have to set the environment variable
```text
export PYSPARK_DRIVER_PYTHON="/usr/local/ipython/bin/ipython"
```

#####Spark Concepts Programming Steps
- SparkContext: First Create a Spark Context
```text
   master = None,
   appName = None, 
   sparkHome = None, 
   pyFiles = None, 
   environment = None, 
   batchSize = 0, 
   serializer = PickleSerializer(), 
   conf = None, 
   gateway = None, 
   jsc = None, 
   profiler_cls = <class 'pyspark.profiler.BasicProfiler'>
```
   
- Create RDDs : To apply any operation on spark, we need to create RDDs












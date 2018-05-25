# California Housing data set
# It appeared in a 1997 paper titled Sparse Spatial Autoregressions, written by Pace, R. Kelley and Ronald Barry and published in the Statistics and Probability Letters journal

debug_level = "WARN"

# ===============================================
# Details of Data
# ===============================================
file = open('data/cal_housing.domain','r')
lines = file.readlines()
attributes = []
for line in lines:
	attribute = line.split(":")[0]
	attributes.append(attribute)
print("Data Attributes", attributes)

# ===============================================
# Load Data
# ===============================================
from pyspark import SparkContext
sc = SparkContext("local", "Spark Regression")
sc.setLogLevel(logLevel=debug_level)
file_file= "data/cal_housing.data"
# Reading the file and creating RDD
data_rdd = sc.textFile(file_file).cache()
# Processing data from txt to list of entries
data_rdd = data_rdd.map(lambda line: line.split(","))
# Inspect data element for index 2
print(data_rdd.take(2))
print(data_rdd.top(2))
print(data_rdd.first())

# ===============================================
# restructure the data to make RDD to a DataFrame
# ===============================================
# following import will help to convert the spark rows to dataframe
from pyspark.sql import SparkSession
spark = SparkSession(sc)

# this import helps us to convert a list object to a row object in spark
from pyspark.sql import Row

# convert the RDD to DataFrame
df = data_rdd.map(lambda line: Row(longitude=line[0],
                              latitude=line[1],
                              housingMedianAge=line[2],
                              totalRooms=line[3],
                              totalBedRooms=line[4],
                              population=line[5],
                              households=line[6],
                              medianIncome=line[7],
                              medianHouseValue=line[8])).toDF()

df.show()

from pyspark.sql.types import *

def convertColumn(df, names, newType):
	for name in names:
		df = df.withColumn(name, df[name].cast(newType))
	return df

df = convertColumn(df, attributes, FloatType())

df.show()

from pyspark.sql.functions import *

df = df.withColumn("medianHouseValue", col("medianHouseValue")/100000)
roomsPerHousehold = df.select(col("totalRooms")/col("households"))
populationPerHousehold = df.select(col("population")/col("households"))
bedroomsPerRoom = df.select(col("totalBedRooms")/col("totalRooms"))


df = df.withColumn("roomsPerHousehold", col("totalRooms")/col("households")) \
   .withColumn("populationPerHousehold", col("population")/col("households")) \
   .withColumn("bedroomsPerRoom", col("totalBedRooms")/col("totalRooms"))


truncated_df = df.select("medianHouseValue",
                          "totalBedRooms",
                          "population",
                          "households",
                          "medianIncome",
                          "roomsPerHousehold",
                          "populationPerHousehold",
                          "bedroomsPerRoom")

from pyspark.ml.linalg import DenseVector
input_data = truncated_df.rdd.map(lambda x: (x[0], DenseVector(x[1:])))
input_data_df = spark.createDataFrame(input_data, ["label", "features"])

# Using StandardScaler
from pyspark.ml.feature import StandardScaler

# StandardScaler rescale your dataset by normalizing each feature to have unit standard deviation and/or zero mean
# Parameters:
# [withStd: True by default. Scales the data to unit standard deviation.]
# [withMean: False by default. Centers the data with mean before scaling.]

scaler = StandardScaler(inputCol="features", outputCol="scaledFeatures",
                        withStd=True, withMean=True)
scalerModel = scaler.fit(input_data_df)
scaledData = scalerModel.transform(input_data_df)

train_data_s, test_data_s = scaledData.randomSplit([.8,.2],seed=1234)

from pyspark.ml.regression import LinearRegression
from pyspark.ml.regression import LinearRegressionModel

lr = LinearRegression(featuresCol = 'scaledFeatures',
                      labelCol='label',
                      maxIter=50,
                      regParam=0.3,
                      elasticNetParam=0.8,
                      solver="normal",
                      loss="squaredError",
                      fitIntercept=True)

lr_model = lr.fit(train_data_s)
predicted = lr_model.transform(test_data_s)
predictions = predicted.select("prediction").rdd.map(lambda x: x[0])
labels = predicted.select("label").rdd.map(lambda x: x[0])
predictionAndLabel = predictions.zip(labels).collect()

print(predictionAndLabel[:5])

model_path = "./lr_model"
lr_model.save(model_path)
model2 = LinearRegressionModel.load(model_path)
# Check the model that is saved is correct
print(model2.coefficients==lr_model.coefficients)

spark.stop()
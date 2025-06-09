from pyspark.sql import SparkSession
# Create a Spark session
spark = SparkSession.builder.appName("example").getOrCreate()
# Create a simple DataFrame
data = [("Alice", 1), ("Bob", 2), ("Cathy", 3)]
df = spark.createDataFrame(data, ["Name", "Value"])
# Show the DataFrame
df.show()
# Stop the Spark session
spark.stop()
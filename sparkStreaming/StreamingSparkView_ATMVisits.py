from pyspark.sql import SparkSession

# TO-DO: create a spark session, with an appropriately named application name
spark = SparkSession.builder.appName('ATMVisits').getOrCreate()

#TO-DO: set the log level to WARN
spark.sparkContext.setLogLevel("WARN")

#TO-DO: read the gear-position kafka topic as a source into a streaming dataframe with the bootstrap server localhost:9092,
# configuring the stream to read the earliest messages possible

gearPositionRawDF = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers","localhost:9092") \
    .option("subscribe", "atm-visits") \
    .option("startingOffsets", "earliest") \
    .load()

#TO-DO: using a select expression on the streaming dataframe, cast the key and the value columns from kafka as strings, and then select them

gearPositionDF=gearPositionRawDF.selectExpr("cast(key as string) key", "cast(value as string) value")

# TO-DO: create a temporary streaming view called "GearPosition" based on the streaming dataframe
gearPositionDF.createOrReplaceTempView("ATMVisits")

# TO-DO: query the temporary view "GearPosition" using spark.sql
gearPositionViewDF=spark.sql("select * from ATMVisits")

# Write the dataframe from the last query to a kafka broker at localhost:9092, with a topic called gear-position-updates
gearPositionViewDF.writeStream.format("kafka") \
    .option("kafka.bootstrap.servers","localhost:9092") \
    .option("topic", "atm-visit-updates") \
    .option("checkpointLocation","/tmp/kafkacheckpoint") \
    .start() \
    .awaitTermination()

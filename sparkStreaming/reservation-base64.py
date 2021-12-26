from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, to_json, col, unbase64, base64, split, expr
from pyspark.sql.types import StructField, StructType, StringType, BooleanType, ArrayType, DateType

redisMessageSchema = StructType(
    [
        StructField("key", StringType()),
        StructField("value", StringType()),
        StructField("expiredType", StringType()),
        StructField("expiredValue",StringType()),
        StructField("existType", StringType()),
        StructField("ch", StringType()),
        StructField("incr",BooleanType()),
        StructField("zSetEntries", ArrayType( \
            StructType([
                StructField("element", StringType()), \
                StructField("score", StringType()) \
                ])) \
                    )

    ]
)

# TO-DO: create a StructType for the Reservation schema for the following fields:
# {"reservationId":"814840107","customerName":"Jim Harris", "truckNumber":"15867", "reservationDate":"Sep 29, 2020, 10:06:23 AM"}
reservationSchema = StructType(
    [
        StructField("reservationId", StringType()),
        StructField("customerName", StringType()),
        StructField("truckNumber", StringType()),
        StructField("reservationDate", StringType())
    ]
)
# TO-DO: create a spark session, with an appropriately named application name
spark = SparkSession.builder.appName("reservation-base64").getOrCreate()

#TO-DO: set the log level to WARN
spark.sparkContext.setLogLevel("WARN")

#TO-DO: read the redis-server kafka topic as a source into a streaming dataframe with the bootstrap server localhost:9092, configuring the stream to read the earliest messages possible
redisServerRawDF = spark.readStream.format("kafka")\
    .option("kafka.bootstrap.servers", "localhost:9092")\
    .option("subscribe", "redis-server")\
    .option("startingOffsets", "earliest")\
    .load()
#TO-DO: using a select expression on the streaming dataframe, cast the key and the value columns from kafka as strings, and then select them
redisServerDF = redisServerRawDF.selectExpr("cast (key as string) key", "cast (value as string) value")

#TO-DO: using the redisMessageSchema StructType, deserialize the JSON from the streaming dataframe
redisServerDeserializedDF = redisServerDF.withColumn("value", from_json("value", redisMessageSchema ))\
    .selectExpr(col("value.*"))\
    .createOrReplaceTempView("RedisData")

# TO-DO: create a temporary streaming view called "RedisData" based on the streaming dataframe
# it can later be queried with spark.sql

#TO-DO: using spark.sql, select key, zSetEntries[0].element as reservation from RedisData
zSetEntriesEncodedDF = spark.sql("select key, zSetEntries[0].element as reservation from RedisData")

#TO-DO: from the dataframe use the unbase64 function to select a column called reservation with the base64 decoded JSON, and cast it to a string
zSetEntriesdecodedDF = zSetEntriesEncodedDF.withColumn("reservation", unbase64(zSetEntriesEncodedDF.reservation).cast("string"))

#TO-DO: using the customer location StructType, deserialize the JSON from the streaming dataframe, selecting column reservation.* as a temporary view called TruckReservation
truckReservationDF = zSetEntriesdecodedDF.withColumn("reservation", from_json(reservationSchema))\
    .select(col("reservation.*"))\
    .createOrReplaceTempView("TruckReservation")

#TO-DO: using spark.sql select * from CustomerLocation
customerLocationDF = spark.sql("select * from CustomerLocation")

# TO-DO: write the stream to the console, and configure it to run indefinitely, the console output will look something like this:

customerLocationDF.writeStream.outputMode("append").format("console")\
    .option("kafka.bootstrap.servers", "localhost:9092")\
    .option("startingOffsets", "earliest")\
    .start()\
    .awaitTermination()


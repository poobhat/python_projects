from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, to_json, col, unbase64, base64, split, expr
from pyspark.sql.types import StructField, StructType, StringType, BooleanType, ArrayType, DateType, IntegerType

# TO-DO: create a Vehicle Status kafka message schema StructType including the following JSON elements:
# {"truckNumber":"5169","destination":"Florida","milesFromShop":505,"odomoterReading":50513}
vehicleStatusSchema = StructType(
    [
        StructField("truckNumber", StringType()),
        StructField("destination", StringType()),
        StructField("milesFromShop", IntegerType()),
        StructField("odomoterReading", IntegerType())

    ]
)

# TO-DO: create a Checkin Status kafka message schema StructType including the following JSON elements:
# {"reservationId":"1601485848310","locationName":"New Mexico","truckNumber":"3944","status":"In"}
checkinStatusSchema = StructType(
    [
        StructField("reservationId", StringType()),
        StructField("locationName", StringType()),
        StructField("truckNumber", StringType()),
        StructField("status", StringType())
    ]
)

# TO-DO: create a spark session, with an appropriately named application name
spark = SparkSession.builder.appName("Vehicle-checkin-status").getOrCreate()

#TO-DO: set the log level to WARN
spark.sparkContext.setLogLevel("WARN")

#TO-DO: read the vehicle-status kafka topic as a source into a streaming dataframe with the bootstrap server localhost:9092, configuring the stream to read the earliest messages possible
vehicleStatusRawDF = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "vehicle-status" ) \
    .option("startingOffsets", "earliest") \
    .load()

vehicleStatusRawDF = vehicleStatusRawDF.selectExpr("cast (key as string) key", "cast (value as string) value")

#TO-DO: using a select expression on the streaming dataframe, cast the key and the value columns from kafka as strings, and then select them
checkinStatusRawDF = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "check-in") \
    .option("startingOffsets", "earliest") \
    .load()

checkinStatusRawDF = checkinStatusRawDF.selectExpr("cast (key as string) key", "cast (value as string) value")

#TO-DO: using the kafka message StructType, deserialize the JSON from the streaming dataframe
vehicleStatusDF = vehicleStatusRawDF.withColumn("value", from_json("value", vehicleStatusSchema)) \
    .select(col("value.*")) \
    .createOrReplaceTempView("VehicleStatus")

# TO-DO: create a temporary streaming view called "VehicleStatus"
# it can later be queried with spark.sql

#TO-DO: using spark.sql, select truckNumber as statusTruckNumber, destination, milesFromShop, odometerReading from VehicleStatus into a dataframe
vehicleStatusViewDF = spark.sql("select truckNumber as statusTruckNumber, destination, milesFromShop, odomoterReading from VehicleStatus")

#TO-DO: read the check-in kafka topic as a source into a streaming dataframe with the bootstrap server localhost:9092, configuring the stream to read the earliest messages possible
checkinStatusDF = checkinStatusRawDF.withColumn("value", from_json("value", checkinStatusSchema)) \
    .select(col("value.*")) \
    .createOrReplaceTempView("VehicleCheckin")

#TO-DO: using a select expression on the streaming dataframe, cast the key and the value columns from kafka as strings, and then select them

#TO-DO: using the kafka message StructType, deserialize the JSON from the streaming dataframe

# TO-DO: create a temporary streaming view called "VehicleCheckin"
# it can later be queried with spark.sql

#TO-DO: using spark.sql, select reservationId, locationName, truckNumber as checkinTruckNumber, status from VehicleCheckin into a dataframe
checkinStatusViewDF = spark.sql("select reservationId, locationName, truckNumber as checkinTruckNumber, status from VehicleCheckin")
#TO-DO: join the customer dataframe with the deposit dataframe

vehicleCheckingStatusDF = vehicleStatusViewDF \
    .join(checkinStatusViewDF, expr("""statusTruckNumber = checkinTruckNumber"""))
# TO-DO: write the stream to the console, and configure it to run indefinitely, the console output will look something like this:

# vehicleCheckingStatusDF.writeStream.outputMode("append").format("console") \
#     .option("kafka.bootstrap.servers", "localhost:9092") \
#     .option("startingOffsets", "earliest") \
#     .start() \
#     .awaitTermination()

vehicleCheckingStatusDF.selectExpr("cast (statusTruckNumber as string) key",
                                   "to_json(struct(*)) as value")\
    .writeStream.format("kafka")\
    .option("kafka.bootstrap.servers", "localhost:9092")\
    .option("startingOffsets", "earliest")\
    .option("topic", "vehicle-checkin-status")\
    .option("checkpointLocation", "/tmp/kafkacheckpoint")\
    .start()\
    .awaitTermination()
# +-----------------+------------+-------------+---------------+-------------+------------+------------------+------+
# |statusTruckNumber| destination|milesFromShop|odometerReading|reservationId|locationName|checkinTruckNumber|status|
# +-----------------+------------+-------------+---------------+-------------+------------+------------------+------+
# |             1445|Pennsylvania|          447|         297465|1602364379489|    Michigan|              1445|    In|
# |             1445|     Colardo|          439|         298038|1602364379489|    Michigan|              1445|    In|
# |             1445|    Maryland|          439|         298094|1602364379489|    Michigan|              1445|    In|
# |             1445|       Texas|          439|         298185|1602364379489|    Michigan|              1445|    In|
# |             1445|    Maryland|          439|         298234|1602364379489|    Michigan|              1445|    In|
# |             1445|      Nevada|          438|         298288|1602364379489|    Michigan|              1445|    In|
# |             1445|   Louisiana|          438|         298369|1602364379489|    Michigan|              1445|    In|
# |             1445|       Texas|          438|         298420|1602364379489|    Michigan|              1445|    In|
# |             1445|       Texas|          436|         298471|1602364379489|    Michigan|              1445|    In|
# |             1445|  New Mexico|          436|         298473|1602364379489|    Michigan|              1445|    In|
# |             1445|       Texas|          434|         298492|1602364379489|    Michigan|              1445|    In|
# +-----------------+------------+-------------+---------------+-------------+------------+------------------+------+




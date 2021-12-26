from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, to_json, col, unbase64, base64, split, expr
from pyspark.sql.types import StructField, StructType, StringType, BooleanType, ArrayType, DateType

# this is a manually created schema - before Spark 3.0.0, schema inference is not automatic

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

# TO-DO: create a StructType for the Payment schema for the following fields:
# {"reservationId":"9856743232","customerName":"Frank Aristotle","date":"Sep 29, 2020, 10:06:23 AM","amount":"946.88"}
paymentSchema = StructType(
    [
        StructField("reservationId", StringType()),
        StructField("customerName", StringType()),
        StructField("date", StringType()),
        StructField("amount", StringType())
    ]
)
# TO-DO: create a spark session, with an appropriately named application name
spark = SparkSession.builder.appName("ReservationPayment").getOrCreate()
#TO-DO: set the log level to WARN
spark.sparkContext.setLogLevel("WARN")
#TO-DO: read the redis-server kafka topic as a source into a streaming dataframe with the bootstrap server localhost:9092, configuring the stream to read the earliest messages possible
redisRawDF = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "redis-server") \
    .option("startingOffsets", "earliest") \
    .load()

#TO-DO: using a select expression on the streaming dataframe, cast the key and the value columns from kafka as strings, and then select them
redisDF = redisRawDF.selectExpr("cast (key as string) as key", "cast (value as string) as value")

#TO-DO: using the redisMessageSchema StructType, deserialize the JSON from the streaming dataframe
# TO-DO: create a temporary streaming view called "RedisData" based on the streaming dataframe
# it can later be queried with spark.sql

redisJSONdeserializedDF = redisDF.withColumn("value", from_json("value", redisMessageSchema)) \
    .select(col("value.*")) \
    .createOrReplaceTempView("RedisData")

#TO-DO: using spark.sql, select key, zSetEntries[0].element as redisEvent from RedisData
zSetEntriesEncodedDF = spark.sql("select key, zSetEntries[0].element as redisEvent from RedisData")

#TO-DO: from the dataframe use the unbase64 function to select a column called redisEvent with the base64 decoded JSON, and cast it to a string
zSetEntriesDecodedDF1 = zSetEntriesEncodedDF.withColumn("redisEvent", unbase64(zSetEntriesEncodedDF.redisEvent).cast("string")) \
    .filter(col("redisEvent").contains("reservationDate"))

#TO-DO: repeat this a second time, so now you have two separate dataframes that contain redisEvent data
zSetEntriesDecodedDF2 = zSetEntriesEncodedDF.withColumn("redisEvent", unbase64(zSetEntriesEncodedDF.redisEvent).cast("string")) \
    .filter(~(col("redisEvent").contains("reservationDate")))

#TO-DO: using the reservation StructType, deserialize the JSON from the first redis decoded streaming dataframe, selecting column reservation.* as a temporary view called Reservation
reservationDF = zSetEntriesDecodedDF1.withColumn("reservation", from_json("redisEvent",reservationSchema)) \
    .select(col("reservation.*")) \
    .createOrReplaceTempView("Reservation")

#TO-DO: using the payment StructType, deserialize the JSON from the second redis decoded streaming dataframe, selecting column payment.* as a temporary view called Payment
paymentDF = zSetEntriesDecodedDF2.withColumn("payment", from_json("redisEvent", paymentSchema)) \
    .select(col("payment.*")) \
    .createOrReplaceTempView("Payment")

#TO-DO: using spark.sql select select reservationId, reservationDate from Reservation where reservationDate is not null
reservationSelectDF = spark.sql("select reservationId, reservationDate from Reservation where reservationDate is not null")

#TO-DO: using spark.sql select reservationId as paymentReservationId, date as paymentDate, amount as paymentAmount from Payment
paymentSelectDF = spark.sql("select reservationId as paymentReservationId, amount as paymentAmount from Payment")

#TO-DO: join the reservation and payment data using the expression: reservationId=paymentReservationId
reservationPaymentDF = reservationSelectDF.join(paymentSelectDF, expr("""
reservationId=paymentReservationId
"""))
# TO-DO: write the stream to the console, and configure it to run indefinitely
# can you find the reservations who haven't made a payment on their reservation?
reservationPaymentDF.writeStream.outputMode("append").format("console").start().awaitTermination()
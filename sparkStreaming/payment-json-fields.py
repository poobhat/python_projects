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

# TO-DO: create a StructType for the Payment schema for the following fields:
# {"reservationId":"9856743232","customerName":"Frank Aristotle","date":"Sep 29, 2020, 10:06:23 AM","amount":"946.88"}
PaymentSchema = StructType(
    [
        StructField("reservationId", StringType()),
        StructField("customerName", StringType()),
        StructField("date", StringType()),
        StructField("amount", StringType())
    ]
)

# TO-DO: create a spark session, with an appropriately named application name
spark = SparkSession.builder.appName("reservation-base64").getOrCreate()

#TO-DO: set the log level to WARN
spark.sparkContext.setLogLevel("WARN")

#TO-DO: read the redis-server kafka topic as a source into a streaming dataframe with the bootstrap server localhost:9092, configuring the stream to read the earliest messages possible
redisServerRawDF = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "redis-server") \
    .option("startingOffsets", "earliest") \
    .load()

#TO-DO: using a select expression on the streaming dataframe, cast the key and the value columns from kafka as strings, and then select them
redisServerDF = redisServerRawDF.selectExpr("cast (key as string) key", "cast (value as string) value")

#TO-DO: using the redisMessageSchema StructType, deserialize the JSON from the streaming dataframe

# TO-DO: create a temporary streaming view called "RedisData" based on the streaming dataframe
# it can later be queried with spark.sql
redisServerDeserializedDF = redisServerDF.withColumn("value", from_json("value", redisMessageSchema )) \
    .select(col("value.*")) \
    .createOrReplaceTempView("RedisData")

#TO-DO: using spark.sql, select key, zSetEntries[0].element as payment from RedisData
zSetEntriesEncodedDF = spark.sql("select key, zSetEntries[0].element as payment from RedisData")

#TO-DO: from the dataframe use the unbase64 function to select a column called payment with the base64 decoded JSON, and cast it to a string
zSetEntriesdecodedDF = zSetEntriesEncodedDF.withColumn("payment", unbase64(zSetEntriesEncodedDF.payment).cast("string"))

#TO-DO: using the payment StructType, deserialize the JSON from the streaming dataframe, selecting column customer.* as a temporary view called Customer
CustomerDF = zSetEntriesdecodedDF.withColumn("payment", from_json("payment", PaymentSchema)) \
    .select(col("payment.*")) \
    .createOrReplaceTempView("Payment")

#TO-DO: using spark.sql select reservationId, amount,  from Payment
CustomerSqlDF = spark.sql("select reservationId, amount  from Payment")

# TO-DO: write the stream in JSON format to a kafka topic called payment-json, and configure it to run indefinitely, the console output will not show any output.
#You will need to type /data/kafka/bin/kafka-console-consumer --bootstrap-server localhost:9092 --topic customer-attributes --from-beginning to see the JSON data
#
# The data will look like this: {"reservationId":"9856743232","amount":"946.88"}
CustomerSqlDF.selectExpr("cast (reservationId as string) as key", "to_json(struct(*)) as value")\
    .writeStream.outputMode("append").format("console") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("startingOffsets", "earliest") \
    .start() \
    .awaitTermination()



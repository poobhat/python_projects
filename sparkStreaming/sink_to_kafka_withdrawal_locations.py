from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, to_json, col, unbase64, base64, split, expr
from pyspark.sql.types import StructField, StructType, StringType, BooleanType, ArrayType, DateType, FloatType, IntegerType

# TO-DO: create bank withdrawals kafka message schema StructType including the following JSON elements from bank-withdrawals topic:
#  {"accountNumber":"703934969","amount":625.8,"dateAndTime":"Sep 29, 2020, 10:06:23 AM","transactionId":1601395583682}
bankWithdrawalsSchema = StructType(
    [
        StructField("accountNumber", StringType()),
        StructField("amount", FloatType()),
        StructField("dateAndTime", StringType()),
        StructField("transactionId", IntegerType())
    ]
)

# TO-DO: create an atm withdrawals kafka message schema StructType including the following JSON elements:
# {"transactionDate":"Sep 29, 2020, 10:06:23 AM","transactionId":1601395583682,"atmLocation":"Thailand"}
atmWithdrawalsSchema = StructType(
    [
        StructField("transactionDate", StringType()),
        StructField("transactionId", IntegerType()),
        StructField("atmLocation", StringType())
    ]
)

# TO-DO: create a spark session, with an appropriately named application name
spark=SparkSession.builder.appName("withdrawalLocations").getOrCreate()

#TO-DO: set the log level to WARN
spark.sparkContext.setLogLevel("WARN")

#TO-DO: read the bank-withdrawals kafka topic as a source into a streaming dataframe with the bootstrap server localhost:9092, configuring the stream to read the earliest messages possible
bankWithdrawalsDF = spark.readStream.format("kafka")\
    .option("kafka.bootstrap.servers","localhost:9092") \
    .option("subscribe", "bank-withdrawals")\
    .option("startingOffsets", "earliest")\
    .load()

#TO-DO: using a select expression on the streaming dataframe, cast the key and the value columns from kafka as strings, and then select them
bankWithdrawalsDF.selectExpr("cast (key as string) key", "cast (value as string) value")

#TO-DO: using the kafka message StructType, deserialize the JSON from the streaming dataframe

# TO-DO: create a temporary streaming view called "BankWithdrawals"
# it can later be queried with spark.sql
bankWithdrawalsDF.withColumn("value", from_json("value", bankWithdrawalsSchema) )\
    .select(col("value.*"))\
    .createOrReplaceTempView("BankWithdrawals")
#TO-DO: using spark.sql, select * from BankWithdrawals into a dataframe

bankWithdrawalsViewDF = spark.sql("select * from BankWithdrawals")
#TO-DO: read the atm-withdrawals kafka topic as a source into a streaming dataframe with the bootstrap server localhost:9092, configuring the stream to read the earliest messages possible
atmWithdrawalsDF = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers","localhost:9092") \
    .option("subscribe", "atm-withdrawals") \
    .option("startingOffsets", "earliest") \
    .load()
#TO-DO: using a select expression on the streaming dataframe, cast the key and the value columns from kafka as strings, and then select them
atmWithdrawalsDF.selectExpr("cast (key as string) key", "cast (value as string) value")

#TO-DO: using the kafka message StructType, deserialize the JSON from the streaming dataframe

# TO-DO: create a temporary streaming view called "AtmWithdrawals"
# it can later be queried with spark.sql
atmWithdrawalsDF.withColumn("value", from_json("value", atmWithdrawalsSchema))\
    .select(col("value.*"))\
    .createOrReplaceTempView("AtmWithdrawals")

#TO-DO: using spark.sql, select * from AtmWithdrawals into a dataframe
atmWithdrawalsViewDF = spark.sql("select * from AtmWithdrawals")

#TO-DO: join the atm withdrawals dataframe with the bank withdrawals dataframe
withdrawalsDF = bankWithdrawalsViewDF.join(atmWithdrawalsViewDF, "transactionId")

# TO-DO: write the stream to the kafka in a topic called withdrawals-location, and configure it to run indefinitely, the console will not output anything. You will want to attach to the topic using the kafka-console-consumer inside another terminal, it will look something like this:
withdrawalsDF.selectExpr("cast (transactionId as string) key", "to_json(struct(*)) as value").writeStream.format("kafka")\
    .option("kafka.bootstrap.servers", "localhost:9092")\
    .option("topic", "withdrawals-location")\
    .option("startingOffsets", "earliest")\
    .option("checkpointLocation", "/tmp/kafkacheckpoint")\
    .start()\
    .awaitTermination()
# {"accountNumber":"862939503","amount":"844.8","dateAndTime":"Oct 7, 2020 12:33:34 AM","transactionId":"1602030814320","transactionDate":"Oct 7, 2020 12:33:34 AM","atmTransactionId":"1602030814320","atmLocation":"Ukraine"}

'''
The Kafka Connect API
In this exercise we're going to make use of the Kafka Connect API.

See the documentation for more information on any of these actions.

Viewing Connectors
First, we can view connector-plugins:

curl http://localhost:8083/connector-plugins | python -m json.tool

% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
Dload  Upload   Total   Spent    Left  Speed
100  1267  100  1267    0     0  20111      0 --:--:-- --:--:-- --:--:-- 20111
[
    {
        "class": "io.confluent.connect.activemq.ActiveMQSourceConnector",
        "type": "source",
        "version": "5.1.4"
    },
    {
        "class": "io.confluent.connect.elasticsearch.ElasticsearchSinkConnector",
        "type": "sink",
        "version": "5.1.4"
    },
    {
        "class": "io.confluent.connect.hdfs.HdfsSinkConnector",
        "type": "sink",
        "version": "5.1.4"
    },
    {
        "class": "io.confluent.connect.hdfs.tools.SchemaSourceConnector",
        "type": "source",
        "version": "2.1.1-cp6"
    },
    {
        "class": "io.confluent.connect.ibm.mq.IbmMQSourceConnector",
        "type": "source",
        "version": "5.1.4"
    },
    {
        "class": "io.confluent.connect.jdbc.JdbcSinkConnector",
        "type": "sink",
        "version": "5.1.4"
    },
    {
        "class": "io.confluent.connect.jdbc.JdbcSourceConnector",
        "type": "source",
        "version": "5.1.4"
    },
    {
        "class": "io.confluent.connect.jms.JmsSourceConnector",
        "type": "source",
        "version": "5.1.4"
    },
    {
        "class": "io.confluent.connect.replicator.ReplicatorSourceConnector",
        "type": "source",
        "version": "5.1.4"
    },
    {
        "class": "io.confluent.connect.s3.S3SinkConnector",
        "type": "sink",
        "version": "5.1.4"
    },
    {
        "class": "io.confluent.connect.storage.tools.SchemaSourceConnector",
        "type": "source",
        "version": "2.1.1-cp6"
    },
    {
        "class": "org.apache.kafka.connect.file.FileStreamSinkConnector",
        "type": "sink",
        "version": "2.1.1-cp6"
    },
    {
        "class": "org.apache.kafka.connect.file.FileStreamSourceConnector",
        "type": "source",
        "version": "2.1.1-cp6"
    }
]

Quick note, the | python -m json.tool above simply takes the output of the curl command and prints the JSON nicely. You can omit this if you'd like!

Create a Connector
Lets create a connector. We'll dive into more details on how this works later.


curl -X POST -H 'Content-Type: application/json' -d '{
"name": "first-connector",
"config": {
    "connector.class": "FileStreamSource",
    "tasks.max": 1,
    "file": "/var/log/journal/confluent-kafka-connect.service.log",
    "topic": "kafka-connect-logs",
    "key.converter":"org.apache.kafka.connect.json.JsonConverter",
    "key.converter.schemas.enable":"false",
    "value.converter":"org.apache.kafka.connect.json.JsonConverter",
    "value.converter.schemas.enable":"false"
}
}' \
  http://localhost:8083/connectors
List connectors
We can list all configured connectors with:

    curl http://localhost:8083/connectors | python -m json.tool

You can see our connector in the list.

    Detailing connectors
Let's list details on our connector:

curl http://localhost:8083/connectors/first-connector | python -m json.tool

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   479  100   479    0     0  13305      0 --:--:-- --:--:-- --:--:-- 13305
{
    "name": "first-connector",
    "config": {
        "connector.class": "FileStreamSource",
        "key.converter.schemas.enable": "false",
        "file": "/var/log/journal/confluent-kafka-connect.service.log",
        "tasks.max": "1",
        "value.converter.schemas.enable": "false",
        "name": "first-connector",
        "topic": "kafka-connect-logs",
        "value.converter": "org.apache.kafka.connect.json.JsonConverter",
        "key.converter": "org.apache.kafka.connect.json.JsonConverter"
    },
    "tasks": [
        {
            "connector": "first-connector",
            "task": 0
        }
    ],
    "type": "source"
}

Pausing connectors
Sometimes its desirable to pause or restart connectors:

To pause:

curl -X PUT http://localhost:8083/connectors/first-connector/pause

To restart:

curl -X POST http://localhost:8083/connectors/first-connector/restart

Deleting connectors
Finally, to delete your connector:

curl -X DELETE http://localhost:8083/connectors/first-connector
'''
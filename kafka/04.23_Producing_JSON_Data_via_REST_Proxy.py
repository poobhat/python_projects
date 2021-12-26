# Please complete TODO items in the code

from dataclasses import asdict, dataclass, field
import json
import time
import random

import requests
from confluent_kafka import avro, Consumer, Producer
from confluent_kafka.avro import AvroConsumer, AvroProducer, CachedSchemaRegistryClient
from faker import Faker


faker = Faker()
REST_PROXY_URL = "http://localhost:8082"


def produce():
    """Produces data using REST Proxy"""

    # TODO: Set the appropriate headers
    #       See: https://docs.confluent.io/current/kafka-rest/api.html#content-types
    headers = {
        "Content-Type":"application/vnd.kafka.json.v2+json"
    }
    # TODO: Define the JSON Payload to b sent to REST Proxy
    #       To create data, use `asdict(ClickEvent())`
    #       See: https://docs.confluent.io/current/kafka-rest/api.html#post--topics-(string-topic_name)
    data = {
        "records":[
            {"value":asdict(ClickEvent())}
        ]
    }
    # TODO: What URL should be used?
    #       See: https://docs.confluent.io/current/kafka-rest/api.html#post--topics-(string-topic_name)
    resp = requests.post(

        f"{REST_PROXY_URL}/topics/lesson4.sample5",
        data=json.dumps(data), headers=headers  # TODO
    )

    try:
        resp.raise_for_status()
    except:
        print(f"Failed to send data to REST Proxy {json.dumps(resp.json(), indent=2)}")

    print(f"Sent data to REST Proxy {json.dumps(resp.json(), indent=2)}")


@dataclass
class ClickEvent:
    email: str = field(default_factory=faker.email)
    timestamp: str = field(default_factory=faker.iso8601)
    uri: str = field(default_factory=faker.uri)
    number: int = field(default_factory=lambda: random.randint(0, 999))


def main():
    """Runs the simulation against REST Proxy"""
    try:
        while True:
            produce()
            time.sleep(0.5)
    except KeyboardInterrupt as e:
        print("shutting down")


if __name__ == "__main__":
    main()

"""
Sent data to REST Proxy {
  "offsets": [
    {
      "partition": 0,
      "offset": 0,
      "error_code": null,
      "error": null
    }
  ],
  "key_schema_id": null,
  "value_schema_id": null
}
Sent data to REST Proxy {
  "offsets": [
    {
      "partition": 0,
      "offset": 1,
      "error_code": null,
      "error": null
    }
  ],
  "key_schema_id": null,
  "value_schema_id": null
}
Sent data to REST Proxy {
  "offsets": [
    {
      "partition": 0,
      "offset": 2,
      "error_code": null,
      "error": null
    }
  ],
  "key_schema_id": null,
  "value_schema_id": null
}
Sent data to REST Proxy {
  "offsets": [
    {
      "partition": 0,
      "offset": 3,
      "error_code": null,
      "error": null
    }
  ],
  "key_schema_id": null,
  "value_schema_id": null
}
Sent data to REST Proxy {
  "offsets": [
    {
      "partition": 0,
      "offset": 4,
      "error_code": null,
      "error": null
    }
  ],
  "key_schema_id": null,
  "value_schema_id": null
}
Sent data to REST Proxy {
  "offsets": [
    {
      "partition": 0,
      "offset": 5,
      "error_code": null,
      "error": null
    }
  ],
  "key_schema_id": null,
  "value_schema_id": null
}
Sent data to REST Proxy {
  "offsets": [
    {
      "partition": 0,
      "offset": 6,
      "error_code": null,
      "error": null
    }
  ],
  "key_schema_id": null,
  "value_schema_id": null
}
Sent data to REST Proxy {
  "offsets": [
    {
      "partition": 0,
      "offset": 7,
      "error_code": null,
      "error": null
    }
  ],
  "key_schema_id": null,
  "value_schema_id": null
}
Sent data to REST Proxy {
  "offsets": [
    {
      "partition": 0,
      "offset": 8,
      "error_code": null,
      "error": null
    }
  ],
  "key_schema_id": null,
  "value_schema_id": null
}
Sent data to REST Proxy {
  "offsets": [
    {
      "partition": 0,
      "offset": 9,
      "error_code": null,
      "error": null
    }
  ],
  "key_schema_id": null,
  "value_schema_id": null
}
Sent data to REST Proxy {
  "offsets": [
    {
      "partition": 0,
      "offset": 10,
      "error_code": null,
      "error": null
    }
  ],
  "key_schema_id": null,
  "value_schema_id": null
}
Sent data to REST Proxy {
  "offsets": [
    {
      "partition": 0,
      "offset": 11,
      "error_code": null,
      "error": null
    }
  ],
  "key_schema_id": null,
  "value_schema_id": null
}
Sent data to REST Proxy {
  "offsets": [
    {
      "partition": 0,
      "offset": 12,
      "error_code": null,
      "error": null
    }
  ],
  "key_schema_id": null,
  "value_schema_id": null
}
Sent data to REST Proxy {
  "offsets": [
    {
      "partition": 0,
      "offset": 13,
      "error_code": null,
      "error": null
    }
  ],
  "key_schema_id": null,
  "value_schema_id": null
}
Sent data to REST Proxy {
  "offsets": [
    {
      "partition": 0,
      "offset": 14,
      "error_code": null,
      "error": null
    }
  ],
  "key_schema_id": null,
  "value_schema_id": null
}
"""
# Please complete the TODO items in the code
import datetime
from dataclasses import asdict, dataclass
import json

import faust


#
# TODO: Define a ClickEvent Record Class with an email (str), timestamp (str), uri(str),
#       and number (int)
#
#       See: https://docs.python.org/3/library/dataclasses.html
#       See: https://faust.readthedocs.io/en/latest/userguide/models.html#model-types
#
@dataclass
class ClickEvent(faust.Record, validation=True, serializer='json'):
    email : int = ""
    timestamp : datetime = ""
    uri : str = ""
    number : int = 0

app = faust.App("exercise2", broker="kafka://localhost:9092")

#
# TODO: Provide the key (uri) and value type to the clickevent
#
clickevents_topic = app.topic(
    "com.udacity.streams.clickevents",
    key_type = str,
    value_type = ClickEvent,
    #key_type=???,
    #value_type=???,
)

@app.agent(clickevents_topic)
async def clickevent(clickevents):
    async for ce in clickevents:
        print(json.dumps(asdict(ce), indent=2))

if __name__ == "__main__":
    app.main()

# Please complete the TODO items in this code

import faust

#
# TODO: Create the faust app with a name and broker
#       See: https://faust.readthedocs.io/en/latest/userguide/application.html#application-parameters
#
app = faust.App('Hello-Faust')

#
# TODO: Connect Faust to com.udacity.streams.clickevents
#       See: https://faust.readthedocs.io/en/latest/userguide/application.html#app-topic-create-a-topic-description
#
topic = app.topic('com.udacity.streams.clickevents')

#
# TODO: Provide an app agent to execute this function on topic event retrieval
#       See: https://faust.readthedocs.io/en/latest/userguide/application.html#app-agent-define-a-new-stream-processor
#
@app.agent(topic)
async def clickevent(clickevents):
# TODO: Define the async for loop that iterates over clickevents
#       See: https://faust.readthedocs.io/en/latest/userguide/agents.html#the-stream
# TODO: Print each event inside the for loop
    async for event in clickevents:
        print(event)

if __name__ == "__main__":
    app.main()

"""
Usage: exercise6.1.py [OPTIONS] COMMAND [ARGS]...

  Welcome, see list of commands and options below.

  Use --help for help, --version for version information.

  https://faust.readthedocs.io

Options:
  --console-port RANGE[1-65535]   when --debug: Port to run debugger console
                                  on.  [default: 50101]

  --blocking-timeout FLOAT        when --debug: Blocking detector timeout.
                                  [default: 10.0]

  -l, --loglevel [crit|error|warn|info|debug]
                                  Logging level to use.  [default: WARN]
  -f, --logfile FILE              Path to logfile (default is <stderr>).
  -L, --loop [aio|gevent|eventlet|uvloop]
                                  Event loop implementation to use.  [default:
                                  aio]

  --json                          Return output in machine-readable JSON
                                  format  [default: False]

  -D, --datadir DIRECTORY         Directory to keep application state.
                                  [default: {conf.name}-data]

  -W, --workdir DIRECTORY         Working directory to change to after start.
  --no-color, --no_color / --color, --color
                                  Enable colors in output.  [default: False]
  --debug / --no-debug            Enable debugging output, and the blocking
                                  detector.  [default: False]

  -q, --quiet / --no-quiet        Silence output to <stdout>/<stderr>.
                                  [default: False]

  -A, --app TEXT                  Path of Faust application to use, or the
                                  name of a module.

  --version                       Show the version and exit.
  --help                          Show this message and exit.

Commands:
  agents          List agents.
  clean-versions  Delete old version directories.
  completion      Output shell completion to be evaluated by the shell.
  livecheck       Manage LiveCheck instances.
  model           Show model detail.
  models          List all available models as a tabulated list.
  reset           Delete local table state.
  send            Send message to agent/topic.
  tables          List available tables.
  worker          Start worker instance for given app.
"""

"""
python exercise6.1.py worker
┌ƒaµS† v1.7.4─┬──────────────────────────────────────────┐
│ id          │ Hello-Faust                              │
│ transport   │ [URL('kafka://localhost:9092')]          │
│ store       │ memory:                                  │
│ web         │ http://localhost:6066/                   │
│ log         │ -stderr- (warn)                          │
│ pid         │ 1056                                     │
│ hostname    │ c8bfca0b6259                             │
│ platform    │ CPython 3.7.3 (Linux x86_64)             │
│ drivers     │                                          │
│   transport │ aiokafka=1.0.6                           │
│   web       │ aiohttp=3.6.2                            │
│ datadir     │ /home/workspace/Hello-Faust-data         │
│ appdir      │ /home/workspace/Hello-Faust-data/v1      │
└─────────────┴──────────────────────────────────────────┘
"""
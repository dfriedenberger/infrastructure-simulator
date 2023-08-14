# infrastructure-simulator

![Infrastructure Simulator](simulator.gif "Simulator")

You can send command via REST interface. See below


## Installation

```
pip install git+https://github.com/dfriedenberger/infrastructure-simulator
```
or
```
pip install -e .
```
## Usage 

see server.py

## Test
```
pip install fastapi hypercorn
python server.py
```

### Send Commands
Switch Point to right
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"point","cmd":"Wn2"}' http://localhost:8080/control/hello-world
```
Switch Blocksignal to Hp1
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"blocksignal","cmd":"Hp1"}' http://localhost:8080/control/hello-
world
```


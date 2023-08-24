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

### Examples

#### Railway
#### Weiche
![](docs/weiche.gif)

##### Commands
###### Wn1
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"Wn1"}' http://localhost:8080/control/<board>
world
```

###### Wn2
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"Wn2"}' http://localhost:8080/control/<board>
world
```


#### AusfahrsignalZs1
![](docs/ausfahrsignalzs1.gif)

##### Commands
###### Hp0+Sh0
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"Hp0+Sh0"}' http://localhost:8080/control/<board>
world
```

###### Hp0+Sh1
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"Hp0+Sh1"}' http://localhost:8080/control/<board>
world
```

###### Hp0+Zs1
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"Hp0+Zs1"}' http://localhost:8080/control/<board>
world
```

###### Hp0+Zs8
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"Hp0+Zs8"}' http://localhost:8080/control/<board>
world
```

###### Zs1
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"Zs1"}' http://localhost:8080/control/<board>
world
```

###### Hp1
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"Hp1"}' http://localhost:8080/control/<board>
world
```

###### Hp2
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"Hp2"}' http://localhost:8080/control/<board>
world
```


#### AusfahrsignalZs2Zs3
![](docs/ausfahrsignalzs2zs3.gif)

##### Commands
###### Hp0+Sh0
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"Hp0+Sh0"}' http://localhost:8080/control/<board>
world
```

###### Hp0+Sh1
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"Hp0+Sh1"}' http://localhost:8080/control/<board>
world
```

###### Hp1
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"Hp1"}' http://localhost:8080/control/<board>
world
```

###### Hp1+Zs2
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"Hp1+Zs2"}' http://localhost:8080/control/<board>
world
```

###### Hp1+Zs3
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"Hp1+Zs3"}' http://localhost:8080/control/<board>
world
```

###### Hp1+Zs2+Zs3
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"Hp1+Zs2+Zs3"}' http://localhost:8080/control/<board>
world
```

###### Hp2
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"Hp2"}' http://localhost:8080/control/<board>
world
```

###### Hp2+Zs2
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"Hp2+Zs2"}' http://localhost:8080/control/<board>
world
```

###### Hp2+Zs3
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"Hp2+Zs3"}' http://localhost:8080/control/<board>
world
```

###### Hp2+Zs2+Zs3
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"Hp2+Zs2+Zs3"}' http://localhost:8080/control/<board>
world
```


#### HauptsignalZs2Zs3
![](docs/hauptsignalzs2zs3.gif)

##### Commands
###### Hp0
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"Hp0"}' http://localhost:8080/control/<board>
world
```

###### Hp0+Zs1
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"Hp0+Zs1"}' http://localhost:8080/control/<board>
world
```

###### Zs1
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"Zs1"}' http://localhost:8080/control/<board>
world
```

###### Hp1
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"Hp1"}' http://localhost:8080/control/<board>
world
```

###### Hp1+Zs2
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"Hp1+Zs2"}' http://localhost:8080/control/<board>
world
```

###### Hp1+Zs3
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"Hp1+Zs3"}' http://localhost:8080/control/<board>
world
```

###### Hp1+Zs2+Zs3
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"Hp1+Zs2+Zs3"}' http://localhost:8080/control/<board>
world
```

###### Hp2
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"Hp2"}' http://localhost:8080/control/<board>
world
```

###### Hp2+Zs2
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"Hp2+Zs2"}' http://localhost:8080/control/<board>
world
```

###### Hp2+Zs3
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"Hp2+Zs3"}' http://localhost:8080/control/<board>
world
```

###### Hp2+Zs2+Zs3
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"Hp2+Zs2+Zs3"}' http://localhost:8080/control/<board>
world
```


#### EinfahrsignalZs1
![](docs/einfahrsignalzs1.gif)

##### Commands
###### Hp0
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"Hp0"}' http://localhost:8080/control/<board>
world
```

###### Hp0+Zs1
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"Hp0+Zs1"}' http://localhost:8080/control/<board>
world
```

###### Hp0+Zs8
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"Hp0+Zs8"}' http://localhost:8080/control/<board>
world
```

###### Zs1
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"Zs1"}' http://localhost:8080/control/<board>
world
```

###### Hp1
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"Hp1"}' http://localhost:8080/control/<board>
world
```

###### Hp2
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"Hp2"}' http://localhost:8080/control/<board>
world
```


#### BlocksignalZs1
![](docs/blocksignalzs1.gif)

##### Commands
###### Hp0
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"Hp0"}' http://localhost:8080/control/<board>
world
```

###### Hp0+Zs1
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"Hp0+Zs1"}' http://localhost:8080/control/<board>
world
```

###### Hp0+Zs8
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"Hp0+Zs8"}' http://localhost:8080/control/<board>
world
```

###### Zs1
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"Zs1"}' http://localhost:8080/control/<board>
world
```

###### Hp1
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"Hp1"}' http://localhost:8080/control/<board>
world
```


#### Trapeztafel2000
![](docs/trapeztafel2000.gif)

##### Commands
###### Sperren
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"on"}' http://localhost:8080/control/<board>
world
```

###### Freigeben
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"off"}' http://localhost:8080/control/<board>
world
```


#### Haltetafel2000
![](docs/haltetafel2000.gif)

##### Commands
###### Sperren
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"on"}' http://localhost:8080/control/<board>
world
```

###### Freigeben
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"off"}' http://localhost:8080/control/<board>
world
```



#### Allgemein
#### Ampel
![](docs/ampel.gif)

##### Commands
###### Halt
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"halt"}' http://localhost:8080/control/<board>
world
```

###### Achtung
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"achtung"}' http://localhost:8080/control/<board>
world
```

###### Fahrt
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"fahrt"}' http://localhost:8080/control/<board>
world
```

###### Fahrt erwarten
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"<item-id>","cmd":"fahrt_erwarten"}' http://localhost:8080/control/<board>
world
```


#### TestBild
![](docs/testbild.gif)

##### Commands




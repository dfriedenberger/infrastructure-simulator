# Ampel

![](ampel.gif)

## Commands
### Halt "halt"

State:
![](ampelhalt.gif)

Example:
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"ampel","cmd":"halt"}' http://localhost:8080/control/hello-world
```



### Achtung "achtung"

State:
![](ampelachtung.gif)

Example:
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"ampel","cmd":"achtung"}' http://localhost:8080/control/hello-world
```



### Fahrt "fahrt"

State:
![](ampelfahrt.gif)

Example:
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"ampel","cmd":"fahrt"}' http://localhost:8080/control/hello-world
```



### Fahrt erwarten "fahrt_erwarten"

State:
![](ampelfahrt_erwarten.gif)

Example:
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"ampel","cmd":"fahrt_erwarten"}' http://localhost:8080/control/hello-world
```







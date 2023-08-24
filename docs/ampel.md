# Ampel

![](ampel.gif)

## Commands
### Halt "halt"

![](ampelhalt.gif)

Example:
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"ampel","cmd":"halt"}' http://localhost:8080/control/hello-world
```



### Achtung "achtung"

![](ampelachtung.gif)

Example:
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"ampel","cmd":"achtung"}' http://localhost:8080/control/hello-world
```



### Fahrt "fahrt"

![](ampelfahrt.gif)

Example:
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"ampel","cmd":"fahrt"}' http://localhost:8080/control/hello-world
```



### Fahrt erwarten "fahrt_erwarten"

![](ampelfahrt_erwarten.gif)

Example:
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"ampel","cmd":"fahrt_erwarten"}' http://localhost:8080/control/hello-world
```







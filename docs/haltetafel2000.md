# Haltetafel2000

![](haltetafel2000.gif)

## Commands
### Sperren "on"

State:
![](haltetafel2000on.gif)

Example:
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"haltetafel2000","cmd":"on"}' http://localhost:8080/control/hello-world
```



### Freigeben "off"

State:
![](haltetafel2000off.gif)

Example:
```
curl --request POST --header "Content-Type: application/json" --data '{"id":"haltetafel2000","cmd":"off"}' http://localhost:8080/control/hello-world
```







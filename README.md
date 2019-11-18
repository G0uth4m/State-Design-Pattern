# State-Design-Pattern
State is a behavioral design pattern that lets an object alter its behavior when its internal state changes. It appears as if the object changed its class.

## Problem Statement : 
Filters used in vehicle renting web(or Android) applications - If the user chooses CAR section, the internal state changes and only the properties/actions related to cars are displayed/performed or if the user chooses BIKE section, only the properties/actions related to bikes are displayed/performed.

## Description : 
The State pattern is closely related to the concept of a Finite-State Machine.

At any given moment, there are two states(CAR and BIKE) which a program can be in. Within any unique state, the program behaves differently, and the program can be switched from one state to another instantaneously.

Initially an object of the 'Transport' class is created. This object by default will behave as if it is in 'BIKE' state. The user can list only the bikes using the 'listVehicles' method; select which bike he/she wants using the 'selectNextVehicle' method. When the 'toggle_wheels' method is called on this object, the internal state changes to 'CAR' state. Now the user can list only the cars using the same method 'listVehicles'; select which car he/she wants using the same method 'selectNextVehicle'.

## Usage (Python3):
```
$ python3 client.py

[*] Choose your option :

1) Change state
2) List vehicles in current state
3) Select next vehicle in current state
4) Quit (or Ctrl+C)

>>> 2
1) TVS
2) Yamaha
3) Duke
4) Activa
5) Bullet
>>> 3
[+] Selecting vehicle... Vehicle is TVS  -  BIKE
>>> 3
[+] Selecting vehicle... Vehicle is Yamaha  -  BIKE
>>> 1
[*] Switching to CARS
>>> 2
1) Swift Dzire
2) Verna
3) Renault Kwid
4) Nano
5) Innova
>>> 3
[+] Selecting vehicle... Vehicle is Swift Dzire  -  CAR
>>> 3
[+] Selecting vehicle... Vehicle is Verna  -  CAR
>>> 4
[-] Exiting ...
```

## Author
* **Goutham** - [G0uth4m](https://github.com/G0uth4m)

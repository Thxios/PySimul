# PySimul
Simulations using pygame

## How to Run
### Setup
windows
```shell
>python -m pip install -r requirements.txt
```

linux
```shell
>python3 -m pip install -r requirements.txt
```

### Run
windows
```shell
>python simulation.py [Simulation Type]
```
linux
```shell
>python3 simulation.py [Simulation Type]
```

## Description

### General
- press <kbd>Space</kbd> to play/pause the simulation
- to change the simulation settings, see `general/config.py` and `simulation/[Simulation Type]/config.py`

### Double Pendulum
![](demo/pendulum.gif)
- commandline argument: `pendulum`

### Elastic Collision
![](demo/elastics.gif)
- commandline argument: `elastics`

### Electric Field
![](demo/electric.gif)
- commandline argument: `electric`


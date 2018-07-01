# TP Matemática superior
Resolución al problema plateado en el tp de matemática superior del primer cuatrimestre del 2018
# Integrantes
* Collado, Juan María
* Sosa Celman, Ignacio Hernán
* Castillo, Marco Andres
# Requisitos
* Python 3.6
# Ejecución
Para resolver con metodo de biseccion
```
python resolver.py biseccion [a] [b]
```
Para resolver con metodo de punto fijo
```
python resolver.py punto-fijo [a] [b]
```
Para resolver con metodo de Newton-Raphson
```
python resolver.py newton-raphson [inicial]
```
Para mostrar la ayuda
```
python resolver.py -h
```
```
python resolver.py [metodo] -h
```
Opcionalmente se puede cambiar el criterio de corte, cota de error y redondeo utilizado
```
python resolver.py biseccion [a] [b] --corte abs --error 0.00001 --redondeo 6
```
Los criterios de corte pueden elegirse entre [abs, rel, funct-val]
Los valores por defecto son:
* Criterio de corte: abs
* Error: 0.00001
* Redondeo: 6


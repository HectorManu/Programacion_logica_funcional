# Notas

La primera tarea es investigar los lenguajes de programación y 

## 13/02/2023

El dia de hoy entregaremo una nfografia y otras cosas. 

La clase de hoy eestaremos viendo prolog 

````
PROLOG  Es un lenguaje de Inteligncie Artificial basada en la Lógica de predicados es declarativo y expresa relaciones entre objeto. 
````

Hay que repesar la lógica de or y ands, la cual le sigue la lógica de predicados o lógica de primer orden. 

- Prolog expresa relaciones entre objetos 

### PROLOG 
* Prolog vive en un mundo pequeño ya que lo que le decimos es lo que cree y solo conoce los hecho que ya le dijeron y asume todos los hecho que le dijeron son verdad, 
* Prolog funciona de manera en la que enlaza verdades que tiene en si miama

- se basa en tres componentes 
    - Hechos 
      - Proposiciones
      - Predicados
        - Objetos
          - Constantes
          - Variables
        - Relaciones
    - Reglas "con estas reglas funciona prolog "
      - Condición esta es entonces 
      - Conjunción es el and
      - Disyunción es el or 
    - Consultas "con estas funciona prolog"
      - Unificación 
      - Recursividad
      - Backtracking 


#### 1 Hecho o predicados 
Aridad es el número e parametros que tiene 
![alt](/img/2023-02-13_01.png)

##### 1 Ejemplo de hecho
Un Funtor tiene un objeto 
![alt](/img/2023-02-13_02.png)

![alt](/img/2023-02-13_03.png)

![alt](/img/2023-02-13_04.png)

Todos los parametros son **atomos** 

#### Reglas para la declaración 

> un **funtor** le da sentido a la 
> si empieza con guión bajo o empieza con mayuscula es una **Variable**
> **NOTA**: UNA VARIABLE SOLO TIENE EL MISMO VALOR EN UNA MISMA LINEA DE CÓDIGO PERO NO A LO LARGO DEL CÓDIGO ES DECIR EN CADA LÍNEA PODEMSO LLAMAR UNA VARIABLE DE LA MISMA MANERA PERO PUEDE TENER UN VALOR DIFERENTE EN CADA LINEA 
> ![alt](/img/2023-02-13_05.png)
>
> **NOTA** EN PROLOG ES **BASE DE HECHOS** EN VEZ DE *BASE DE DATOS*


###
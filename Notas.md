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


## 14/02/2023

Hablamos de la evaluación perezosa en la cual se habla de que es una manera en la cual no crea listas o información hasta que se necesita La disciplina de tipos en Java se refiere al conjunto de reglas y restricciones que se aplican a los tipos de datos utilizados en el lenguaje de programación Java. Esto incluye la verificación de tipos en tiempo de compilación y en tiempo de ejecución para garantizar que las operaciones y asignaciones de valores sean coherentes con los tipos de datos correspondientes.

## 19/02/2023

El día de hoy empezaremos con el microchip consulta el manual [PIC16F84A](https://ww1.microchip.com/downloads/en/devicedoc/35007b.pdf)

Aquí e dificil que pase las 10000 veces de escritura escritura 
viene de 5 voltsy tiene más característias 

En el indice vermos la organicación de memoria 
lo que cambia **esque puede llamar a 8 rutinas de manera consecutiva y tiene 5 vectores de introdcucción es decir que cuando se receteaba pues puede obtar por más de 3 inicios teniendo comolimite 5 inicios al mismo tiempo**

- La memoria de programa es de 2 tenemos 2 bancos 

cuando un registro esta lleno sirve para darle datos al otro como lo podemos ver en la siguiente imagen:

Si los dos registro se llaman igual están mapeados es decir si se modifica Status no quiere decir eque tengs 2 estatus distintos es decir que tiene como un espejo que mapea los dato y si las pilas se llaman distinto entonces tenemos que son de **configuración**.


- Tenemos más memoria es decir tiens 64 de memoria.
- pero es no queire decir que tenemos más memoria es decir si se modifica el banco derecho también se modifica en el banco izquierdo


### Resumen de instrucciones

aquí tenemos las mismas intrucciones pero cambia el tamaño de las palabras antes teniamios del 0 al 4 y ahora **tenemos del 0 al 6** *aumenta en dos*
Cuando tenemos el d 
  d= 0 se almacena en **W**
  d = 1 se almacena en **f**
  d = 7 bit se almacena en un no registro de dirección

  ![imagen](/img/2023-02-16-2.png)


````
LIST P=16F84A

MISTATUS EQU 0X03
MITRISE EQU 0X86 ; SACAR LA INFO
MIPORTB EQU 0X06
CONST EQU 0XF0

ORG 0X0
BSF MISTATUS, 5 ;CAMBIA DE BANCO
MOVF MISTRISB, 

````

## 06/03/2023

### Instanciación y Bactracking

- Las variables representan objetos
- La que lleva guión bajo _ es para indicar el tipo de aridad
- La instanciación, cuando una variable eseta libre e cuando no tiene valor, cuando se instancia pues cuando 
- El termiador de prolog solo son conocidas hasta el punto se dice que su ámbito está solamente desde que inicia hasta el punto.
- La conjunción y la disyunción y la implicación
- y                   o              (si <> entonces **esa se escribe :-**)
  - **:-** la cabeza de la regla y el cuerpo de la regla es el sí entonces o se a el ***if***
- Prolog es un motor de busqueda entonces lo hace como razonamiento hacia atrás o backchageing 
  - entonces primero recorre uan rama e arbol hasta llegr a la última hoja pues esta va recorriendo

## 07/03/2023

hoy dejo tarea y vimos como buscar elemtnos en especifico en prolog


## 13/03/2023

Sistema Experto
SE
sutiere aconseja eespecializado
preguntas al usuario

Un sistema experto le pregunta cosas que el sistema va a saber de algo que el usuario no sabe entonces el usuario le pregunta algo que tú no sabes, los sistemas expertos son especializados
No se puede hacer un sistema experto para todo 

En qué somos expertos 




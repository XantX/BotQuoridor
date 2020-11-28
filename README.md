# BotQuoridor

Bot desarrollado para el curso de complejidad algorítmica

## Integrantes

* Sebastian Diaz Torres u201717471
* Angie Tomasto Cahuana u201817853
* Patrick Vieri Zurita Tenorio U201621873
___

## Enunciado

**Quoridor** es un juego donde el objetivo de cada participante es llegar hast la base del rival, a cada turno se debe escoger entre colocar dificultades como muros o avanzar lo mas probable es que pierdas si te mantienes enfocado en una acción especifica

* Un tablero de 9 x 9 recuadros;
* 4 fichas (una por jugador);
* 20 paredes (tablas que tapan dos casillas, se repartirán equitativamente entre el numero de jugadores)

___

## Mecánica

El objetivo del juego es ser el primero en llegar a cualquier casilla del extremo opuesto del tablero (el lado opuesto a donde inicia el jugador)
Si se desea ser mas estrictos, podría restringir la llegada unicamente a la casilla central del extremo opuesto

En su turno cada jugador deberá tomar una decision:

1. Mover un espacio de forma vertical u horizontal (salvo excepciones)
1. Colocar una barrera (cada barrera bloquea dos cuadros y dene colocarse de manera que lo haga perfectamente para evitar confusiones)

En caso que un jugador quede frente a otro, este en su turno puede escoger salter por encima del primero, en caso de no ser posible, entonces podría mover un espacio en diagonal. Note que de esta forma puede eater ejecutando un movimiento ventajoso (por ser de dos casillas)

![imagen movimientos](https://i1.wp.com/i.imgur.com/cFIwOOV.jpg?resize=463%2C413)

### Figura 1: Movimiento posibles considerando posiciones de muros rivales(Imagen obtenida de [cueva de lobo](https://www.cuevadelobo.com/quoridor-resena/))

___

**Observaciones:** Ningún recuadro debe quedar inaccesible por cause de las barreras. De la anterior, deducimos que ningún jugador podrá quedar encerrado entre barreras

___

## [Documentación a GoogleColab](https://colab.research.google.com/drive/1xzRO5JmERrXhO8frornhBagErcAHlmYx?usp=sharing)

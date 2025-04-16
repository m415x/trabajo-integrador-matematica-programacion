# Trabajo Integrador 1

Articulación de las asignaturas Matemática y Programación 1

## Integrantes

- Ramallo Gerónimo Gastón
- Lahoz Cristian Daniel
- Lagos Alejandro
- Maldonado Ariana
- Mubilla Yanela

## Descripción

Escribimos un programa que cuenta desde 0 hasta 15 y a su vez mostramos cada número en su representación binaria.

Entradas: Para este problema no requerimos entradas ya que contamos con una cantidad exacta de números en este caso 15.

Resolución del problema:

Información de salida:

Link del video:

_Código fuente:_

- Bien indentado, comentado y legible.
- Incluir todo el código que se utilizó para resolver el problema planteado.

_Inteligencia Artificial:_

Consultamos a la inteligencia artificial como hacer para que en la terminal cada línea que se este ejecutando se sobrescriba la línea anterior.

1. \r (Retorno de Carro):
   Este carácter mueve el cursor al principio de la línea actual, sin avanzar a la siguiente.

1. print(..., end=''):
   Normalmente, print() agrega un salto de línea al final. end='' le dice a print() que no agregue un salto de línea, permitiendo que el texto se imprima en la misma línea.

1. Combinación:
   Al imprimir con \r y end='', el texto se sobrescribe en la misma línea, como si estuvieras borrando y escribiendo de nuevo.

```python
import time

for i in range(5):
    print('\rProcesando... %d' % i, end='') # Imprime la actualización en la misma línea
    time.sleep(1)

print('\rProcesamiento completado!') # Imprime la frase final y se desplaza al final de la línea
```

_Importaciones:_

Módulo time.sleep(seg) suspende la ejecución del hilo que lo invoca por el número de segundos dado. El argumento puede ser un número de punto flotante para indicar un tiempo de suspensión más preciso. El tiempo de suspensión real puede ser menor que el solicitado porque cualquier señal detectada terminará la función sleep() siguiendo la rutina de captura de la señal. El tiempo de suspensión también puede ser más largo que el solicitado por una cantidad arbitraria debido a la planificación de otra actividad en el sistema.

_Implementaciones:_

- Implementamos la opción de dar a elegir al usuario hasta que numero se desee convertir a binario o sea desde 0 hasta n cantidad de números y en el caso de que no se ingrese nada cuente por defecto desde 0 hasta 15.

_A tener en cuenta:_

- Integrar los conceptos matemáticos de las dos primeras unidades vistas hasta ahora (Álgebra de Boole y Sistema binario).
- Utilizar solo los contenidos de Programación trabajados hasta el momento.
- Mostrar una aplicación práctica de los saberes y el trabajo colaborativo realizado.
- Reflejar, si corresponde, el uso de IA.

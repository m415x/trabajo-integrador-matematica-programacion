# Trabajo integrador de Matemática con Programación 1

## Integrantes: 
- Ramallo Geronimo Gaston
- Lahoz Cristian Daniel
- Lagos Alejandro
- Maldonado Ariana
- Mubilla Yanela

## Descripcion:
Escribimos un programa que cuenta desde 0 hasta 15 y a su vez mostramos cada número en su representación binaria.

Entradas: Para este problema no requerimos entradas ya que contamos con una cantidad exacta de numeros en este caso 15.

Resolucion del problema:

Informacion de salida:

Link del video: 

Codigo fuente:
- Bien indentado, comentado y legible.
- Incluir todo el código que se utilizó para resolver el problema planteado.

Inteligencia Artificial: 

Explicación:
Consultamos a la inteligencia artificial como hacer para que en la terminal cada linea que se este ejecutando se sobreescriba a la linea anterior.
1. \r (Retorno de Carro):
Este carácter mueve el cursor al principio de la línea actual, sin avanzar a la siguiente.

1. print(..., end=''):
Normalmente, print() agrega un salto de línea al final. end='' le dice a print() que no agregue un salto de línea, permitiendo que el texto se imprima en la misma línea.

1. Combinación:
Al imprimir con \r y end='', el texto se sobreescribe en la misma línea, como si estuvieras borrando y escribiendo de nuevo.
import time

for i in range(5):
    print('\rProcesando... %d' % i, end='')  # Imprime la actualización en la misma línea
    time.sleep(1)

print('\rProcesamiento completado!')  # Imprime la frase final y se desplaza al final de la línea

Importaciones: Módulo time.sleep(seg) suspende la ejecución del hilo que lo invoca por el número de segundos dado. El argumento puede ser un número de punto flotante para indicar un tiempo de suspensión más preciso. El tiempo de suspensión real puede ser menor que el solicitado porque cualquier señal detectada terminará la función sleep() siguiendo la rutina de captura de la señal. El tiempo de suspensión también puede ser más largo que el solicitado por una cantidad arbitraria debido a la planificación de otra actividad en el sistema.

Implementaciones:
- Implementamos la opcion de dar a elegir al usuario hasta que numero se desee convertir a binario osea desde 0 hasta n cantidad de numeros y en el caso de que no se ingrese nada cuente por defecto desde 0 hasta 15.
Ten en cuenta que el proyecto debe:

A tener en cuenta:
- Integrar los conceptos matemáticos de las dos primera unidades vistas hasta
ahora (Álgebra de Boole y Sistema binario).
- Utilizar solo los contenidos de Programación trabajados hasta el momento.
- Mostrar una aplicación práctica de los saberes y el trabajo colaborativo
realizado.
- Reflejar, si corresponde, el uso de IA.

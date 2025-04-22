# Tecnicatura Universitaria en Programación - UTN

## Trabajo Práctico Integrador N° 1

Integración de las asignaturas Matemática y Programación 1. 

## Integrantes

- Lagos Alejandro  
- Lahoz Cristian Daniel  
- Maldonado Ariana  
- Mubilla Yanela  
- Ramallo Gerónimo Gastón
  
**Comisión:** N° 8

## Descripción de la Actividad 

**Actividad:** Contador Binario

**Consigna:**  
Escribimos un programa que, usando un ciclo, cuenta desde 0 hasta 15 y muestra cada número en su representación binaria.  
Como extensión, utilizamos un retardo con `time.sleep()` para simular el conteo de un circuito digital.

## Información de Entrada

Para este problema no requerimos entradas por parte del usuario, ya que el programa cuenta de manera automática desde 0 hasta 15, que es un rango fijo definido en la consigna.

## Resolución del problema

Para resolver el problema utilizamos los siguientes conceptos de programación:

- Usamos un ciclo **for** que recorre automáticamente los números del 0 al 15.
- Aplicamos la función **bin()** de Python para obtener la representación binaria de cada número.
- Usamos el método **zfill(4)** para asegurarnos de que todos los números binarios tengan 4 dígitos, simulando así un contador binario de 4 bits. <span style="color:red;">(esto podríamos poner que lo buscamos con IA)</span>
- Incorporamos la función **time.sleep(1)** para generar un retardo de 1 segundo entre cada número, simulando el ritmo de conteo de un circuito electrónico.
- Validamos que el conteo se mantenga dentro del rango de 0 a 15, cumpliendo con la consigna del ejercicio.
- Incluimos una pequeña mejora opcional que permite elegir si el conteo se realiza de forma ascendente (0 a 15) o descendente (15 a 0), manteniendo siempre el límite definido.

## Información de Salida

El programa imprime por pantalla cada número en su representación binaria de 4 bits, de forma secuencial desde 0000 (que representa el 0) hasta 1111 (que representa el 15).  
Cada número se muestra con una pausa de un segundo entre uno y otro, lo que permite visualizar claramente el conteo en tiempo real.

Link del video:

_Código fuente:_

- Bien indentado, comentado y legible.
- Incluir todo el código que se utilizó para resolver el problema planteado.

_Inteligencia Artificial:_

- Consultamos como hacer para que en la terminal cada línea que se este ejecutando se sobrescriba la línea anterior.

  1. \r (Retorno de Carro):
     Este carácter mueve el cursor al principio de la línea actual, sin avanzar a la siguiente.

  2. print(..., end=''):
     Normalmente, print() agrega un salto de línea al final. end='' le dice a print() que no agregue un salto de línea, permitiendo que el texto se imprima en la misma línea.

  3. Combinación:
     Al imprimir con \r y end='', el texto se sobrescribe en la misma línea, como si estuvieras borrando y escribiendo de nuevo.

```python
import time

for i in range(5):
   print('\rProcesando... %d' % i, end='') # Imprime la actualización en la misma línea
   time.sleep(1)

print('\rProcesamiento completado!') # Imprime la frase final y se desplaza al final de la línea
```

- Consultamos como hacer para imprimir textos en diferentes colores con el módulo colorama.

_Importaciones:_

- Módulo **time** función _sleep(seg)_ suspende la ejecución del hilo que lo invoca por el número de segundos dado. El argumento puede ser un número de punto flotante para indicar un tiempo de suspensión más preciso. El tiempo de suspensión real puede ser menor que el solicitado porque cualquier señal detectada terminará la función sleep() siguiendo la rutina de captura de la señal. El tiempo de suspensión también puede ser más largo que el solicitado por una cantidad arbitraria debido a la planificación de otra actividad en el sistema.
- Modulo **colorama** permite imprimir textos en colores en la salida de la terminal o consola, incluyendo el fondo o estilo del texto, en múltiples plataformas. En la mayoría de las terminales el módulo utiliza internamente las secuencias de escape ANSI o bien las funciones de la API del sistema en Windows para obtener el mismo resultado.

_Implementaciones:_

- Implementamos la opción de dar a elegir al usuario hasta que numero se desee convertir a binario o sea desde 0 hasta n cantidad de números y en el caso de que no se ingrese nada cuente por defecto desde 0 hasta 15.

_A tener en cuenta:_

- Integrar los conceptos matemáticos de las dos primeras unidades vistas hasta ahora (Álgebra de Boole y Sistema binario).
- Utilizar solo los contenidos de Programación trabajados hasta el momento.
- Mostrar una aplicación práctica de los saberes y el trabajo colaborativo realizado.
- Reflejar, si corresponde, el uso de IA.

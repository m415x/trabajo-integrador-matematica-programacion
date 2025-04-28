# Tecnicatura Universitaria en Programación - UTN

## Trabajo Práctico Integrador N° 1
Integración de las asignaturas Matemática y Programación 1. 

## Descripción de la actividad 
Contador Binario en Python 

## 🟢 Versión original: Contador Binario  

**Consigna:**  
Escribir un programa que, usando un ciclo, cuente desde 0 hasta 15 y muestre cada número en su representación binaria.
Como extensión, se debe incluir un retardo (por ejemplo, con time.sleep) para simular el funcionamiento de un circuito real.

## Información de entrada
Esta versión no requiere entradas por parte del usuario. El programa cuenta automáticamente desde 0 hasta 15, un rango fijo definido en la consigna.

## Resolución del problema

Para resolver este ejercicio se utilizaron los siguientes conceptos de programación:
- Se emplea un ciclo **for** para recorrer automáticamente los números del 0 al 15.
- Se usa la función **bin()** de Python para obtener la representación binaria de cada número.
- Aplicamos el método **.zfill(4)** para asegurar que cada número binario tenga exactamente 4 bits, simulando un contador binario típico.
- Se utiliza **time.sleep(1)** para introducir un retardo de 1 segundo entre cada número, simulando el ritmo de un circuito electrónico.
- Se valida que el conteo se mantenga dentro del rango de 0 a 15, respetando la consigna original.

## Información de salida

El programa imprime por pantalla cada número del 0 al 15 en su representación binaria de 4 bits.
La salida se muestra de forma secuencial (ej. 0000, 0001, 0010, ..., 1111), con una pausa de 1 segundo entre cada número, para permitir visualizar el conteo en tiempo real.

## 🟠 Versión 2: Sentido de conteo + Mensaje de bienvenida

Esta versión incorpora una interfaz en consola que presenta un mensaje de bienvenida con colores, y permite al usuario elegir si desea contar de forma ascendente (asc) o 
descendente (desc). También se solicita el número hasta/dese donde se desea contar. Esto hace que el programa sea más interactivo y configurable.

## 🔴 Versión 3: Representación tipo LED

En lugar de mostrar solo el número en binario, esta versión incorpora una visualización tipo LED utilizando emojis de "pelotitas". 

       -  🟡 representa un bit encendido (1)
       -  ⚫ representa un bit apagado (0)
       
Esto simula el funcionamiento de un circuito lógico binario, donde cada bit activa o apaga una luz (como ocurre en contadores digitales reales).
El objetivo es brindar una forma visual e intuitiva de entender cómo se representan los números en binario a nivel físico o electrónico.

## 🔵 Versión 4: Conversión a Octal y Hexadecimal

Además de mostrar la representación binaria, esta versión permite visualizar también el número en octal y hexadecimal, todo en una sola línea y con distintos colores para cada 
sistema numérico. Esto enriquece el programa desde un punto de vista didáctico y técnico.

## 🟣 Versión final: Integración total

En esta última versión se integraron todas las funcionalidades desarrolladas en etapas anteriores, creando un único programa completo, interactivo y visualmente amigable.
El usuario puede personalizar su experiencia eligiendo:
- La dirección del conteo: ascendente (asc) o descendente (desc)
- El valor inicial o final del conteo
Si desea visualizar el resultado:
- Solo en binario con representación LED (emojis)
- O en formato extendido con múltiples sistemas numéricos: decimal, binario, octal y hexadecimal

Además, toda la interfaz está mejorada con colores en la consola, pausas que simulan el ritmo de un circuito real, y una salida ordenada y clara.
Esta versión representa una síntesis de lo aprendido, combinando interacción con el usuario, lógica binaria, representación visual, y conceptos de sistemas numéricos, 
logrando así una simulación simple pero educativa de un contador lógico digital en funcionamiento.


## Presentación del proyecto en YouTube
 🎞️ Link del video: https://www.youtube.com/watch?v=kNnzmHkZLsA
 

## Uso de inteligencia artificial en el proyecto

En este proyecto, la inteligencia artificial fue utilizada para optimizar y automatizar varias partes del código. A continuación, se detallan las consultas realizadas y cómo la IA ayudó en la implementación:

1. **Sobrescribir líneas en la terminal**: Consultamos cómo hacer que cada línea ejecutada en la terminal sobrescriba la línea anterior, mejorando la visualización de los procesos en tiempo real.
   - **Uso de `\r` (Retorno de Carro)**: Este carácter mueve el cursor al inicio de la línea actual sin avanzar a la siguiente, permitiendo sobrescribir el contenido.
   - **Uso de `print(..., end='')`**: Modificamos la función `print()` para evitar que agregue un salto de línea, permitiendo que el texto se imprima en la misma línea.

2. **Impresión de texto en colores con `colorama`**: Consultamos cómo imprimir textos en diferentes colores en la terminal, facilitando la visualización y destacando los mensajes importantes.
   - **Módulo `colorama`**: Permitió resaltar el texto en diferentes colores y estilos, mejorando la legibilidad de los mensajes en la terminal.

3. **Uso del módulo `time` para suspender la ejecución**: Consultamos cómo suspender la ejecución de un hilo durante un período de tiempo determinado, controlando el flujo del programa y mejorando la experiencia del usuario.
   - **Función `time.sleep(seg)`**: Permite pausar la ejecución durante el número de segundos especificado, y la IA ayudó a encontrar la forma correcta de implementarlo.

4. **Aplicación del método `.zfill(4)` para simular un contador binario**: Investigamos cómo asegurar que cada número binario tenga exactamente 4 bits para simular un contador binario.
   - **Uso de `.zfill(4)`**: Garantiza que cada número binario tenga 4 dígitos, como un contador binario típico.
     La IA sugirió el uso del método **`.zfill(4)`**, que agrega ceros a la izquierda de un número binario hasta que alcance un tamaño específico, en este caso 4 bits.
     Esto asegura que los números binarios siempre se representen de manera uniforme, con ceros a la izquierda si es necesario, lo cual es común en sistemas que requieren un formato fijo.
  

## Herramientas tecnológicas utilizadas 

Este proyecto fue desarrollado utilizando las siguientes tecnologías:
<table> <tr> <td align="center"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="60" 
alt="Python Logo" /><br><b>Python</b></td> <td align="center"><img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" width="60" 
alt="VSCode Logo" /><br><b>Visual Studio Code</b></td> <td align="center"><img 
src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" width="60" alt="Git Logo" /><br><b>Git</b></td> </tr> </table>

- Python: Lenguaje de programación utilizado para construir toda la lógica del contador y sus variantes.
- Visual Studio Code: Entorno de desarrollo usado para escribir, depurar y ejecutar el código.
- Git: Sistema de control de versiones utilizado para gestionar el progreso del proyecto y su historial.

## Herramientas para grabación y edición de video

<table>
  <tr>
    <td align="center">
      <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRSWg8QTVqtsX8NyFySoTkrQj7FrbfvZNib8w&s" width="60" alt="OBS Logo" /><br>
      <b>OBS Studio</b>
    </td>
    <td align="center">
      <img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/11/05/b0/1105b015-f3b0-a9a3-b4d4-0ed9d9e9ef4c/AppIcon-0-0-1x_U007emarketing-0-8-0-85-220.png/1200x630wa.png" width="60" alt="Zoom Logo" /><br>
      <b>Zoom</b>
    </td>
    <td align="center">
      <img src="https://cdn.worldvectorlogo.com/logos/capcut-logo-vector.svg" width="60" alt="CapCut Logo" /><br>
      <b>CapCut</b>
    </td>
  </tr>
</table>

- OBS Studio: Utilizado para grabar la ejecución del programa y la interfaz.
- Zoom: Herramienta auxiliar para grabar pantalla o compartir explicaciones en vivo.
- CapCut: Software de edición de video para recortar, agregar texto y mejorar la presentación final.

## Integrantes del equipo
**Comisión:** N° 8

<table border="1">
  <thead>
    <tr>
      <th>Nombre</th>
      <th>Foto</th>
      <th>LinkedIn</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lagos Alejandro</td>
      <td><img src="https://media.licdn.com/dms/image/v2/D4D03AQFV1azd5VG4vQ/profile-displayphoto-shrink_200_200/B4DZZ6JuBhGgAY-/0/1745806095683?e=1751500800&v=beta&t=9aeYHUos_ZA5ZV9sCC0fKPzStW2adSqjfbxve1eQTZI" alt="Foto Alejandro" width="100"></td>
      <td><a href="https://www.linkedin.com/in/alejandro-lagos-8a8633197/">Lagos Alejandro</a></td>
    </tr>
    <tr>
      <td>Lahoz Cristian Daniel</td>
      <td><img src="https://media.licdn.com/dms/image/v2/D4E03AQHWUhZNJ8C_qw/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1724795304271?e=1751500800&v=beta&t=VL2j_wKfQmO5MlhDAlZsGoPbDvGKovJ8FdIMrvt35F4" alt="Foto Cristian" width="100"></td>
      <td><a href="https://www.linkedin.com/in/lahozcristian/">Lahoz Cristian Daniel</a></td>
    </tr>
    <tr>
      <td>Maldonado Ariana</td>
      <td><img src="https://media.licdn.com/dms/image/v2/D4D03AQEthcHd_8VwPQ/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1727565461008?e=1751500800&v=beta&t=SL8JhMPEWTTspykjb_oLNzr40hX6IiA2AXXd-B_f-wI" alt="Foto Ariana" width="100"></td>
      <td><a href="https://www.linkedin.com/in/ariana-maldonado/">Ariana Maldonado</a></td>
    </tr>
    <tr>
      <td>Mubilla Yanela</td>
      <td><img src="https://media.licdn.com/dms/image/v2/D4D03AQHihWsPc19THw/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1730723695846?e=1751500800&v=beta&t=MpmBxO55WgjRoagnGVWPyoWD3WjylKQpXTzULaTI0Kw" alt="Foto Yanela" width="100"></td>
      <td><a href="https://www.linkedin.com/in/yanela-mubilla-683aa3336/">Yanela Mubilla</a></td>
    </tr>
    <tr>
      <td>Ramallo Gerónimo Gastón</td>
      <td><img src="https://media.licdn.com/dms/image/v2/D4D35AQG3EAmDC01g-w/profile-framedphoto-shrink_200_200/B4DZVDjgdqHIAg-/0/1740595136676?e=1746414000&v=beta&t=kED8UTrW4jFhUSuO1LM-hJFob60WEWSPEhrChb74if0" alt="Foto Gerónimo" width="100"></td>
      <td><a href="https://www.linkedin.com/in/geronimo-ramallo/">Ramallo Gerónimo Gastón</a></td>
    </tr>
  </tbody>
</table>

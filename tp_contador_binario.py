## TRABAJO PRÁTICO INTEGRADOR Nº 1 
## Contador Binario

import time  # Importar módulo "time" para hacer pausas.
             
    
def contador_binario():             
    for numero in range (16):        # bucle for: Itera de 0 a 15.
        binario = bin(numero)[2:]    # convierte el número a binario y elimina '0b'.
        binario = binario.zfill(4)   # rellena con ceros a la izquierda para 4 cifras.
        print(binario)               # muestra el número binario en la terminal.
        time.sleep(1)                # pausa de 1 segundo entre cada impresión, para mostrar cada número con intervalo.

contador_binario()                   # llamada a la función para ejecutar el contador.

"""

# JUSTIFICACIÓN
import time                # se importa el módulo time, que contiene funciones relacionadas con el tiempo.
                           # se usará para hacer una pausa de 1 segungo entre cada iteración del bucle. 

def contador_binario():    # se define una función llamada "contador_binario", sin parametros. 

for numero in range (16)   # se inicia un bucle for que itera 16 veces, desde el valor 0 hasta el valor 15 (inclusive). 
                           # range (16): genera los números 0 hasta el 15.


binario = bin(numero)[2:]   # convierte el número entero "numero" en su representación binaria como una cadena de texto. 
                           # el prefijo '0b' indica que es un número binario en Python, pero [2:] se usa para eliminar esos dos primeros caracteres y 
                           # quedarse solo con la parte del número binario. 

binario = binario.zfill(4) # el método zfill(4) se aplica sobre la cadena binario para asegurarse de que tenga 4 caracteres, rellenando con ceros 
                           # a la izquierda si es necesario. 
                           # por ejemplo, si el número binario es '111', se transformará en '0111'.

print(binario)             # se imprime el valor de binario en la consola, mostrando la representación binaria de cada número de la secuencia.

time.sleep(1)              # la función time.sleep(1) hace una pausa de 1 segundo entre cada iteración del bucle. 
                           # esto hace que el programa imprima un número binario por segundo, dándole tiempo al usuario para ver cada uno antes de que el siguiente aparezca.

contador_binario()         # finalmente, se llama a la función contador_binario() para ejecutar el código que hemos definido. 
                           # esto iniciará el proceso de contar del 0 al 15 en binario, mostrando cada número con un retraso de 1 segundo entre cada uno.
"""
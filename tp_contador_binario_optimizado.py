import time  # importar módulo "time" para hacer pausas.

def contador_binario():  
    # preguntar al usuario si quiere ver los números en orden ascendente o descendente.
    orden = input("¿Quieres ver los números en orden ascendente o descendente? (asc/desc): ").lower()

    if  orden == 'asc':                  # si el usuario elige 'asc', contamos de 0 a 15.
        rango = range(16)
    elif orden == 'desc':                # si el usuario elige 'desc', contamos de 15 a 0.
        rango = range(15, -1, -1)
    else:                                # si el usuario no elige 'asc' o 'desc', mostramos mensaje de "error".
        print("Error, define un orden correcto por favor ('asc' o 'desc').")
        return                           # salir de la función. 
            
    for numero in rango:                 # bucle for: Itera sobre el rango elegido por el usuario.
        binario = bin(numero)[2:]        # convierte el número a binario y elimina '0b'.
        binario = binario.zfill(4)       # rellena con ceros a la izquierda para 4 cifras.
        print(f"{binario} = {numero}")   # muestra el número binario seguido de su equivalente decimal.
        time.sleep(1)                    # pausa de 1 segundo entre cada impresión, para mostrar cada número con intervalo.

contador_binario()                       # llamada a la función para ejecutar el contador.

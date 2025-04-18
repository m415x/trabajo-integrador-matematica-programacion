# ========== Importaciones de módulos ==========

# time.sleep(segundos) suspende la ejecución del hilo que lo invoca por el número de segundos dado.
from time import sleep

# Imprime textos en colores en la salida de la terminal
from colorama import init, Fore, Back, Style


# ========== Definición de funciones ==========


def bienvenida():
    """
    Imprime un mensaje de bienvenida al usuario y explica las instrucciones para usar el programa.
    El mensaje incluye opciones para contar hacia adelante o hacia atrás.
    Utiliza la biblioteca colorama para dar formato al texto, incluyendo colores y estilos.
    """
    init()  # Inicializa colorama para que funcione en Windows

    print(
        Back.WHITE  # Fondo blanco
        + Fore.BLACK  # Letras negras
        + Style.BRIGHT  # Letras en negrita
        + "Bienvenida/o al contador binario".upper()  # Convierte el texto a mayúsculas
        + Style.RESET_ALL  # Resetea el estilo a su valor por defecto
    )

    sleep(0.5)  # Pausa de 0.5 segundos antes de mostrar las opciones

    print(
        Fore.RED  # Letras rojas
        + """
Elija una opción:
[1] Contar hacia adelante
[2] Contar hacia atrás
        """
        + Style.RESET_ALL  # Resetea el estilo a su valor por defecto
    )


def contar():
    """
    Utiliza un bucle for para iterar desde 0 hasta 15, imprimiendo cada número en la misma línea.
    Utiliza la función sleep para pausar la ejecución durante 1 segundo entre cada número.
    """
    for i in range(15 + 1):
        print(f"\rContando...{i}", end="")  # Imprime la actualización en la misma línea
        sleep(1)  # Pausa de 1 segundo entre cada número


# Opcional
def sentido_contar():
    """
    Permite al usuario elegir entre contar hacia adelante o hacia atrás.
    Si elige contar hacia adelante, se le pide que ingrese un número hasta donde desea contar.
    Si elige contar hacia atrás, se le pide que ingrese un número desde donde desea contar.
    El sentido de la cuenta se representa como 1 para adelante y -1 para atrás.
    """
    sentido = int(input("> "))

    if sentido == 1:
        print("\nElija el número hasta donde desea contar:")
        numero = int(input("> "))
    elif sentido == 2:
        print("\nElija el número desde donde desea contar:")
        numero = int(input("> "))
        sentido = -1

    return sentido, numero  # Devuelve el sentido de la cuenta y el número elegido


# Opcional: Función que permite elegir entre contar en binario, decimal, octal o hexadecimal.
def funcion_4():
    pass


# ========== Programa principal ==========
bienvenida()
contar()

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
[asc] Contar hacia adelante
[desc] Contar hacia atrás
        """
        + Style.RESET_ALL  # Resetea el estilo a su valor por defecto
    )


def orden_y_rango():
    """
    Permite al usuario elegir entre contar hacia adelante o hacia atrás.
    Si elige contar hacia adelante, se le pide que ingrese un número hasta donde desea contar.
    Si elige contar hacia atrás, se le pide que ingrese un número desde donde desea contar.
    El sentido de la cuenta se representa como 'asc' para adelante y 'desc' para atrás.
    """
    sentido = input("> ")

    if sentido == "asc":
        print("\nElija el número hasta donde desea contar:")
        numero = int(input("> "))
        rango = range(numero + 1)

    elif sentido == "desc":
        print("\nElija el número desde donde desea contar:")
        numero = int(input("> "))
        rango = range(numero, -1, -1)

    return numero, rango  # Devuelve el rango de iteración y el numero ingresado


def contador_binario(numero, rango):  
    print()
    for dec in rango:
        longitud_maxima_binario = len(bin(numero)[2:])
        binario = decimal_a_binario(dec).zfill(longitud_maxima_binario)
        longitud_maxima_decimal = str(numero)

        print(f"\r{binario} = {str(dec).zfill(len(longitud_maxima_decimal))}", end="")
        sleep(1)        


def decimal_a_binario(num):
    if num == 0:
        return "0"
    bits = []
    while num > 0:
        bits.insert(0, str(num % 2))
        num = num // 2
    return ''.join(bits)


def main():
    bienvenida()
    numero, rango = orden_y_rango()
    contador_binario(numero, rango)


# ========== Programa principal ==========

if __name__ == "__main__":
    main()
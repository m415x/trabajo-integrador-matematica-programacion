from time import sleep
from colorama import init, Fore, Back, Style


def bienvenida():
    init()
    print(
        Back.WHITE
        + Fore.BLACK
        + Style.BRIGHT
        + "Bienvenida/o al contador numérico".upper()
        + Style.RESET_ALL
    )
    sleep(0.5)
    print(
        Fore.RED
        + """
Elija una opción:
[asc] Contar hacia adelante
[desc] Contar hacia atrás
        """
        + Style.RESET_ALL
    )


def orden_y_rango():
    sentido = ""
    while sentido not in ["asc", "desc"]:
        sentido = input("> ").lower()
        if sentido not in ["asc", "desc"]:
            print(Fore.RED + "Opción no válida. Use 'asc' o 'desc'." + Style.RESET_ALL)

    numero_valido = False
    while not numero_valido:
        if sentido == "asc":
            print("\nElija el número hasta donde desea contar:")
        else:
            print("\nElija el número desde donde desea contar:")

        numero_input = input("> ")
        if numero_input.isdigit():
            numero = int(numero_input)
            numero_valido = True
        else:
            print(
                Fore.RED + "Debe ingresar un número entero positivo." + Style.RESET_ALL
            )

    rango = range(numero + 1) if sentido == "asc" else range(numero, -1, -1)
    return numero, rango


# incluir octal y hexadecimal
def contador_numerico(numero, rango):

    # Calcular anchos máximos para alinear columnas
    max_bin_len = len(bin(numero)[2:])
    max_dec_len = len(str(numero))
    max_oct_len = len(oct(numero)[2:])
    max_hex_len = len(hex(numero)[2:])

    print()  # Salto de línea

    for dec in rango:
        # Formatear binario y decimal (siempre visibles)
        binario = bin(dec)[2:].zfill(max_bin_len)
        dec_str = str(dec).zfill(max_dec_len)
        octal = oct(dec)[2:].zfill(max_oct_len)
        hexadecimal = hex(dec)[2:].upper().zfill(max_hex_len)
        linea = f"{Fore.YELLOW}{binario}{Style.RESET_ALL} (bin) | {Fore.CYAN}{dec_str}{Style.RESET_ALL} (dec) | {Fore.MAGENTA}{octal}{Style.RESET_ALL} (oct) | {Fore.GREEN}{hexadecimal}{Style.RESET_ALL} (hex)"

        # Imprimir la línea con el formato deseado
        print(f"\r{linea}", end="")
        sleep(1)

    print("\n" + Fore.GREEN + "¡Conteo completado!" + Style.RESET_ALL)


def main():
    bienvenida()
    numero, rango = orden_y_rango()
    contador_numerico(numero, rango)


if __name__ == "__main__":
    main()

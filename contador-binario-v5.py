# ========== Importaciones de módulos ==========

# time.sleep(segundos) suspende la ejecución del hilo que lo invoca por el número de segundos dado.
from time import sleep

# Imprime textos en colores en la salida de la terminal
from colorama import init, Fore, Back, Style


# ========== Definición de funciones ==========


def bienvenida():
    """
    Muestra un mensaje de bienvenida con formato de colores en la terminal.

    La función:
    1. Inicializa colorama para compatibilidad con Windows
    2. Muestra un título con fondo blanco y letras negras
    3. Espera medio segundo
    4. Muestra las opciones disponibles en color rojo

    No recibe parámetros ni retorna valores.
    """
    init()  # Necesario para que colorama funcione correctamente en Windows

    # Imprime el título con formato especial
    print(
        Back.WHITE  # Establece fondo blanco
        + Fore.BLACK  # Establece texto negro
        + Style.BRIGHT  # Texto en negrita
        + " Bienvenida/o al contador numérico ".upper()  # Convierte a mayúsculas
        + Style.RESET_ALL  # Restablece los estilos
    )

    sleep(0.5)  # Pequeña pausa para mejor experiencia de usuario

    # Muestra las opciones disponibles
    print(
        Fore.LIGHTGREEN_EX  # Texto en color verde claro
        + """
Elija una opción:
[asc] Contar hacia adelante
[desc] Contar hacia atrás
        """
        + Style.RESET_ALL  # Restablece los estilos
    )


def orden_y_rango():
    """
    Gestiona la selección del sentido de conteo y el rango numérico.

    La función:
    1. Solicita y valida el sentido de conteo (asc/desc)
    2. Solicita y valida un número entero positivo
    3. Genera el rango adecuado según la selección

    Retorna:
    - numero: int - El número máximo/mínimo del rango
    - rango: range - Objeto range configurado según la dirección de conteo
    """
    sentido = ""  # Variable para almacenar la dirección del conteo

    # Bucle para seguir preguntando hasta que ingrese asc o desc
    while True:
        sentido = input("> ").lower()  # Convertir a minúsculas para comparación

        if sentido == "asc" or sentido == "desc":
            break  # Sale del while si es válido.
        else:
            print(
                Fore.RED
                + "ERROR: Ingresas una opción inválida. Usa 'asc' o 'desc'"
                + Style.RESET_ALL
            )  # Mensaje de error en rojo

    numero_valido = False  # Bandera para controlar la validación numérica

    # Validación del número de conteo
    while not numero_valido:
        # Mensaje contextual según dirección de conteo
        if sentido == "asc":
            print("\nElija el número hasta donde desea contar:")
        else:
            print("\nElija el número desde donde desea contar:")

        numero_input = input("> ")  # Captura la entrada del usuario

        # Verifica si la entrada son solo dígitos (isdigit() solo acepta n° enteros positivos)
        if numero_input.isdigit():
            numero = int(numero_input)  # Conversión a entero
            numero_valido = True  # Marca como válido para salir del bucle
        else:
            print(
                Fore.RED + "Debe ingresar un número entero positivo." + Style.RESET_ALL
            )

    # Generación del rango según dirección seleccionada
    rango = range(numero + 1) if sentido == "asc" else range(numero, -1, -1)

    return numero, rango  # Retorna el número y el rango generado


def contador_numerico(numero, rango):
    """
    Ejecuta el conteo mostrando números decimales y su equivalente en varias bases numéricas.

    Parámetros:
    - numero: int - Número máximo/mínimo del rango
    - rango: range - Secuencia de números a mostrar

    La función:
    1. Pregunta si desea ver representaciones en octal y hexadecimal
    2. Calcula los largos máximos para alineación
    3. Itera sobre el rango mostrando cada número
    4. Formatea la salida con colores y representación visual
    """
    # Preguntar si desea ver otras bases
    print("\n¿Desea ver también las representaciones en octal y hexadecimal? (si / no)")
    mostrar_oct_hex = input("> ").lower() == "si"

    # Calcular anchos máximos para alinear columnas
    max_bin_len = len(bin(numero)[2:])  # [2:] para eliminar '0b' del prefijo
    max_dec_len = len(str(numero))
    max_oct_len = (
        len(oct(numero)[2:]) if mostrar_oct_hex else 0
    )  # [2:] para eliminar '0o' del prefijo
    max_hex_len = (
        len(hex(numero)[2:]) if mostrar_oct_hex else 0
    )  # [2:] para eliminar '0x' del prefijo

    print()  # Salto de línea para mejor presentación

    # Itera sobre cada número en el rango
    for dec in rango:
        # Convierte a binario y rellena con ceros a la izquierda
        binario = decimal_a_binario(dec).zfill(max_bin_len)

        # Formatea el número decimal con ceros a la izquierda
        decimal = str(dec).zfill(max_dec_len)

        # Si se desea mostrar octal y hexadecimal
        if mostrar_oct_hex:
            # Mostrar todas las bases
            octal = oct(dec)[2:].zfill(max_oct_len)
            hexadecimal = hex(dec)[2:].upper().zfill(max_hex_len)

            # Muestra el resultado en la misma línea (\r) con colores
            linea = (
                f"\r{Fore.LIGHTGREEN_EX}{decimal}{Style.RESET_ALL}₁₀ | "
                f"{Fore.LIGHTYELLOW_EX}{binario}{Style.RESET_ALL}₂ | "
                f"{Fore.LIGHTBLUE_EX}{octal}{Style.RESET_ALL}₈ | "
                f"{Fore.LIGHTRED_EX}{hexadecimal}{Style.RESET_ALL}₁₆"
            )

        # Si no se desea mostrar octal y hexadecimal
        else:
            # Llama a la función para obtener la representación de LEDs
            leds = leds_binario(binario)

            # Muestra el resultado en la misma línea (\r) con LEDs
            linea = (
                f"\r{Fore.LIGHTGREEN_EX}{decimal}{Style.RESET_ALL}₁₀ | "
                f"{Fore.LIGHTYELLOW_EX}{binario}{Style.RESET_ALL}₂  {leds}"
            )

        print(linea, end="")  # Muestra el resultado
        sleep(1)  # Pausa de 1 segundo entre números

    # Mensaje de finalización
    print(
        "\n\n" + Fore.LIGHTMAGENTA_EX + "¡Conteo completado!".upper() + Style.RESET_ALL
    )


def leds_binario(binario):
    """
    Convierte una cadena binaria en una representación visual de LEDs.

    Parámetros:
    - binario: str - Cadena que representa un número binario

    Retorna:
    - str - Representación visual de LEDs (🟡 y ⚫)

    Proceso:
    1. Itera sobre cada bit en la cadena binaria
    2. Asigna un LED encendido (🟡) o apagado (⚫) según el valor del bit
    """
    leds = ""  # Cadena para almacenar los emojis de LEDs

    # Construye la cadena de LEDs bit por bit
    for bit in binario:
        if bit == "1":
            leds += "🟡"  # LED encendido
        else:
            leds += "⚫"  # LED apagado

    return leds  # Retorna la representación visual de LEDs


def decimal_a_binario(num):
    """
    Convierte un número decimal a su representación binaria mediante divisiones sucesivas.

    Parámetros:
    - num: int - Número decimal a convertir

    Retorna:
    - str - Representación binaria del número

    Proceso:
    1. Caso especial para 0
    2. Para números positivos:
        - Divide sucesivamente por 2
        - Almacena los restos
        - Ordena los restos en orden inverso
    """
    if num == 0:  # Caso especial para el número 0
        return "0"

    bits = []  # Lista para almacenar los dígitos binarios

    # Conversión mediante divisiones sucesivas
    while num > 0:
        bits.insert(0, str(num % 2))  # Inserta el resto al principio
        num = num // 2  # División entera para continuar el proceso

    return "".join(bits)  # Une los bits para formar el string binario


def main():
    """
    Función principal que coordina la ejecución del programa.

    Flujo:
    1. Muestra mensaje de bienvenida
    2. Obtiene parámetros de conteo
    3. Ejecuta el contador binario
    """
    bienvenida()  # Muestra la interfaz inicial
    numero, rango = orden_y_rango()  # Obtiene configuración del usuario
    contador_numerico(numero, rango)  # Ejecuta el conteo


# ========== Programa principal ==========

if __name__ == "__main__":
    """
    Punto de entrada principal del programa.
    Verifica si el script se ejecuta directamente (no importado) y llama a main().
    """
    main()

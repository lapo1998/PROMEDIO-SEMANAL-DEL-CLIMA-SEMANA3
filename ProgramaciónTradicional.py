#promedio semanal del clima metodo tradicional

def obtener_temperaturas_diarias():
    """
    Función para solicitar al usuario las temperaturas diarias de la semana.
    Retorna una lista con 7 temperaturas (una para cada día).
    """
    print("\n--- Registro de Temperaturas Diarias ---")
    temperaturas = [] # Inicializa una lista vacía para almacenar las temperaturas.
    dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

    # Bucle para iterar a través de cada día de la semana.
    for i in range(7): # Se esperan 7 temperaturas para los 7 días de la semana.
        while True: # Bucle interno para asegurar que la entrada sea válida.
            try:
                # Solicita al usuario la temperatura para el día actual.
                temp_str = input(f"Ingrese la temperatura del {dias_semana[i]} (°C): ")
                temperatura = float(temp_str) # Convierte la entrada a un número flotante (decimal).
                temperaturas.append(temperatura) # Añade la temperatura a la lista.
                break # Sale del bucle interno si la entrada es válida.
            except ValueError:
                # Maneja el error si el usuario ingresa algo que no es un número.
                print("Entrada no válida. Por favor, ingrese un número para la temperatura.")
            except Exception as e:
                # Captura cualquier otro error inesperado.
                print(f"Ocurrió un error inesperado: {e}")

    return temperaturas # Devuelve la lista de temperaturas ingresadas.

def calcular_promedio_semanal(lista_temperaturas):
    """
    Función para calcular el promedio de una lista de temperaturas.
    Recibe una lista de números (temperaturas) como argumento.
    Retorna el promedio de esas temperaturas.
    """
    # Verifica si la lista de temperaturas no está vacía para evitar división por cero.
    if not lista_temperaturas:
        print("La lista de temperaturas está vacía, no se puede calcular el promedio.")
        return 0.0 # Retorna 0.0 si no hay datos.

    # Calcula la suma de todas las temperaturas en la lista.
    suma_temperaturas = sum(lista_temperaturas)
    # Calcula el número de elementos en la lista.
    cantidad_dias = len(lista_temperaturas)
    # Calcula el promedio dividiendo la suma por la cantidad.
    promedio = suma_temperaturas / cantidad_dias

    return promedio # Devuelve el valor del promedio calculado.

def mostrar_resultados(temperaturas_registradas, promedio_calculado):
    """
    Función para mostrar las temperaturas diarias registradas y el promedio semanal.
    Recibe la lista de temperaturas y el promedio como argumentos.
    No retorna ningún valor, solo imprime en consola.
    """
    print("\n--- Resumen Climático Semanal ---")
    dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

    # Muestra cada temperatura con su día correspondiente.
    for i, temp in enumerate(temperaturas_registradas):
        print(f"Temperatura del {dias_semana[i].capitalize()}: {temp:.2f}°C")

    # Muestra el promedio semanal final, formateado a dos decimales.
    print(f"\nEl promedio semanal de la temperatura es: {promedio_calculado:.2f}°C")

# 2. Lógica Principal del Programa (Flujo Tradicional) 

if __name__ == "__main__":
    print("==========================================================")
    print("PROGRAMA DE CÁLCULO DE PROMEDIO SEMANAL DEL CLIMA")
    print("UTILIZANDO PROGRAMACIÓN TRADICIONAL")
    print("==========================================================")

    # Paso 1: Obtener los datos (temperaturas diarias).
    # La función 'obtener_temperaturas_diarias' se encarga de la entrada de datos.
    temperaturas_del_clima = obtener_temperaturas_diarias()

    # Paso 2: Procesar los datos (calcular el promedio).
    # La función 'calcular_promedio_semanal' toma las temperaturas y devuelve el promedio.
    promedio_clima = calcular_promedio_semanal(temperaturas_del_clima)

    # Paso 3: Mostrar los resultados.
    # La función 'mostrar_resultados' se encarga de la salida de información.
    mostrar_resultados(temperaturas_del_clima, promedio_clima)

    print("\nPrograma finalizado.")
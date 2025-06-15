# promedio semanal del clima Programación Orientada a Objetos (POO)

class ClimaSemanal:
    """
    Clase que representa el clima de una semana.
    Encapsula las temperaturas diarias y los métodos para gestionarlas.
    Aplica los principios de encapsulación y abstracción.
    """
    def __init__(self, nombre_ciudad="Ciudad Desconocida"):
        """
        Constructor de la clase ClimaSemanal.
        Inicializa los atributos esenciales para una semana de clima.
        """
        #atributos 
        self.nombre_ciudad = nombre_ciudad 
        self._temperaturas_diarias = []
        # Lista de nombres de días para facilitar la interacción.
        self._dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        print(f"Objeto ClimaSemanal creado para: {self.nombre_ciudad}")

    def registrar_temperaturas(self):
        """
        Método para solicitar y registrar las 7 temperaturas diarias de la semana.
        Este método encapsula la lógica de entrada de datos dentro del objeto.
        """
        print(f"\n--- Registro de Temperaturas para {self.nombre_ciudad} ---")
        self._temperaturas_diarias = [] # Reinicia la lista por si se usa varias veces.

        # Itera 7 veces para obtener las temperaturas de cada día.
        for i in range(7):
            while True: # Bucle para validar la entrada del usuario.
                try:
                    # Solicita la temperatura para el día actual.
                    temp_str = input(f"Ingrese la temperatura del {self._dias_semana[i]} (°C): ")
                    temperatura = float(temp_str) # Convierte la entrada a número.
                    self._temperaturas_diarias.append(temperatura) # Añade la temperatura a la lista interna.
                    break # Sale del bucle interno si la entrada es válida.
                except ValueError:
                    # Maneja el error si el usuario ingresa algo que no es un número.
                    print("Entrada no válida. Por favor, ingrese un número para la temperatura.")
                except Exception as e:
                    # Captura cualquier otro error inesperado.
                    print(f"Ocurrió un error inesperado: {e}")
        print("Registro de temperaturas completado.")

    def _calcular_promedio(self):
        """
        Método "privado" (indicado por _) para calcular el promedio de las temperaturas registradas.
        Este es un método auxiliar interno que encapsula la lógica del cálculo.
        No está diseñado para ser llamado directamente desde fuera de la clase.
        """
        # Verifica si hay temperaturas registradas para evitar errores de división por cero.
        if not self._temperaturas_diarias:
            print("No hay temperaturas registradas para calcular el promedio.")
            return 0.0 # Retorna 0.0 si la lista está vacía.

        suma = sum(self._temperaturas_diarias) # Suma todas las temperaturas.
        cantidad = len(self._temperaturas_diarias) # Obtiene el número de temperaturas.
        promedio = suma / cantidad # Realiza el cálculo del promedio.
        return promedio # Retorna el valor del promedio.

    def mostrar_informe_semanal(self):
        """
        Método para mostrar un informe completo de las temperaturas y el promedio semanal.
        Abstrae la presentación de los datos del clima en un único método.
        """
        print(f"\n--- Informe Climático Semanal para {self.nombre_ciudad} ---")

        # Verifica si hay temperaturas registradas antes de mostrar el informe detallado.
        if not self._temperaturas_diarias:
            print("No se han registrado temperaturas para esta semana.")
            return

        # Muestra las temperaturas diarias con sus respectivos días.
        for i, temp in enumerate(self._temperaturas_diarias):
            print(f"  {self._dias_semana[i].capitalize()}: {temp:.2f}°C")

        # Calcula el promedio utilizando el método interno y lo muestra.
        promedio = self._calcular_promedio() # Llama al método interno _calcular_promedio.
        print(f"\nEl promedio semanal de la temperatura es: {promedio:.2f}°C")
        print("-------------------------------------------------")

    # Métodos "getters" (opcionales pero buenos para la encapsulación)
    def get_temperaturas_diarias(self):
        """
        Método "getter" para obtener una copia de las temperaturas diarias.
        Permite acceder a los datos internos de forma controlada sin exponer la lista original.
        """
        return list(self._temperaturas_diarias) # Retorna una copia para evitar modificaciones externas directas.

    def get_promedio_actual(self):
        """
        Método "getter" para obtener el promedio actual sin mostrar el informe completo.
        """
        return self._calcular_promedio()

# uso del programa (Demostración de POO)

if __name__ == "__main__":
    print("==========================================================")
    print("PROGRAMA DE CÁLCULO DE PROMEDIO SEMANAL DEL CLIMA")
    print("UTILIZANDO PROGRAMACIÓN ORIENTADA A OBJETOS")
    print("==========================================================")

    # Paso 1: Crear una instancia del objeto ClimaSemanal.
    # Abstracción: Estamos trabajando con un "ClimaSemanal", no con listas sueltas de números.
    clima_quito = ClimaSemanal("Quito")

    # Paso 2: Registrar las temperaturas.
    # Encapsulación: El método registrar_temperaturas se encarga de manejar la lista interna.
    clima_quito.registrar_temperaturas()

    # Paso 3: Mostrar el informe semanal.
    # Encapsulación y Abstracción: El método mostrar_informe_semanal presenta todo el resumen.
    # No necesitamos llamar a "_calcular_promedio" directamente desde fuera.
    clima_quito.mostrar_informe_semanal()

    print("\n--- Demostración de Encapsulación (acceso controlado) ---")
    print(f"Temperaturas registradas (via getter): {clima_quito.get_temperaturas_diarias()}")
    print(f"Promedio actual (via getter): {clima_quito.get_promedio_actual():.2f}°C")
    print("\nPrograma finalizado.")
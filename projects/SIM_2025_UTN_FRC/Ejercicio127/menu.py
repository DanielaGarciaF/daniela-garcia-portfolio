# ============================
# Función para mostrar menú principal
# ============================
def mostrar_menu_principal():
    """Muestra el menú principal y obtiene la opción del usuario"""
    print("="*80)
    print("SIMULADOR DE POLIDEPORTIVO - MENÚ PRINCIPAL")
    print("="*80)
    print("\n¿Cómo desea controlar la simulación?")
    print("1. Por TIEMPO máximo (ej: 24 horas, 7 días)")
    print("2. Por CANTIDAD de iteraciones/filas (ej: 12, 20, 50 filas)")
    print("3. Salir")
    print("-" * 40)
    
    while True:
        try:
            opcion = input("Seleccione una opción (1-3): ").strip()
            if opcion in ['1', '2', '3']:
                return int(opcion)
            else:
                print("Por favor seleccione 1, 2 o 3.")
        except ValueError:
            print("Por favor ingrese un número válido.")

def configurar_parada_tiempo():
    """Configura los parámetros para parada por tiempo"""
    print("\n" + "-"*40)
    print("CONFIGURACIÓN POR TIEMPO")
    print("-"*40)
    
    while True:
        try:
            tiempo_input = input("Tiempo máximo de simulación (en horas, ej: 24, 168): ")
            tiempo_horas = float(tiempo_input)
            if tiempo_horas <= 0:
                print("El tiempo debe ser mayor que 0.")
                continue
            tiempo_minutos = tiempo_horas * 60
            print(f"✓ Tiempo configurado: {tiempo_horas} horas ({tiempo_minutos} minutos)")
            return tiempo_minutos
        except ValueError:
            print("Por favor ingrese un número válido.")

def configurar_parada_iteraciones():
    """Configura los parámetros para parada por iteraciones"""
    print("\n" + "-"*40)
    print("CONFIGURACIÓN POR ITERACIONES")
    print("-"*40)
    
    while True:
        try:
            iteraciones_input = input("Número máximo de iteraciones/filas (ej: 12, 20, 50): ")
            max_iteraciones = int(iteraciones_input)
            if max_iteraciones <= 0:
                print("El número de iteraciones debe ser mayor que 0.")
                continue
            print(f"✓ Iteraciones configuradas: {max_iteraciones} filas")
            return max_iteraciones
        except ValueError:
            print("Por favor ingrese un número entero válido.")

def configurar_visualizacion():
    """Configura cuántas filas mostrar al inicio"""
    print("\n" + "-"*40)
    print("CONFIGURACIÓN DE VISUALIZACIÓN")
    print("-"*40)
    
    while True:
        try:
            mostrar_input = input("¿Cuántas filas mostrar al inicio? (ej: 10): ")
            mostrar_primeras = int(mostrar_input)
            if mostrar_primeras < 0:
                print("El número debe ser 0 o positivo.")
                continue
            print(f"✓ Mostrando primeras {mostrar_primeras} filas")
            return mostrar_primeras
        except ValueError:
            print("Por favor ingrese un número entero válido.")

def configurar_semilla():
    """Configura la semilla para reproducibilidad"""
    print("\n" + "-"*40)
    print("CONFIGURACIÓN DE SEMILLA ALEATORIA")
    print("-"*40)
    
    while True:
        semilla_input = input("Semilla para números aleatorios (deje vacío para aleatorio): ").strip()
        if semilla_input == "":
            print("✓ Usando semilla aleatoria")
            return None
        try:
            semilla = int(semilla_input)
            print(f"✓ Usando semilla: {semilla}")
            return semilla
        except ValueError:
            print("Por favor ingrese un número entero o deje vacío.")

def configurar_exportacion_csv():
    """Pregunta si se desea exportar la simulación a CSV"""
    print("\n" + "-"*40)
    print("EXPORTACIÓN DE RESULTADOS")
    print("-"*40)
    
    while True:
        opcion = input("¿Desea generar archivo CSV? (s/n): ").strip().lower()
        if opcion in ("s", "n"):
            return opcion == "s"
        print("Por favor responda 's' o 'n'.")

from menu import *
from simulador import SimuladorVectorial
import random

# ============================
# Ejecución principal
# ============================
if __name__ == "__main__":
    while True:
        # Mostrar menú principal
        opcion = mostrar_menu_principal()
        
        if opcion == 3:
            print("\n¡Gracias por usar el simulador! Hasta luego.")
            break
        
        # Configurar según la opción seleccionada
        if opcion == 1:
            # Parada por tiempo
            limite_tiempo = configurar_parada_tiempo()
            limite_iteraciones = 1000000  # Muy alto para que no sea limitante
            modo_parada = 'tiempo'
        elif opcion == 2:
            # Parada por iteraciones
            limite_iteraciones = configurar_parada_iteraciones()
            limite_tiempo = 1000000 * 60  # Muy alto para que no sea limitante
            modo_parada = 'iteraciones'
        
        # Configuraciones comunes
        mostrar_primeras = configurar_visualizacion()
        semilla = configurar_semilla()
        
        # Configurar semilla si se especificó
        if semilla is not None:
            random.seed(semilla)

        exportar_csv = configurar_exportacion_csv()
        
        # Crear simulador
        simulador = SimuladorVectorial()
        simulador.modo_parada = modo_parada
        simulador.limite_tiempo = limite_tiempo
        simulador.limite_iteraciones = limite_iteraciones
        simulador.exportar_csv = exportar_csv

        # Ejecutar simulación
        print("\n" + "="*80)
        print("INICIANDO SIMULACIÓN CONFIGURADA...")
        print("="*80)
        
        simulador.ejecutar(mostrar_primeras=mostrar_primeras)
        
        # Preguntar si desea realizar otra simulación
        print("\n" + "-"*80)
        continuar = input("¿Desea realizar otra simulación? (s/n): ").strip().lower()
        if continuar != 's':
            print("\n¡Gracias por usar el simulador! Hasta luego.")
            break
        
        print("\n" * 2)  # Espacio entre simulaciones
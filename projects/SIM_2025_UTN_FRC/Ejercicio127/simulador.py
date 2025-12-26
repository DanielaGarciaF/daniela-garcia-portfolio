from typing import List, Dict, Tuple
from estado import EstadoSimulacion
from entidades import Equipo
from distribuciones import (
    generar_rnd,
    box_muller,
    tiempo_exponencial,
    tiempo_normal_box_muller,
    ocupacion_normal_box_muller
)

class SimuladorVectorial:
    """Simulador que trabaja con vectores de estado i-1 e i"""
    def __init__(self):
        self.estados: List[EstadoSimulacion] = []
        self.vector_resultados = []
        self.modo_parada = None  # 'tiempo' o 'iteraciones'
        self.limite_tiempo = None  # en minutos
        self.limite_iteraciones = None
    
        self.max_trazabilidad = 1000
        self.trazabilidad_completa = True    

    def limpiar_ocupacion_si_corresponde(self, estado: EstadoSimulacion):
        # Handball
        if estado.tmp_handball_2_usado:
            estado.tmp_handball_1_disponible = None
            estado.tmp_handball_2_disponible = None
            estado.rnd_ocupacion_handball_1 = None
            estado.rnd_ocupacion_handball_2 = None
            estado.tmp_handball_2_usado = False

        # Football
        if estado.tmp_football_2_usado:
            estado.tmp_football_1_disponible = None
            estado.tmp_football_2_disponible = None
            estado.rnd_ocupacion_football_1 = None
            estado.rnd_ocupacion_football_2 = None
            estado.tmp_football_2_usado = False

        # Basketball
        if estado.tmp_basketball_2_usado:
            estado.tmp_basketball_1_disponible = None
            estado.tmp_basketball_2_disponible = None
            estado.rnd_ocupacion_basketball_1 = None
            estado.rnd_ocupacion_basketball_2 = None
            estado.tmp_basketball_2_usado = False

    def generar_proxima_llegada_handball(self, estado: EstadoSimulacion):
        """Genera la próxima llegada de handball usando z disponibles o generando nuevos"""
        if estado.hay_z_disponible_handball:
            # Usar el z1 (seno) que estaba disponible
            z_a_usar = estado.z_handball_1
            estado.hay_z_disponible_handball = False  # Ya no hay z disponible
        else:
            # Generar nuevos números aleatorios y nuevos números Box-Muller
            estado.rnd_handball_1 = generar_rnd()
            estado.rnd_handball_2 = generar_rnd()
            estado.z_handball_0, estado.z_handball_1 = box_muller(estado.rnd_handball_1, estado.rnd_handball_2)
            z_a_usar = estado.z_handball_0  # Usar z0 (coseno)
            estado.hay_z_disponible_handball = True  # z1 (seno) queda disponible para próxima llegada
        
        # Calcular tiempo de próxima llegada
        estado.tiempo_prox_handball = tiempo_normal_box_muller(z_a_usar, 6, 2)
        estado.prox_llegada_handball = estado.reloj + estado.tiempo_prox_handball
    
    def generar_proxima_llegada_basketball(self, estado: EstadoSimulacion):
        """Genera la próxima llegada de basketball usando z disponibles o generando nuevos"""
        if estado.hay_z_disponible_basketball:
            # Usar el z1 (seno) que estaba disponible
            z_a_usar = estado.z_basketball_1
            estado.hay_z_disponible_basketball = False  # Ya no hay z disponible
        else:
            # Generar nuevos números aleatorios y nuevos números Box-Muller
            estado.rnd_basketball_1 = generar_rnd()
            estado.rnd_basketball_2 = generar_rnd()
            estado.z_basketball_0, estado.z_basketball_1 = box_muller(estado.rnd_basketball_1, estado.rnd_basketball_2)
            z_a_usar = estado.z_basketball_0  # Usar z0 (coseno)
            estado.hay_z_disponible_basketball = True  # z1 (seno) queda disponible para próxima llegada
        
        # Calcular tiempo de próxima llegada
        estado.tiempo_prox_basketball = tiempo_normal_box_muller(z_a_usar, 8, 2)
        estado.prox_llegada_basketball = estado.reloj + estado.tiempo_prox_basketball
    
    def obtener_tiempo_ocupacion_handball(self, estado: EstadoSimulacion):
        """Obtiene tiempo de ocupación para handball"""

        # CASO 1: usar TMP2 ya disponible
        if estado.tmp_handball_2_disponible is not None:
            estado.tmp_handball_2_usado = True
            return estado.tmp_handball_2_disponible

        # CASO 2: generar nuevos valores
        estado.rnd_ocupacion_handball_1 = generar_rnd()
        estado.rnd_ocupacion_handball_2 = generar_rnd()

        z0, z1 = box_muller(
            estado.rnd_ocupacion_handball_1,
            estado.rnd_ocupacion_handball_2
        )

        estado.tmp_handball_1_disponible = ocupacion_normal_box_muller(z0, 80, 20)
        estado.tmp_handball_2_disponible = ocupacion_normal_box_muller(z1, 80, 20)

        return estado.tmp_handball_1_disponible

    def obtener_tiempo_ocupacion_football(self, estado: EstadoSimulacion):
        """Obtiene tiempo de ocupación para football"""

        # CASO 1: usar TMP2 ya disponible
        if estado.tmp_football_2_disponible is not None:
            estado.tmp_football_2_usado = True
            return estado.tmp_football_2_disponible

        # CASO 2: generar nuevos valores
        estado.rnd_ocupacion_football_1 = generar_rnd()
        estado.rnd_ocupacion_football_2 = generar_rnd()

        z0, z1 = box_muller(
            estado.rnd_ocupacion_football_1,
            estado.rnd_ocupacion_football_2
        )

        estado.tmp_football_1_disponible = ocupacion_normal_box_muller(z0, 90, 10)
        estado.tmp_football_2_disponible = ocupacion_normal_box_muller(z1, 90, 10)

        return estado.tmp_football_1_disponible

    def obtener_tiempo_ocupacion_basketball(self, estado: EstadoSimulacion):
        """Obtiene tiempo de ocupación para basketball"""

        # CASO 1: usar TMP2 ya disponible
        if estado.tmp_basketball_2_disponible is not None:
            estado.tmp_basketball_2_usado = True
            return estado.tmp_basketball_2_disponible

        # CASO 2: generar nuevos valores
        estado.rnd_ocupacion_basketball_1 = generar_rnd()
        estado.rnd_ocupacion_basketball_2 = generar_rnd()

        z0, z1 = box_muller(
            estado.rnd_ocupacion_basketball_1,
            estado.rnd_ocupacion_basketball_2
        )

        estado.tmp_basketball_1_disponible = ocupacion_normal_box_muller(z0, 100, 30)
        estado.tmp_basketball_2_disponible = ocupacion_normal_box_muller(z1, 100, 30)

        return estado.tmp_basketball_1_disponible

    def determinar_proximo_evento(self, estado: EstadoSimulacion) -> Tuple[str, float]:
        """Determina el próximo evento a ocurrir"""
        eventos = []
        
        # Llegadas
        if estado.prox_llegada_handball < float('inf'):
            eventos.append(("Llegada_H", estado.prox_llegada_handball))
        if estado.prox_llegada_football < float('inf'):
            eventos.append(("Llegada_F", estado.prox_llegada_football))
        if estado.prox_llegada_basketball < float('inf'):
            eventos.append(("Llegada_B", estado.prox_llegada_basketball))
        
        # Fin de juego 
        if estado.prox_fin_juego < float('inf'):
            eventos.append(("Fin_Juego", estado.prox_fin_juego))

        # Fin de acondicionamiento
        if estado.prox_fin_acondicionamiento < float('inf'):
             eventos.append(("Fin_Acondicionamiento", estado.prox_fin_acondicionamiento))

        # Si no hay eventos, terminar
        if not eventos:
            return ("Fin", float('inf'))
        
        # Encontrar el evento más próximo
        return min(eventos, key=lambda x: x[1])
    
    def manejar_llegada(self, tipo: str, estado: EstadoSimulacion):
        """Maneja la llegada de un equipo"""
        # Crear nuevo equipo
        if tipo == "H":
            id_equipo = estado.id_counter_handball
            estado.id_counter_handball += 1
        elif tipo == "F":
            id_equipo = estado.id_counter_football
            estado.id_counter_football += 1
        else:  # B
            id_equipo = estado.id_counter_basketball
            estado.id_counter_basketball += 1
        
        equipo = Equipo(tipo, id_equipo, estado.reloj)
        estado.equipos.append(equipo)
        
        # Agregar a la cola correspondiente
        if tipo == "B":
            estado.cola_basketball.append(equipo)
        else:
            estado.cola_handball_football.append(equipo)
        
        # Programar próxima llegada del mismo tipo
        if tipo == "H":
            self.generar_proxima_llegada_handball(estado)
        elif tipo == "F":
            estado.rnd_football = generar_rnd()
            estado.tiempo_prox_football = tiempo_exponencial(estado.rnd_football, 10)
            estado.prox_llegada_football = estado.reloj + estado.tiempo_prox_football
        else:  # B
            self.generar_proxima_llegada_basketball(estado)
        
        # Intentar asignar cancha
        self.asignar_cancha(estado)
    
    def asignar_cancha(self, estado):

        if estado.estado_servidor != "Libre":
            return

        hay_fh = len(estado.cola_handball_football) > 0
        cant_b = len(estado.cola_basketball)

        if not hay_fh and cant_b == 0:
            return

        # ===============================
        # DECISIÓN DE PRIORIDAD (DOMINIO)
        # ===============================

        if cant_b >= 2:
            # Basketball PRIORIDAD por tener 2 esperando
            equipos = [
                estado.cola_basketball.pop(0),
                estado.cola_basketball.pop(0)
            ]
            self.iniciar_basketball(equipos, estado)
            return

        if cant_b == 1 and not hay_fh:
            # Único Basket y no hay otros esperando
            equipo = estado.cola_basketball.pop(0)
            self.iniciar_basketball([equipo], estado)
            return

        # Caso contrario → prioridad H/F
        if hay_fh:
            equipo = estado.cola_handball_football.pop(0)
            self.iniciar_equipo_individual(equipo, estado)

    def iniciar_equipo_individual(self, equipo, estado):
        # Caso con acondicionamiento
        if estado.ultima_disciplina is not None and equipo.tipo != estado.ultima_disciplina:
            estado.estado_servidor = "Acondicionamiento"
            estado.equipos_actuales = [equipo]
            estado.prox_fin_acondicionamiento = estado.reloj + 10
            return

        # ✅ INICIO DE SERVICIO UNIFICADO
        self.iniciar_servicio(equipo, estado)

        # Tiempo de ocupación
        if equipo.tipo == "H":
            tiempo = self.obtener_tiempo_ocupacion_handball(estado)
        else:  # F
            tiempo = self.obtener_tiempo_ocupacion_football(estado)

        estado.equipos_actuales = [equipo]
        estado.estado_servidor = f"Ocupado_{equipo.tipo}"
        estado.prox_fin_juego = estado.reloj + tiempo

    def iniciar_basketball(self, equipos, estado):
        if estado.ultima_disciplina is not None and estado.ultima_disciplina != "B":
            estado.estado_servidor = "Acondicionamiento"
            estado.equipos_actuales = equipos
            estado.prox_fin_acondicionamiento = estado.reloj + 10
            return

        tiempo = self.obtener_tiempo_ocupacion_basketball(estado)
        estado.estado_servidor = "Ocupado_B"
        estado.equipos_actuales = equipos
        estado.prox_fin_juego = estado.reloj + tiempo

        # ✅ TODOS pasan por iniciar_servicio
        for e in equipos:
            self.iniciar_servicio(e, estado)

    def iniciar_servicio(self, equipo: Equipo, estado: EstadoSimulacion):
        """Inicia el servicio de un equipo y actualiza estadísticas"""
        equipo.iniciar_juego(estado.reloj)

        if equipo.tipo == "H":
            estado.equipos_handball_atendidos += 1
            estado.tiempo_espera_handball += equipo.tiempo_espera

        elif equipo.tipo == "F":
            estado.equipos_football_atendidos += 1
            estado.tiempo_espera_football += equipo.tiempo_espera

        else:  # B
            estado.equipos_basketball_atendidos += 1
            estado.tiempo_espera_basketball += equipo.tiempo_espera
        
    def manejar_fin_juego(self, estado):

        for equipo in estado.equipos_actuales:
            equipo.finalizar_juego(estado.reloj)
            estado.ultima_disciplina = equipo.tipo

        estado.equipos_actuales = []
        estado.estado_servidor = "Libre"
        estado.prox_fin_juego = float("inf")

        self.asignar_cancha(estado)

    def manejar_fin_acondicionamiento(self, estado: EstadoSimulacion):
        equipos = estado.equipos_actuales

        # ✅ TODOS inician servicio juntos
        for e in equipos:
            self.iniciar_servicio(e, estado)

        tipo = equipos[0].tipo
        estado.estado_servidor = f"Ocupado_{tipo}"
        estado.ultima_disciplina = tipo

        # Tiempo de ocupación
        if tipo == "H":
            tiempo = self.obtener_tiempo_ocupacion_handball(estado)
        elif tipo == "F":
            tiempo = self.obtener_tiempo_ocupacion_football(estado)
        else:
            tiempo = self.obtener_tiempo_ocupacion_basketball(estado)

        estado.prox_fin_juego = estado.reloj + tiempo
        estado.prox_fin_acondicionamiento = float("inf")

    def ejecutar_paso(self, estado_anterior: EstadoSimulacion) -> EstadoSimulacion:
        """Ejecuta un paso de la simulación"""
        estado = EstadoSimulacion(estado_anterior)
        
        self.limpiar_ocupacion_si_corresponde(estado)

        # Determinar próximo evento
        evento, tiempo_evento = self.determinar_proximo_evento(estado)
        
        # Avanzar reloj al tiempo del evento
        estado.reloj = tiempo_evento
        estado.evento_actual = evento
        
        # Manejar el evento
        if evento == "Llegada_H":
            self.manejar_llegada("H", estado)
        elif evento == "Llegada_F":
            self.manejar_llegada("F", estado)
        elif evento == "Llegada_B":
            self.manejar_llegada("B", estado)
        elif evento == "Fin_Juego":
            self.manejar_fin_juego(estado)
        elif evento == "Fin_Acondicionamiento":
            self.manejar_fin_acondicionamiento(estado)
        elif evento == "Fin":
            # No hay más eventos programados
            pass
        
        return estado
    
    def crear_vector_fila(self, estado: EstadoSimulacion, iteracion: int) -> Dict:
        """Crea una fila para el vector de resultados"""

        # =============================
        # Formateo de colas
        # =============================
        cola_fh = ", ".join(str(e) for e in estado.cola_handball_football)
        cola_b = ", ".join(str(e) for e in estado.cola_basketball)

        # =============================
        # Equipos actuales en cancha
        # =============================
        equipos_actuales = ", ".join(str(e) for e in estado.equipos_actuales)

        # =============================
        # Z usados Handball
        # =============================
        z_handball_usado = None
        if estado.hay_z_disponible_handball:
            z_handball_usado = (
                estado.z_handball_1
                if estado.z_handball_1 is not None
                else estado.z_handball_0
            )
        else:
            z_handball_usado = (
                estado.z_handball_0
                if estado.z_handball_0 is not None
                else None
            )

        # =============================
        # Z usados Basketball
        # =============================
        z_basketball_usado = None
        if estado.hay_z_disponible_basketball:
            z_basketball_usado = (
                estado.z_basketball_1
                if estado.z_basketball_1 is not None
                else estado.z_basketball_0
            )
        else:
            z_basketball_usado = (
                estado.z_basketball_0
                if estado.z_basketball_0 is not None
                else None
            )

        # =============================
        # === EQUIPOS (COLUMNAS CLAVE) ===
        # =============================
       
        if self.trazabilidad_completa or iteracion <= self.max_trazabilidad:
            equipos_id = ", ".join(e.id for e in estado.equipos)
            equipos_estado = ", ".join(
                f"{e.id}:{e.estado}" for e in estado.equipos
            )
            equipos_tmp_llegada = ", ".join(
                f"{e.id}:{round(e.tiempo_llegada, 2)}" for e in estado.equipos
            )
        else:
            equipos_id = ""
            equipos_estado = ""
            equipos_tmp_llegada = ""

        # =============================
        # Vector
        # =============================
        return {
            "Iteracion": len(self.estados) - 1,
            "Evento": estado.evento_actual,
            "Reloj (min)": round(estado.reloj, 2),
            "Reloj (h)": round(estado.reloj / 60, 2),

            # ---------- Handball ----------
            "RND1_H": round(estado.rnd_handball_1, 4) if estado.rnd_handball_1 is not None else "",
            "RND2_H": round(estado.rnd_handball_2, 4) if estado.rnd_handball_2 is not None else "",
            "Z0_H": round(estado.z_handball_0, 4) if estado.z_handball_0 is not None else "",
            "Z1_H": round(estado.z_handball_1, 4) if estado.z_handball_1 is not None else "",
            "Z_Usado_H": round(z_handball_usado, 4) if z_handball_usado is not None else "",
            "Tmp_Prox_H": round(estado.tiempo_prox_handball, 2) if estado.tiempo_prox_handball is not None else "",
            "Prox_Llegada_H": round(estado.prox_llegada_handball, 2)
            if estado.prox_llegada_handball != float("inf") else "",

            # ---------- Football ----------
            "RND_F": round(estado.rnd_football, 4) if estado.rnd_football is not None else "",
            "Tmp_Prox_F": round(estado.tiempo_prox_football, 2) if estado.tiempo_prox_football is not None else "",
            "Prox_Llegada_F": round(estado.prox_llegada_football, 2)
            if estado.prox_llegada_football != float("inf") else "",

            # ---------- Basketball ----------
            "RND1_B": round(estado.rnd_basketball_1, 4) if estado.rnd_basketball_1 is not None else "",
            "RND2_B": round(estado.rnd_basketball_2, 4) if estado.rnd_basketball_2 is not None else "",
            "Z0_B": round(estado.z_basketball_0, 4) if estado.z_basketball_0 is not None else "",
            "Z1_B": round(estado.z_basketball_1, 4) if estado.z_basketball_1 is not None else "",
            "Z_Usado_B": round(z_basketball_usado, 4) if z_basketball_usado is not None else "",
            "Tmp_Prox_B": round(estado.tiempo_prox_basketball, 2) if estado.tiempo_prox_basketball is not None else "",
            "Prox_Llegada_B": round(estado.prox_llegada_basketball, 2)
            if estado.prox_llegada_basketball != float("inf") else "",

            # ---------- Ocupación Handball ----------
            "RND1_Ocup_H": round(estado.rnd_ocupacion_handball_1, 4)
                if estado.rnd_ocupacion_handball_1 is not None else "",
            "RND2_Ocup_H": round(estado.rnd_ocupacion_handball_2, 4)
                if estado.rnd_ocupacion_handball_2 is not None else "",
            "TMP1_Ocup_H": round(estado.tmp_handball_1_disponible, 2)
                if estado.tmp_handball_1_disponible is not None else "",
            "TMP2_Ocup_H": round(estado.tmp_handball_2_disponible, 2)
                if estado.tmp_handball_2_disponible is not None else "",

            # ---------- Ocupación Football ----------
            "RND1_Ocup_F": round(estado.rnd_ocupacion_football_1, 4)
                if estado.rnd_ocupacion_football_1 is not None else "",
            "RND2_Ocup_F": round(estado.rnd_ocupacion_football_2, 4)
                if estado.rnd_ocupacion_football_2 is not None else "",
            "TMP1_Ocup_F": round(estado.tmp_football_1_disponible, 2)
                if estado.tmp_football_1_disponible is not None else "",
            "TMP2_Ocup_F": round(estado.tmp_football_2_disponible, 2)
                if estado.tmp_football_2_disponible is not None else "",

            # ---------- Ocupación Basketball ----------
            "RND1_Ocup_B": round(estado.rnd_ocupacion_basketball_1, 4)
                if estado.rnd_ocupacion_basketball_1 is not None else "",
            "RND2_Ocup_B": round(estado.rnd_ocupacion_basketball_2, 4)
                if estado.rnd_ocupacion_basketball_2 is not None else "",
            "TMP1_Ocup_B": round(estado.tmp_basketball_1_disponible, 2)
                if estado.tmp_basketball_1_disponible is not None else "",
            "TMP2_Ocup_B": round(estado.tmp_basketball_2_disponible, 2)
                if estado.tmp_basketball_2_disponible is not None else "",

            # ---------- Ocupación ----------
            "Proximo_Fin_Juego": round(estado.prox_fin_juego, 2)
            if estado.prox_fin_juego != float("inf") else "",

            # ---------- Colas ----------
            "Cola_FH": cola_fh,
            "Cola_B": cola_b,

            # ---------- Servidor ----------
            "Estado_Servidor": estado.estado_servidor,
            "Equipos_Actuales": equipos_actuales,

            # ---------- Estadísticas ----------
            "Cant_H_Atend": estado.equipos_handball_atendidos,
            "Acu_Espera_H": round(estado.tiempo_espera_handball, 2),
            "Cant_F_Atend": estado.equipos_football_atendidos,
            "Acu_Espera_F": round(estado.tiempo_espera_football, 2),
            "Cant_B_Atend": estado.equipos_basketball_atendidos,
            "Acu_Espera_B": round(estado.tiempo_espera_basketball, 2),

            # ---------- Equipos ----------
            "Equipos_ID": equipos_id,
            "Equipos_Estado": equipos_estado,
            "Equipos_TMP_Llegada": equipos_tmp_llegada,

            # ---------- Control ----------
            "Equipos_Lista": len(estado.equipos),
            "Z_Disp_H": estado.hay_z_disponible_handball,
            "Z_Disp_B": estado.hay_z_disponible_basketball,
        }

    
    def ejecutar(self, mostrar_primeras: int = 10):
        """Ejecuta la simulación completa con el criterio de parada seleccionado"""
        print("="*80)
        print("INICIANDO SIMULACIÓN...")
        print("="*80)
        print(f"Modo de parada: {'TIEMPO' if self.modo_parada == 'tiempo' else 'ITERACIONES'}")
        if self.modo_parada == 'tiempo':
            print(f"Tiempo máximo: {self.limite_tiempo/60:.1f} horas ({self.limite_tiempo} minutos)")
        else:
            print(f"Iteraciones máximas: {self.limite_iteraciones} filas")
        print()

        if self.modo_parada == "iteraciones" and self.limite_iteraciones > self.max_trazabilidad:
            self.trazabilidad_completa = False

        if self.modo_parada == "tiempo":  
            self.trazabilidad_completa = False
        
        # Estado inicial
        estado_inicial = EstadoSimulacion()
        self.estados.append(estado_inicial)
        self.vector_resultados.append(self.crear_vector_fila(estado_inicial, iteracion=0))
        
        iteracion = 0
        seguir = True
        
        while seguir:
            estado_anterior = self.estados[-1]
            
            # Verificar si hay eventos pendientes
            evento, tiempo_evento = self.determinar_proximo_evento(estado_anterior)
            if evento == "Fin":
                # No hay más eventos programados
                print("No hay más eventos programados. Finalizando simulación.")
                break
            
            # Verificar criterio de parada según el modo seleccionado
            if self.modo_parada == 'tiempo':
                # Parar por tiempo: si el próximo evento supera el tiempo límite
                if tiempo_evento > self.limite_tiempo:
                    print(f"Próximo evento ({tiempo_evento/60:.2f}h) supera el tiempo límite ({self.limite_tiempo/60:.2f}h).")
                    seguir = False
                    break
            elif self.modo_parada == 'iteraciones':
                # Parar por iteraciones: si alcanzamos el límite de filas
                if iteracion >= self.limite_iteraciones:
                    print(f"Alcanzado el límite de {self.limite_iteraciones} iteraciones.")
                    seguir = False
                    break
            
            # Ejecutar un paso
            nuevo_estado = self.ejecutar_paso(estado_anterior)
            self.estados.append(nuevo_estado)

            iteracion += 1
            self.vector_resultados.append(
                self.crear_vector_fila(nuevo_estado, iteracion)
            )
            
            # Mostrar progreso cada 10 iteraciones
            if iteracion % 10 == 0:
                print(f"Progreso: Iteración {iteracion}, Reloj: {nuevo_estado.reloj/60:.2f}h")
        
        print(f"\nSimulación completada en {iteracion} iteraciones")
        print(f"Tiempo final: {self.estados[-1].reloj/60:.2f} horas")
        
        # Mostrar resultados según lo solicitado
        self.mostrar_resultados(mostrar_primeras)
        
        # Generar reporte final
        self.generar_reporte()
        
        # Exportar a CSV
        if getattr(self, "exportar_csv", False):
            self.exportar_a_csv()
        else:
            print("\n(No se generó archivo CSV)")
    
    def mostrar_resultados(self, mostrar_primeras: int):
        """Muestra las primeras filas y las últimas dos según configuración"""
        print("\n" + "="*80)
        print("VECTOR DE SIMULACIÓN")
        print("="*80)
        
        total_filas = len(self.vector_resultados)
        
        # Ajustar cuántas filas mostrar al inicio
        filas_a_mostrar_inicio = min(mostrar_primeras, total_filas)
        
        # Mostrar las primeras filas
        if filas_a_mostrar_inicio > 0:
            print(f"\n--- PRIMERAS {filas_a_mostrar_inicio} FILAS ---")
            self.mostrar_tabla(self.vector_resultados[:filas_a_mostrar_inicio])
        
        # Mostrar las últimas 2 filas SI hay más filas que las mostradas al inicio
        if total_filas > filas_a_mostrar_inicio:
            print(f"\n--- ÚLTIMAS 2 FILAS ---")
            self.mostrar_tabla(self.vector_resultados[-2:])
        elif total_filas == filas_a_mostrar_inicio and total_filas >= 2:
            # Si solo hay las filas mostradas al inicio, mostrar las últimas 2 de esas
            print(f"\n--- ÚLTIMAS 2 FILAS (de las mostradas) ---")
            self.mostrar_tabla(self.vector_resultados[-2:])
        
        print(f"\nTotal de filas generadas: {total_filas}")
    
    def mostrar_tabla(self, filas: List[Dict]):
        """Muestra una tabla legible con ancho dinámico por columna"""

        if not filas:
            return

        COLUMNAS_VISIBLES = [
            "Iteracion",
            "Evento",
            "Reloj (min)",
            "Reloj (h)",
            "Prox_Llegada_H",
            "Prox_Llegada_F",
            "Prox_Llegada_B",
            "Proximo_Fin_Juego",
            "Cola_FH",
            "Cola_B",
            "Estado_Servidor",
            "Equipos_Actuales",
            "Cant_H_Atend",
            "Acu_Espera_H",
            "Cant_F_Atend",
            "Acu_Espera_F",
            "Cant_B_Atend",
            "Acu_Espera_B",
        ]

        columnas = [c for c in COLUMNAS_VISIBLES if c in filas[0]]

        # =============================
        # Calcular ancho por columna
        # =============================
        anchos = {}
        for col in columnas:
            max_dato = max(len(str(fila.get(col, ""))) for fila in filas)
            anchos[col] = max(len(col), max_dato) + 2

        # =============================
        # Encabezado
        # =============================
        header = " | ".join(col.ljust(anchos[col]) for col in columnas)
        print(header)
        print("-" * len(header))

        # =============================
        # Filas
        # =============================
        for fila in filas:
            row = " | ".join(str(fila.get(col, "")).ljust(anchos[col]) for col in columnas)
            print(row)

    def generar_reporte(self):
        """Genera un reporte con los resultados finales"""
        estado_final = self.estados[-1]
        
        print("\n" + "="*80)
        print("REPORTE FINAL DE SIMULACIÓN")
        print("="*80)
        
        print("\n--- ESTADÍSTICAS POR DISCIPLINA ---")
        
        for tipo, nombre in [("H", "HANDBALL"), ("F", "FOOTBALL"), ("B", "BASKETBALL")]:
            if tipo == "H":
                cantidad = estado_final.equipos_handball_atendidos
                tiempo_total = estado_final.tiempo_espera_handball
            elif tipo == "F":
                cantidad = estado_final.equipos_football_atendidos
                tiempo_total = estado_final.tiempo_espera_football
            else:
                cantidad = estado_final.equipos_basketball_atendidos
                tiempo_total = estado_final.tiempo_espera_basketball
            
            if cantidad > 0:
                promedio = tiempo_total / cantidad
                print(f"\n{nombre}:")
                print(f"  Equipos atendidos: {cantidad}")
                print(f"  Tiempo promedio de espera: {promedio:.2f} min ({promedio/60:.2f} h)")
                print(f"  Tiempo total de espera: {tiempo_total:.2f} min")
            else:
                print(f"\n{nombre}: No hubo equipos atendidos")
        
        print("\n--- ESTADO FINAL ---")
        print(f"Reloj final: {estado_final.reloj/60:.2f} horas")
        print(f"Estado del servidor: {estado_final.estado_servidor}")
        print(f"Equipos en cola F/H: {len(estado_final.cola_handball_football)}")
        print(f"Equipos en cola B: {len(estado_final.cola_basketball)}")
        print(f"Total de equipos creados: {len(estado_final.equipos)}")
    
    def exportar_a_csv(self):
        """Exporta los resultados a un archivo CSV con columnas por equipo,
        mostrando FINALIZADO solo la primera vez que ocurre.
        """

        if not self.vector_resultados:
            print("No hay datos para exportar")
            return

        import os
        from datetime import datetime
        import pandas as pd


        df = pd.DataFrame(self.vector_resultados)

        filas_expand = []
        max_equipos = 0

        # =============================
        # Calcular máximo de equipos
        # =============================
        for _, fila in df.iterrows():
            ids = fila.get("Equipos_ID", "")
            cant = len(ids.split(", ")) if ids else 0
            max_equipos = max(max_equipos, cant)

        # =============================
        # Estados anteriores por equipo
        # =============================
        estados_previos = {}   # clave: ID equipo → estado anterior

        # =============================
        # Expandir filas
        # =============================
        for _, fila in df.iterrows():
            nueva_fila = fila.drop(
                ["Equipos_ID", "Equipos_Estado", "Equipos_TMP_Llegada"],
                errors="ignore"
            ).to_dict()

            ids = fila.get("Equipos_ID", "").split(", ") if fila.get("Equipos_ID") else []
            estados = fila.get("Equipos_Estado", "").split(", ") if fila.get("Equipos_Estado") else []
            tmps = fila.get("Equipos_TMP_Llegada", "").split(", ") if fila.get("Equipos_TMP_Llegada") else []

            for i in range(max_equipos):
                idx = i + 1

                if i < len(ids):
                    eq_id = ids[i]
                    estado_actual = estados[i].split(":")[1]
                    tmp_llegada = float(tmps[i].split(":")[1])

                    estado_anterior = estados_previos.get(eq_id)

                    # 🔴 REGLA DEFINITIVA
                    if estado_actual == "Finalizado" and estado_anterior == "Finalizado":
                        # No mostrar más
                        nueva_fila[f"Equipo_{idx}_ID"] = ""
                        nueva_fila[f"Equipo_{idx}_Estado"] = ""
                        nueva_fila[f"Equipo_{idx}_TMP_Llegada"] = ""
                    else:
                        nueva_fila[f"Equipo_{idx}_ID"] = eq_id
                        nueva_fila[f"Equipo_{idx}_Estado"] = estado_actual
                        nueva_fila[f"Equipo_{idx}_TMP_Llegada"] = tmp_llegada

                    # Actualizar estado previo
                    estados_previos[eq_id] = estado_actual

                else:
                    nueva_fila[f"Equipo_{idx}_ID"] = ""
                    nueva_fila[f"Equipo_{idx}_Estado"] = ""
                    nueva_fila[f"Equipo_{idx}_TMP_Llegada"] = ""

            filas_expand.append(nueva_fila)

        df_final = pd.DataFrame(filas_expand)

        # =============================
        # Ordenar columnas
        # =============================
        column_order = [
            'Iteracion', 'Evento', 'Reloj (min)', 'Reloj (h)',

            'RND1_H', 'RND2_H', 'Tmp_Prox_H', 'Prox_Llegada_H',
            'RND_F', 'Tmp_Prox_F', 'Prox_Llegada_F',
            'RND1_B', 'RND2_B', 'Tmp_Prox_B', 'Prox_Llegada_B',

            'RND1_Ocup_H', 'RND2_Ocup_H', 'TMP1_Ocup_H', 'TMP2_Ocup_H',
            'RND1_Ocup_F', 'RND2_Ocup_F', 'TMP1_Ocup_F', 'TMP2_Ocup_F',
            'RND1_Ocup_B', 'RND2_Ocup_B', 'TMP1_Ocup_B', 'TMP2_Ocup_B',

            'Proximo_Fin_Juego',
            'Cola_FH', 'Cola_B',
            'Estado_Servidor', 'Equipos_Actuales',

            'Cant_H_Atend', 'Acu_Espera_H',
            'Cant_F_Atend', 'Acu_Espera_F',
            'Cant_B_Atend', 'Acu_Espera_B',
            'Equipos_Lista',
        ]

        for i in range(1, max_equipos + 1):
            column_order.extend([
                f"Equipo_{i}_ID",
                f"Equipo_{i}_Estado",
                f"Equipo_{i}_TMP_Llegada"
            ])

        df_final = df_final[column_order]

        # =============================
        # Carpeta de simulaciones
        # =============================
        carpeta = "simulaciones"
        os.makedirs(carpeta, exist_ok=True)

        # =============================
        # Nombre del archivo con fecha y hora
        # =============================
        timestamp = datetime.now().strftime("%d%m%Y_%H%M")
        nombre_archivo = f"Simulacion{timestamp}.csv"
        ruta_archivo = os.path.join(carpeta, nombre_archivo)
        df_final.to_csv(ruta_archivo, index=False, encoding="utf-8")

        print(f"\nDatos exportados a {ruta_archivo}")
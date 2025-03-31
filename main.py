"""
Academic Performance Analyzer
Proyecto para la Universidad de Santander (UDES)
Este sistema analiza el rendimiento académico de estudiantes, programas y facultades.
"""

import os
import sys

# Función para limpiar la consola de forma cross-platform
# !Falta testear en MacOS
def clear_screen():
    """
    Limpia la pantalla de la terminal según el sistema operativo.
    """
    os.system("cls" if os.name == "nt" else "clear")


# Datos
# Posible mejora, administrar la data con archivos JSON para tener persistencia de datos
estudiantes = [
    {"codigo": "2020115001", "nombre": "Carolina Martínez Ruiz", "programa": "Ingeniería de Software", "semestre": 7},
    {"codigo": "2021220034", "nombre": "Andrés Felipe Gómez", "programa": "Medicina", "semestre": 5},
    {"codigo": "2022118092", "nombre": "Valentina Sánchez Torres", "programa": "Ingeniería de Software", "semestre": 3},
    {"codigo": "2019456123", "nombre": "Juan Carlos Ramírez", "programa": "Administración de Empresas", "semestre": 8},
    {"codigo": "2023110056", "nombre": "Daniela Hernández Díaz", "programa": "Psicología", "semestre": 2},
    {"codigo": "2020119045", "nombre": "Miguel Ángel Quintero", "programa": "Ingeniería de Software", "semestre": 6},
    {"codigo": "2021345087", "nombre": "Laura Sofía Parra", "programa": "Derecho", "semestre": 5},
    {"codigo": "2020112089", "nombre": "Santiago Ortiz Méndez", "programa": "Ingeniería de Software", "semestre": 7},
    {"codigo": "2022230078", "nombre": "Isabella Castro Rojas", "programa": "Enfermería", "semestre": 3},
    {"codigo": "2021116032", "nombre": "David Alejandro Moreno", "programa": "Ingeniería de Software", "semestre": 5}
]

asignaturas = [
    {"codigo": "IS2045", "nombre": "Fundamentos de Programación", "creditos": 4, "programa": "Ingeniería de Software"},
    {"codigo": "IS3067", "nombre": "Gestores de Bases de Datos", "creditos": 3, "programa": "Ingeniería de Software"},
    {"codigo": "IS4023", "nombre": "Diseño de Software I", "creditos": 3, "programa": "Ingeniería de Software"},
    {"codigo": "CB1015", "nombre": "Cálculo Diferencial", "creditos": 4, "programa": "Ciencias Básicas"},
    {"codigo": "CB1024", "nombre": "Física Mecánica", "creditos": 4, "programa": "Ciencias Básicas"}
]

calificaciones = [
    {"codigo_estudiante": "2020115001", "codigo_asignatura": "IS3067", "nota": 4.2, "periodo": "2023-1"},
    {"codigo_estudiante": "2020115001", "codigo_asignatura": "IS4023", "nota": 3.8, "periodo": "2023-1"},
    {"codigo_estudiante": "2020119045", "codigo_asignatura": "IS3067", "nota": 3.5, "periodo": "2023-1"},
    {"codigo_estudiante": "2020119045", "codigo_asignatura": "IS4023", "nota": 4.0, "periodo": "2023-1"},
    {"codigo_estudiante": "2020112089", "codigo_asignatura": "IS3067", "nota": 4.5, "periodo": "2023-1"},
    {"codigo_estudiante": "2020112089", "codigo_asignatura": "IS4023", "nota": 4.3, "periodo": "2023-1"},
    {"codigo_estudiante": "2022118092", "codigo_asignatura": "CB1015", "nota": 3.2, "periodo": "2023-1"},
    {"codigo_estudiante": "2022118092", "codigo_asignatura": "CB1024", "nota": 2.8, "periodo": "2023-1"},
    {"codigo_estudiante": "2021116032", "codigo_asignatura": "CB1015", "nota": 3.6, "periodo": "2023-1"},
    {"codigo_estudiante": "2021116032", "codigo_asignatura": "CB1024", "nota": 3.4, "periodo": "2023-1"},
    
    {"codigo_estudiante": "2020115001", "codigo_asignatura": "IS2045", "nota": 4.7, "periodo": "2023-2"},
    {"codigo_estudiante": "2020119045", "codigo_asignatura": "IS2045", "nota": 3.9, "periodo": "2023-2"},
    {"codigo_estudiante": "2022118092", "codigo_asignatura": "IS2045", "nota": 2.9, "periodo": "2023-2"},
    {"codigo_estudiante": "2020112089", "codigo_asignatura": "IS2045", "nota": 4.2, "periodo": "2023-2"},
    {"codigo_estudiante": "2021116032", "codigo_asignatura": "IS2045", "nota": 3.8, "periodo": "2023-2"},
    {"codigo_estudiante": "2021116032", "codigo_asignatura": "IS3067", "nota": 4.1, "periodo": "2023-2"},
    {"codigo_estudiante": "2022118092", "codigo_asignatura": "IS3067", "nota": 3.0, "periodo": "2023-2"},
    {"codigo_estudiante": "2020115001", "codigo_asignatura": "CB1015", "nota": 4.3, "periodo": "2023-2"},
    {"codigo_estudiante": "2020119045", "codigo_asignatura": "CB1015", "nota": 3.7, "periodo": "2023-2"},
    {"codigo_estudiante": "2020112089", "codigo_asignatura": "CB1015", "nota": 4.8, "periodo": "2023-2"},
    
    {"codigo_estudiante": "2021116032", "codigo_asignatura": "IS4023", "nota": 3.2, "periodo": "2024-1"},
    {"codigo_estudiante": "2022118092", "codigo_asignatura": "IS4023", "nota": 2.7, "periodo": "2024-1"},
    {"codigo_estudiante": "2020115001", "codigo_asignatura": "CB1024", "nota": 3.9, "periodo": "2024-1"},
    {"codigo_estudiante": "2020119045", "codigo_asignatura": "CB1024", "nota": 3.5, "periodo": "2024-1"},
    {"codigo_estudiante": "2020112089", "codigo_asignatura": "CB1024", "nota": 4.6, "periodo": "2024-1"},
    {"codigo_estudiante": "2021116032", "codigo_asignatura": "CB1024", "nota": 3.3, "periodo": "2024-1"},
    {"codigo_estudiante": "2022118092", "codigo_asignatura": "CB1015", "nota": 3.4, "periodo": "2024-1"},
    {"codigo_estudiante": "2020115001", "codigo_asignatura": "IS4023", "nota": 4.5, "periodo": "2024-1"},
    {"codigo_estudiante": "2020119045", "codigo_asignatura": "IS4023", "nota": 4.2, "periodo": "2024-1"},
    {"codigo_estudiante": "2020112089", "codigo_asignatura": "IS3067", "nota": 4.7, "periodo": "2024-1"}
]

facultades = {
    "Facultad de Ingenierías": ["Ingeniería de Software", "Ingeniería Civil", "Ingeniería Ambiental"],
    "Facultad de Ciencias de la Salud": ["Medicina", "Enfermería", "Psicología"],
    "Facultad de Ciencias Económicas, Administrativas y Contables": ["Administración de Empresas", "Contaduría Pública"],
    "Facultad de Ciencias Sociales, Políticas y Jurídicas": ["Derecho", "Comunicación Social"]
}

# Diccionario de programas para evitar errores de escritura por consola (código -> nombre)
programas = {
    "IS": "Ingeniería de Software",
    "MD": "Medicina",
    "AE": "Administración de Empresas",
    "PSI": "Psicología",
    "DER": "Derecho"
}

# Función genérica para registrar una entidad en una lista como estudiantes, asignaturas, calificaciones ya que todas tienen la misma logica
def registrar_entidad(entidad, lista_destino):
    """
    Registra una entidad en la lista destino.

    Parámetros:
        entidad: Diccionario con la información de la entidad.
        lista_destino: Lista donde se agregará la entidad.
    """
    try:
        lista_destino.append(entidad)
    except Exception as e:
        reportar_error(f"Error al registrar entidad: {e}")

# Función de orden superior: filtrar calificaciones usando una función de filtro ingresada como parámetro
def filtrar_calificaciones(lista, filtro_func):
    """
    Filtra una lista de calificaciones usando una función de filtro.

    Parámetros:
        lista: Lista de calificaciones.
        filtro_func: Función que devuelve True/False.
    Retorna:
        Lista filtrada.
    """
    return [item for item in lista if filtro_func(item)]

# Funciones de análisis individual
def calcular_promedio_estudiante(codigo_estudiante, periodo=None, calificaciones=calificaciones):
    """
    Calcula el promedio de un estudiante.
    
    Parámetros:
        codigo_estudiante: Código del estudiante.
        periodo: (Opcional) Periodo académico (ej. "2023-1").
    Retorna:
        Promedio o None.
    """
    try:
        notas = [reg["nota"] for reg in calificaciones if reg["codigo_estudiante"] == codigo_estudiante and (reg["periodo"] == periodo if periodo else True)]
        if not notas:
            return None
        return sum(notas) / len(notas)
    except Exception as e:
        reportar_error(f"Error al calcular promedio para {codigo_estudiante}: {e}")
        return None

def obtener_historial_academico(codigo_estudiante, calificaciones=calificaciones):
    """
    Obtiene el historial académico de un estudiante.
    
    Parámetros:
        codigo_estudiante: Código del estudiante.
    Retorna:
        Lista de registros.
    """
    try:
        historial = [reg for reg in calificaciones if reg["codigo_estudiante"] == codigo_estudiante]
        if not historial:
            raise ValueError("No se encontró historial para el estudiante.")
        return historial
    except Exception as e:
        reportar_error(f"Error al obtener historial para {codigo_estudiante}: {e}")
        return []

def analizar_desempeno_estudiante(codigo_estudiante, calificaciones=calificaciones):
    """
    Identifica la asignatura con mejor y peor desempeño de un estudiante.
    
    Parámetros:
        codigo_estudiante: Código del estudiante.
    Retorna:
        Diccionario con 'mejor' y 'peor' desempeño.
    """
    try:
        registros = [reg for reg in calificaciones if reg["codigo_estudiante"] == codigo_estudiante]
        if not registros:
            raise ValueError("No hay registros para el estudiante.")
        mejor = max(registros, key=lambda x: x["nota"])
        peor = min(registros, key=lambda x: x["nota"])
        return {"mejor": mejor, "peor": peor}
    except Exception as e:
        reportar_error(f"Error en desempeño para {codigo_estudiante}: {e}")
        return {}

# Funciones de análisis por programa académico
def promedio_programa(programa, periodo, calificaciones=calificaciones, estudiantes=estudiantes):
    """
    Calcula el promedio general de un programa en un periodo.
    
    Parámetros:
        programa: Nombre del programa.
        periodo: Periodo académico.
    Retorna:
        Promedio o None.
    """
    try:
        codigos_prog = [est["codigo"] for est in estudiantes if est["programa"] == programa]
        notas = [reg["nota"] for reg in calificaciones if reg["codigo_estudiante"] in codigos_prog and reg["periodo"] == periodo]
        if not notas:
            raise ValueError("No se encontraron calificaciones para el programa en ese periodo.")
        return sum(notas) / len(notas)
    except Exception as e:
        reportar_error(f"Error al calcular promedio para el programa {programa} en {periodo}: {e}")
        return None

def asignaturas_mayor_reprobacion(programa, periodo, calificaciones=calificaciones, asignaturas=asignaturas, estudiantes=estudiantes):
    """
    Identifica asignaturas con mayor índice de reprobación en un programa para un periodo.
    
    Parámetros:
        programa: Nombre del programa.
        periodo: Periodo académico.
    Retorna:
        Lista de asignaturas con porcentaje de reprobación.
    """
    try:
        codigos_prog = [est["codigo"] for est in estudiantes if est["programa"] == programa]
        regs = [reg for reg in calificaciones if reg["codigo_estudiante"] in codigos_prog and reg["periodo"] == periodo]
        stats = {}
        for reg in regs:
            codigo_asig = reg["codigo_asignatura"]
            stats.setdefault(codigo_asig, {"total": 0, "reprobados": 0})
            stats[codigo_asig]["total"] += 1
            if reg["nota"] < 3.0:
                stats[codigo_asig]["reprobados"] += 1
        resultados = []
        for codigo, datos in stats.items():
            porcentaje = datos["reprobados"] / datos["total"]
            nombre_asig = next((a["nombre"] for a in asignaturas if a["codigo"] == codigo), "Desconocido")
            resultados.append({"codigo": codigo, "nombre": nombre_asig, "porcentaje_reprobacion": porcentaje})
        resultados.sort(key=lambda x: x["porcentaje_reprobacion"], reverse=True)
        return resultados
    except Exception as e:
        reportar_error(f"Error en asignaturas reprobadas para {programa}: {e}")
        return []

def comparar_periodos(programa, periodo1, periodo2, calificaciones=calificaciones, estudiantes=estudiantes):
    """
    Compara el promedio de un programa entre dos periodos.
    
    Parámetros:
        programa: Nombre del programa.
        periodo1, periodo2: Periodos a comparar.
    Retorna:
        Diccionario con promedios.
    """
    try:
        prom1 = promedio_programa(programa, periodo1, calificaciones, estudiantes)
        prom2 = promedio_programa(programa, periodo2, calificaciones, estudiantes)
        return {"periodo1": prom1, "periodo2": prom2}
    except Exception as e:
        reportar_error(f"Error al comparar periodos para {programa}: {e}")
        return {}

# Funciones de análisis comparativo y reportes
def generar_estadisticas(grades_list):
    """
    Genera estadísticas (promedio, mínimo, máximo) de una lista de notas.
    
    Parámetros:
        grades_list: Lista de números.
    Retorna:
        Diccionario con 'promedio', 'minimo' y 'maximo'.
    """
    try:
        if not grades_list:
            raise ValueError("Lista vacía.")
        promedio = sum(grades_list) / len(grades_list)
        return {"promedio": promedio, "minimo": min(grades_list), "maximo": max(grades_list)}
    except Exception as e:
        reportar_error(f"Error al generar estadísticas: {e}")
        return {}

def identificar_top_estudiantes(n=5, periodo=None, calificaciones=calificaciones, estudiantes=estudiantes):
    """
    Identifica los top n estudiantes según su promedio.
    
    Parámetros:
        n: Número de estudiantes (por defecto 5).
        periodo: (Opcional) Filtrado por periodo.
    Retorna:
        Lista de estudiantes con su promedio.
    """
    try:
        lista_promedios = []
        for est in estudiantes:
            prom = calcular_promedio_estudiante(est["codigo"], periodo, calificaciones)
            if prom is not None:
                lista_promedios.append({"codigo": est["codigo"], "nombre": est["nombre"], "promedio": prom})
        lista_promedios.sort(key=lambda x: x["promedio"], reverse=True)
        return lista_promedios[:n]
    except Exception as e:
        reportar_error(f"Error al identificar top estudiantes: {e}")
        return []

# Función para reportar errores de forma formateada
def reportar_error(mensaje):
    """
    Imprime un mensaje de error formateado.
    """
    print(f"*** ERROR: {mensaje} ***")


# MENUS
# =============================================================================
# lo ideal seria separar estos menus en archivos ui por ejemplo

# Menú para gestión de Estudiantes
def menu_estudiantes():
    while True:
        clear_screen()
        print("=== Menú Estudiantes ===")
        print("1. Registrar nuevo estudiante")
        print("2. Calcular promedio de un estudiante")
        print("3. Ver historial académico")
        print("4. Analizar desempeño individual")
        print("5. Volver al menú principal")
        try:
            op = int(input("Seleccione una opción: "))
        except Exception:
            print("Opción inválida. Intente de nuevo.")
            input("Presione Enter para continuar...")
            continue

        if op == 1:
            clear_screen()
            print("Registrar nuevo estudiante")
            codigo = input("Código: ")
            nombre = input("Nombre: ")
            # Para el programa, se pide el código y se busca en el diccionario
            prog_code = input("Código del programa (ej. IS, MD, AE, PSI, DER): ").upper()
            programa = programas.get(prog_code)
            if not programa:
                print("Código de programa inválido.")
                input("Presione Enter para continuar...")
                continue
            try:
                semestre = int(input("Semestre: "))
            except Exception:
                print("Semestre inválido.")
                input("Presione Enter para continuar...")
                continue
            nuevo_est = {"codigo": codigo, "nombre": nombre, "programa": programa, "semestre": semestre}
            registrar_entidad(nuevo_est, estudiantes)
            print("Estudiante registrado exitosamente.")
            input("Presione Enter para continuar...")
        elif op == 2:
            clear_screen()
            print("Calcular promedio de un estudiante")
            codigo = input("Ingrese el código del estudiante: ")
            periodo = input("Ingrese el periodo (dejar vacío para global): ")
            periodo = periodo if periodo.strip() != "" else None
            prom = calcular_promedio_estudiante(codigo, periodo)
            if prom is not None:
                print(f"El promedio del estudiante {codigo} es: {prom:.2f}")
            input("Presione Enter para continuar...")
        elif op == 3:
            clear_screen()
            print("Historial académico del estudiante")
            codigo = input("Ingrese el código del estudiante: ")
            historial = obtener_historial_academico(codigo)
            if historial:
                for reg in historial:
                    print(f"Asignatura: {reg['codigo_asignatura']}, Nota: {reg['nota']}, Periodo: {reg['periodo']}")
            input("Presione Enter para continuar...")
        elif op == 4:
            clear_screen()
            print("Analizar desempeño individual")
            codigo = input("Ingrese el código del estudiante: ")
            desempeño = analizar_desempeno_estudiante(codigo)
            if desempeño:
                print(f"Mejor desempeño: Asignatura {desempeño['mejor']['codigo_asignatura']} con nota {desempeño['mejor']['nota']}")
                print(f"Peor desempeño: Asignatura {desempeño['peor']['codigo_asignatura']} con nota {desempeño['peor']['nota']}")
            input("Presione Enter para continuar...")
        elif op == 5:
            break
        else:
            print("Opción inválida.")
            input("Presione Enter para continuar...")

# Menú para gestión de Programas Académicos
def menu_programas():
    while True:
        clear_screen()
        print("=== Menú Programas Académicos ===")
        print("1. Calcular promedio de un programa")
        print("2. Asignaturas con mayor reprobación")
        print("3. Comparar periodos")
        print("4. Volver al menú principal")
        try:
            op = int(input("Seleccione una opción: "))
        except Exception:
            print("Opción inválida. Intente de nuevo.")
            input("Presione Enter para continuar...")
            continue

        if op == 4:
            break

        # Para buscar, se pide el código del programa
        prog_code = input("Ingrese el código del programa (ej. IS, MD, AE, PSI, DER): ").upper()
        programa = programas.get(prog_code)
        if not programa:
            print("Código de programa inválido.")
            input("Presione Enter para continuar...")
            continue

        if op == 1:
            clear_screen()
            print("Promedio de un programa")
            periodo = input("Ingrese el periodo (ej. '2023-1'): ")
            prom = promedio_programa(programa, periodo)
            if prom is not None:
                print(f"El promedio del programa {programa} en {periodo} es: {prom:.2f}")
            input("Presione Enter para continuar...")
        elif op == 2:
            clear_screen()
            print("Asignaturas con mayor reprobación")
            periodo = input("Ingrese el periodo (ej. '2023-1'): ")
            asignaturas_rep = asignaturas_mayor_reprobacion(programa, periodo)
            if asignaturas_rep:
                for asig in asignaturas_rep:
                    print(f"{asig['codigo']} - {asig['nombre']}: {asig['porcentaje_reprobacion']*100:.1f}% reprobación")
            input("Presione Enter para continuar...")
        elif op == 3:
            clear_screen()
            print("Comparar periodos para un programa")
            periodo1 = input("Ingrese el primer periodo: ")
            periodo2 = input("Ingrese el segundo periodo: ")
            comp = comparar_periodos(programa, periodo1, periodo2)
            if comp:
                print(f"Promedio en {periodo1}: {comp['periodo1']:.2f}")
                print(f"Promedio en {periodo2}: {comp['periodo2']:.2f}")
            input("Presione Enter para continuar...")
        else:
            print("Opción inválida.")
            input("Presione Enter para continuar...")

# Menú para gestión de Calificaciones
def menu_calificaciones():
    while True:
        clear_screen()
        print("=== Menú Calificaciones ===")
        print("1. Registrar calificación")
        print("2. Volver al menú principal")
        try:
            op = int(input("Seleccione una opción: "))
        except Exception:
            print("Opción inválida.")
            input("Presione Enter para continuar...")
            continue

        if op == 1:
            clear_screen()
            print("Registrar calificación")
            codigo_est = input("Ingrese el código del estudiante: ")
            codigo_asig = input("Ingrese el código de la asignatura (ej. IS2045, CB1015, etc.): ").upper()
            try:
                nota = float(input("Ingrese la nota (0 a 5): "))
            except Exception:
                print("Nota inválida.")
                input("Presione Enter para continuar...")
                continue
            periodo = input("Ingrese el periodo (ej. '2023-1'): ")
            nueva_cal = {"codigo_estudiante": codigo_est, "codigo_asignatura": codigo_asig, "nota": nota, "periodo": periodo}
            registrar_entidad(nueva_cal, calificaciones)
            print("Calificación registrada exitosamente.")
            input("Presione Enter para continuar...")
        elif op == 2:
            break
        else:
            print("Opción inválida.")
            input("Presione Enter para continuar...")

# Menú para reportes generales
def menu_reportes():
    while True:
        clear_screen()
        print("=== Menú Reportes ===")
        print("1. Generar estadísticas generales de calificaciones")
        print("2. Identificar top estudiantes")
        print("3. Volver al menú principal")
        try:
            op = int(input("Seleccione una opción: "))
        except Exception:
            print("Opción inválida.")
            input("Presione Enter para continuar...")
            continue
        
        if op == 1:
            clear_screen()
            print("Estadísticas generales de calificaciones")
            todas_notas = [reg["nota"] for reg in calificaciones]
            stats = generar_estadisticas(todas_notas)
            if stats:
                print(f"Promedio: {stats['promedio']:.2f}")
                print(f"Mínimo: {stats['minimo']:.2f}")
                print(f"Máximo: {stats['maximo']:.2f}")
            input("Presione Enter para continuar...")
        elif op == 2:
            clear_screen()
            print("Top estudiantes")
            periodo = input("Ingrese el periodo (dejar vacío para global): ")
            periodo = periodo if periodo.strip() != "" else None
            top_est = identificar_top_estudiantes(5, periodo)
            for est in top_est:
                print(f"{est['codigo']} - {est['nombre']}: Promedio {est['promedio']:.2f}")
            input("Presione Enter para continuar...")
        elif op == 3:
            break
        else:
            print("Opción inválida.")
            input("Presione Enter para continuar...")

# Menú principal de la aplicación
def main_menu():
    while True:
        clear_screen()
        print("=== Academic Performance Analyzer ===")
        print("1. Gestión de Estudiantes")
        print("2. Gestión de Programas Académicos")
        print("3. Gestión de Calificaciones")
        print("4. Reportes")
        print("5. Salir")
        try:
            op = int(input("Seleccione una opción: "))
        except Exception:
            print("Opción inválida. Intente de nuevo.")
            input("Presione Enter para continuar...")
            continue

        if op == 1:
            menu_estudiantes()
        elif op == 2:
            menu_programas()
        elif op == 3:
            menu_calificaciones()
        elif op == 4:
            menu_reportes()
        elif op == 5:
            print("Saliendo del sistema...")
            sys.exit(0)
        else:
            print("Opción inválida.")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    main_menu()
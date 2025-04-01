"""
Academic Performance Analyzer
Proyecto para la Universidad de Santander (UDES)
Sistema para analizar el rendimiento académico de estudiantes, 
programas y facultades con persistencia en JSON.
"""

import os
import sys
import json
from typing import Any, Callable, Dict, List, Optional, Union

DATA_FILE = "data.json"


def load_data() -> Dict[str, Any]:
    """
    Carga los datos desde un archivo JSON.
    Si el archivo no existe, se crean datos por defecto.
    """
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            return data
        except Exception as e:
            print(f"*** ERROR: No se pudo cargar el archivo de datos: {e} ***")
    # Datos por defecto si no existe archivo o error al cargar
    data = {
        "estudiantes": [
            {"codigo": "2020115001", "nombre": "Carolina Martínez Ruiz",
             "programa": "Ingeniería de Software", "semestre": 7},
            {"codigo": "2021220034", "nombre": "Andrés Felipe Gómez",
             "programa": "Medicina", "semestre": 5},
            {"codigo": "2022118092", "nombre": "Valentina Sánchez Torres",
             "programa": "Ingeniería de Software", "semestre": 3},
            {"codigo": "2019456123", "nombre": "Juan Carlos Ramírez",
             "programa": "Administración de Empresas", "semestre": 8},
            {"codigo": "2023110056", "nombre": "Daniela Hernández Díaz",
             "programa": "Psicología", "semestre": 2},
            {"codigo": "2020119045", "nombre": "Miguel Ángel Quintero",
             "programa": "Ingeniería de Software", "semestre": 6},
            {"codigo": "2021345087", "nombre": "Laura Sofía Parra",
             "programa": "Derecho", "semestre": 5},
            {"codigo": "2020112089", "nombre": "Santiago Ortiz Méndez",
             "programa": "Ingeniería de Software", "semestre": 7},
            {"codigo": "2022230078", "nombre": "Isabella Castro Rojas",
             "programa": "Enfermería", "semestre": 3},
            {"codigo": "2021116032", "nombre": "David Alejandro Moreno",
             "programa": "Ingeniería de Software", "semestre": 5}
        ],
        "asignaturas": [
            {"codigo": "IS2045", "nombre": "Fundamentos de Programación",
             "creditos": 4, "programa": "Ingeniería de Software"},
            {"codigo": "IS3067", "nombre": "Gestores de Bases de Datos",
             "creditos": 3, "programa": "Ingeniería de Software"},
            {"codigo": "IS4023", "nombre": "Diseño de Software I",
             "creditos": 3, "programa": "Ingeniería de Software"},
            {"codigo": "CB1015", "nombre": "Cálculo Diferencial",
             "creditos": 4, "programa": "Ciencias Básicas"},
            {"codigo": "CB1024", "nombre": "Física Mecánica",
             "creditos": 4, "programa": "Ciencias Básicas"}
        ],
        "calificaciones": [
            {"codigo_estudiante": "2020115001", "codigo_asignatura": "IS3067",
             "nota": 4.2, "periodo": "2023-1"},
            {"codigo_estudiante": "2020115001", "codigo_asignatura": "IS4023",
             "nota": 3.8, "periodo": "2023-1"},
            {"codigo_estudiante": "2020119045", "codigo_asignatura": "IS3067",
             "nota": 3.5, "periodo": "2023-1"},
            {"codigo_estudiante": "2020119045", "codigo_asignatura": "IS4023",
             "nota": 4.0, "periodo": "2023-1"},
            {"codigo_estudiante": "2020112089", "codigo_asignatura": "IS3067",
             "nota": 4.5, "periodo": "2023-1"},
            {"codigo_estudiante": "2020112089", "codigo_asignatura": "IS4023",
             "nota": 4.3, "periodo": "2023-1"},
            {"codigo_estudiante": "2022118092", "codigo_asignatura": "CB1015",
             "nota": 3.2, "periodo": "2023-1"},
            {"codigo_estudiante": "2022118092", "codigo_asignatura": "CB1024",
             "nota": 2.8, "periodo": "2023-1"},
            {"codigo_estudiante": "2021116032", "codigo_asignatura": "CB1015",
             "nota": 3.6, "periodo": "2023-1"},
            {"codigo_estudiante": "2021116032", "codigo_asignatura": "CB1024",
             "nota": 3.4, "periodo": "2023-1"},
            {"codigo_estudiante": "2020115001", "codigo_asignatura": "IS2045",
             "nota": 4.7, "periodo": "2023-2"},
            {"codigo_estudiante": "2020119045", "codigo_asignatura": "IS2045",
             "nota": 3.9, "periodo": "2023-2"},
            {"codigo_estudiante": "2022118092", "codigo_asignatura": "IS2045",
             "nota": 2.9, "periodo": "2023-2"},
            {"codigo_estudiante": "2020112089", "codigo_asignatura": "IS2045",
             "nota": 4.2, "periodo": "2023-2"},
            {"codigo_estudiante": "2021116032", "codigo_asignatura": "IS2045",
             "nota": 3.8, "periodo": "2023-2"},
            {"codigo_estudiante": "2021116032", "codigo_asignatura": "IS3067",
             "nota": 4.1, "periodo": "2023-2"},
            {"codigo_estudiante": "2022118092", "codigo_asignatura": "IS3067",
             "nota": 3.0, "periodo": "2023-2"},
            {"codigo_estudiante": "2020115001", "codigo_asignatura": "CB1015",
             "nota": 4.3, "periodo": "2023-2"},
            {"codigo_estudiante": "2020119045", "codigo_asignatura": "CB1015",
             "nota": 3.7, "periodo": "2023-2"},
            {"codigo_estudiante": "2020112089", "codigo_asignatura": "CB1015",
             "nota": 4.8, "periodo": "2023-2"},
            {"codigo_estudiante": "2021116032", "codigo_asignatura": "IS4023",
             "nota": 3.2, "periodo": "2024-1"},
            {"codigo_estudiante": "2022118092", "codigo_asignatura": "IS4023",
             "nota": 2.7, "periodo": "2024-1"},
            {"codigo_estudiante": "2020115001", "codigo_asignatura": "CB1024",
             "nota": 3.9, "periodo": "2024-1"},
            {"codigo_estudiante": "2020119045", "codigo_asignatura": "CB1024",
             "nota": 3.5, "periodo": "2024-1"},
            {"codigo_estudiante": "2020112089", "codigo_asignatura": "CB1024",
             "nota": 4.6, "periodo": "2024-1"},
            {"codigo_estudiante": "2021116032", "codigo_asignatura": "CB1024",
             "nota": 3.3, "periodo": "2024-1"},
            {"codigo_estudiante": "2022118092", "codigo_asignatura": "CB1015",
             "nota": 3.4, "periodo": "2024-1"},
            {"codigo_estudiante": "2020115001", "codigo_asignatura": "IS4023",
             "nota": 4.5, "periodo": "2024-1"},
            {"codigo_estudiante": "2020119045", "codigo_asignatura": "IS4023",
             "nota": 4.2, "periodo": "2024-1"},
            {"codigo_estudiante": "2020112089", "codigo_asignatura": "IS3067",
             "nota": 4.7, "periodo": "2024-1"}
        ],
        "facultades": {
            "Facultad de Ingenierías": [
                "Ingeniería de Software",
                "Ingeniería Civil",
                "Ingeniería Ambiental"
            ],
            "Facultad de Ciencias de la Salud": [
                "Medicina",
                "Enfermería",
                "Psicología"
            ],
            "Facultad de Ciencias Económicas, Administrativas y Contables": [
                "Administración de Empresas",
                "Contaduría Pública"
            ],
            "Facultad de Ciencias Sociales, Políticas y Jurídicas": [
                "Derecho",
                "Comunicación Social"
            ]
        },
        "programas": {
            "IS": "Ingeniería de Software",
            "MD": "Medicina",
            "AE": "Administración de Empresas",
            "PSI": "Psicología",
            "DER": "Derecho"
        }
    }
    return data


def save_data(data: Dict[str, Any]) -> None:
    """
    Guarda los datos en un archivo JSON.
    """
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"*** ERROR: No se pudo guardar el archivo de datos: {e} ***")


def clear_screen() -> None:
    """
    Limpia la pantalla de la terminal según el sistema operativo.
    """
    os.system("cls" if os.name == "nt" else "clear")


def reportar_error(mensaje: str) -> None:
    """
    Imprime un mensaje de error formateado.
    """
    print(f"*** ERROR: {mensaje} ***")


def registrar_entidad(entidad: Dict[str, Any], lista_destino: List[Dict[str, Any]]) -> None:
    """
    Registra una entidad en la lista destino.

    Args:
        entidad: Diccionario con la información de la entidad.
        lista_destino: Lista donde se agregará la entidad.
    """
    try:
        lista_destino.append(entidad)
    except Exception as e:
        reportar_error(f"Error al registrar entidad: {e}")


def filtrar_calificaciones(
    lista: List[Dict[str, Any]], filtro_func: Callable[[Dict[str, Any]], bool]
) -> List[Dict[str, Any]]:
    """
    Filtra una lista de calificaciones usando una función de filtro.

    Args:
        lista: Lista de calificaciones.
        filtro_func: Función que devuelve True/False.

    Returns:
        Lista filtrada.
    """
    return [item for item in lista if filtro_func(item)]


def calcular_promedio_estudiante(
    codigo_estudiante: str,
    periodo: Optional[str] = None,
    calificaciones: Optional[List[Dict[str, Any]]] = None
) -> Optional[float]:
    """
    Calcula el promedio de un estudiante.

    Args:
        codigo_estudiante: Código del estudiante.
        periodo: (Opcional) Periodo académico (ej. "2023-1").
        calificaciones: Lista de calificaciones. Si no se pasa, se usa la data cargada.

    Returns:
        Promedio o None.
    """
    if calificaciones is None:
        calificaciones = data["calificaciones"]
    try:
        notas = [
            reg["nota"]
            for reg in calificaciones
            if reg["codigo_estudiante"] == codigo_estudiante and
            (reg["periodo"] == periodo if periodo else True)
        ]
        if not notas:
            return None
        return sum(notas) / len(notas)
    except Exception as e:
        reportar_error(f"Error al calcular promedio para {codigo_estudiante}: {e}")
        return None


def obtener_historial_academico(
    codigo_estudiante: str,
    calificaciones: Optional[List[Dict[str, Any]]] = None
) -> List[Dict[str, Any]]:
    """
    Obtiene el historial académico de un estudiante.

    Args:
        codigo_estudiante: Código del estudiante.
        calificaciones: Lista de calificaciones.

    Returns:
        Lista de registros.
    """
    if calificaciones is None:
        calificaciones = data["calificaciones"]
    try:
        historial = [
            reg for reg in calificaciones if reg["codigo_estudiante"] == codigo_estudiante
        ]
        if not historial:
            raise ValueError("No se encontró historial para el estudiante.")
        return historial
    except Exception as e:
        reportar_error(f"Error al obtener historial para {codigo_estudiante}: {e}")
        return []


def analizar_desempeno_estudiante(
    codigo_estudiante: str,
    calificaciones: Optional[List[Dict[str, Any]]] = None
) -> Dict[str, Dict[str, Any]]:
    """
    Identifica la asignatura con mejor y peor desempeño de un estudiante.

    Args:
        codigo_estudiante: Código del estudiante.
        calificaciones: Lista de calificaciones.

    Returns:
        Diccionario con 'mejor' y 'peor' desempeño.
    """
    if calificaciones is None:
        calificaciones = data["calificaciones"]
    try:
        registros = [
            reg for reg in calificaciones if reg["codigo_estudiante"] == codigo_estudiante
        ]
        if not registros:
            raise ValueError("No hay registros para el estudiante.")
        mejor = max(registros, key=lambda x: x["nota"])
        peor = min(registros, key=lambda x: x["nota"])
        return {"mejor": mejor, "peor": peor}
    except Exception as e:
        reportar_error(f"Error en desempeño para {codigo_estudiante}: {e}")
        return {}


def promedio_programa(
    programa: str,
    periodo: str,
    calificaciones: Optional[List[Dict[str, Any]]] = None,
    estudiantes: Optional[List[Dict[str, Any]]] = None
) -> Optional[float]:
    """
    Calcula el promedio general de un programa en un periodo.

    Args:
        programa: Nombre del programa.
        periodo: Periodo académico.
        calificaciones: Lista de calificaciones.
        estudiantes: Lista de estudiantes.

    Returns:
        Promedio o None.
    """
    if calificaciones is None:
        calificaciones = data["calificaciones"]
    if estudiantes is None:
        estudiantes = data["estudiantes"]
    try:
        codigos_prog = [
            est["codigo"] for est in estudiantes if est["programa"] == programa
        ]
        notas = [
            reg["nota"]
            for reg in calificaciones
            if reg["codigo_estudiante"] in codigos_prog and reg["periodo"] == periodo
        ]
        if not notas:
            raise ValueError("No se encontraron calificaciones para el programa en ese periodo.")
        return sum(notas) / len(notas)
    except Exception as e:
        reportar_error(f"Error al calcular promedio para el programa {programa} en {periodo}: {e}")
        return None


def asignaturas_mayor_reprobacion(
    programa: str,
    periodo: str,
    calificaciones: Optional[List[Dict[str, Any]]] = None,
    asignaturas: Optional[List[Dict[str, Any]]] = None,
    estudiantes: Optional[List[Dict[str, Any]]] = None
) -> List[Dict[str, Union[str, float]]]:
    """
    Identifica asignaturas con mayor índice de reprobación en un programa para un periodo.

    Args:
        programa: Nombre del programa.
        periodo: Periodo académico.
        calificaciones: Lista de calificaciones.
        asignaturas: Lista de asignaturas.
        estudiantes: Lista de estudiantes.

    Returns:
        Lista de asignaturas con porcentaje de reprobación.
    """
    if calificaciones is None:
        calificaciones = data["calificaciones"]
    if asignaturas is None:
        asignaturas = data["asignaturas"]
    if estudiantes is None:
        estudiantes = data["estudiantes"]
    try:
        codigos_prog = [
            est["codigo"] for est in estudiantes if est["programa"] == programa
        ]
        regs = [
            reg for reg in calificaciones
            if reg["codigo_estudiante"] in codigos_prog and reg["periodo"] == periodo
        ]
        stats: Dict[str, Dict[str, int]] = {}
        for reg in regs:
            codigo_asig = reg["codigo_asignatura"]
            stats.setdefault(codigo_asig, {"total": 0, "reprobados": 0})
            stats[codigo_asig]["total"] += 1
            if reg["nota"] < 3.0:
                stats[codigo_asig]["reprobados"] += 1
        resultados = []
        for codigo, datos in stats.items():
            porcentaje = datos["reprobados"] / datos["total"]
            nombre_asig = next(
                (a["nombre"] for a in asignaturas if a["codigo"] == codigo), "Desconocido"
            )
            resultados.append({
                "codigo": codigo,
                "nombre": nombre_asig,
                "porcentaje_reprobacion": porcentaje
            })
        resultados.sort(key=lambda x: x["porcentaje_reprobacion"], reverse=True)
        return resultados
    except Exception as e:
        reportar_error(f"Error en asignaturas reprobadas para {programa}: {e}")
        return []


def comparar_periodos(
    programa: str,
    periodo1: str,
    periodo2: str,
    calificaciones: Optional[List[Dict[str, Any]]] = None,
    estudiantes: Optional[List[Dict[str, Any]]] = None
) -> Dict[str, Optional[float]]:
    """
    Compara el promedio de un programa entre dos periodos.

    Args:
        programa: Nombre del programa.
        periodo1: Primer periodo.
        periodo2: Segundo periodo.
        calificaciones: Lista de calificaciones.
        estudiantes: Lista de estudiantes.

    Returns:
        Diccionario con promedios.
    """
    if calificaciones is None:
        calificaciones = data["calificaciones"]
    if estudiantes is None:
        estudiantes = data["estudiantes"]
    try:
        prom1 = promedio_programa(programa, periodo1, calificaciones, estudiantes)
        prom2 = promedio_programa(programa, periodo2, calificaciones, estudiantes)
        return {"periodo1": prom1, "periodo2": prom2}
    except Exception as e:
        reportar_error(f"Error al comparar periodos para {programa}: {e}")
        return {}


def generar_estadisticas(grades_list: List[float]) -> Dict[str, float]:
    """
    Genera estadísticas (promedio, mínimo, máximo) de una lista de notas.

    Args:
        grades_list: Lista de números.

    Returns:
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


def identificar_top_estudiantes(
    n: int = 5,
    periodo: Optional[str] = None,
    calificaciones: Optional[List[Dict[str, Any]]] = None,
    estudiantes: Optional[List[Dict[str, Any]]] = None
) -> List[Dict[str, Union[str, float]]]:
    """
    Identifica los top n estudiantes según su promedio.

    Args:
        n: Número de estudiantes (por defecto 5).
        periodo: (Opcional) Filtrado por periodo.
        calificaciones: Lista de calificaciones.
        estudiantes: Lista de estudiantes.

    Returns:
        Lista de estudiantes con su promedio.
    """
    if calificaciones is None:
        calificaciones = data["calificaciones"]
    if estudiantes is None:
        estudiantes = data["estudiantes"]
    try:
        lista_promedios = []
        for est in estudiantes:
            prom = calcular_promedio_estudiante(est["codigo"], periodo, calificaciones)
            if prom is not None:
                lista_promedios.append({
                    "codigo": est["codigo"],
                    "nombre": est["nombre"],
                    "promedio": prom
                })
        lista_promedios.sort(key=lambda x: x["promedio"], reverse=True)
        return lista_promedios[:n]
    except Exception as e:
        reportar_error(f"Error al identificar top estudiantes: {e}")
        return []


def validar_nota(nota: float) -> bool:
    """
    Valida que la nota esté en el rango [0, 5].

    Args:
        nota: Nota a validar.

    Returns:
        True si es válida, False en caso contrario.
    """
    return 0.0 <= nota <= 5.0


def validar_codigo_unico(
    codigo: str, estudiantes: List[Dict[str, Any]]
) -> bool:
    """
    Verifica que el código de estudiante no exista ya en la lista.

    Args:
        codigo: Código a validar.
        estudiantes: Lista de estudiantes.

    Returns:
        True si es único, False de lo contrario.
    """
    return not any(est["codigo"] == codigo for est in estudiantes)


def existe_asignatura(codigo_asig: str, asignaturas: List[Dict[str, Any]]) -> bool:
    """
    Valida que la asignatura exista en la lista de asignaturas.

    Args:
        codigo_asig: Código de la asignatura.
        asignaturas: Lista de asignaturas.

    Returns:
        True si existe, False de lo contrario.
    """
    return any(a["codigo"] == codigo_asig for a in asignaturas)


def existe_estudiante(codigo_est: str, estudiantes: List[Dict[str, Any]]) -> bool:
    """
    Valida que el estudiante exista en la lista de estudiantes.

    Args:
        codigo_est: Código del estudiante.
        estudiantes: Lista de estudiantes.

    Returns:
        True si existe, False de lo contrario.
    """
    return any(est["codigo"] == codigo_est for est in estudiantes)


# ----------------- Menús ----------------- #


def menu_estudiantes() -> None:
    """
    Menú para la gestión de estudiantes.
    """
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
            codigo = input("Código: ").strip()
            if not validar_codigo_unico(codigo, data["estudiantes"]):
                print("Error: Código duplicado.")
                input("Presione Enter para continuar...")
                continue
            nombre = input("Nombre: ").strip()
            prog_code = input("Código del programa (ej. IS, MD, AE, PSI, DER): ").strip().upper()
            programa = data["programas"].get(prog_code)
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
            nuevo_est = {
                "codigo": codigo,
                "nombre": nombre,
                "programa": programa,
                "semestre": semestre
            }
            registrar_entidad(nuevo_est, data["estudiantes"])
            save_data(data)
            print("Estudiante registrado exitosamente.")
            input("Presione Enter para continuar...")

        elif op == 2:
            clear_screen()
            print("Calcular promedio de un estudiante")
            codigo = input("Ingrese el código del estudiante: ").strip()
            periodo = input("Ingrese el periodo (dejar vacío para global): ").strip()
            periodo = periodo if periodo else None
            prom = calcular_promedio_estudiante(codigo, periodo)
            if prom is not None:
                print(f"El promedio del estudiante {codigo} es: {prom:.2f}")
            else:
                print("No se encontró promedio para el estudiante.")
            input("Presione Enter para continuar...")

        elif op == 3:
            clear_screen()
            print("Historial académico del estudiante")
            codigo = input("Ingrese el código del estudiante: ").strip()
            historial = obtener_historial_academico(codigo)
            if historial:
                for reg in historial:
                    print(f"Asignatura: {reg['codigo_asignatura']}, Nota: {reg['nota']}, Periodo: {reg['periodo']}")
            else:
                print("No se encontró historial para el estudiante.")
            input("Presione Enter para continuar...")

        elif op == 4:
            clear_screen()
            print("Analizar desempeño individual")
            codigo = input("Ingrese el código del estudiante: ").strip()
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


def menu_programas() -> None:
    """
    Menú para la gestión de programas académicos.
    """
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

        prog_code = input("Ingrese el código del programa (ej. IS, MD, AE, PSI, DER): ").strip().upper()
        programa = data["programas"].get(prog_code)
        if not programa:
            print("Código de programa inválido.")
            input("Presione Enter para continuar...")
            continue

        if op == 1:
            clear_screen()
            print("Promedio de un programa")
            periodo = input("Ingrese el periodo (ej. '2023-1'): ").strip()
            prom = promedio_programa(programa, periodo)
            if prom is not None:
                print(f"El promedio del programa {programa} en {periodo} es: {prom:.2f}")
            else:
                print("No se pudo calcular el promedio.")
            input("Presione Enter para continuar...")

        elif op == 2:
            clear_screen()
            print("Asignaturas con mayor reprobación")
            periodo = input("Ingrese el periodo (ej. '2023-1'): ").strip()
            asignaturas_rep = asignaturas_mayor_reprobacion(programa, periodo)
            if asignaturas_rep:
                for asig in asignaturas_rep:
                    print(f"{asig['codigo']} - {asig['nombre']}: {asig['porcentaje_reprobacion']*100:.1f}% reprobación")
            else:
                print("No se encontraron datos.")
            input("Presione Enter para continuar...")

        elif op == 3:
            clear_screen()
            print("Comparar periodos para un programa")
            periodo1 = input("Ingrese el primer periodo: ").strip()
            periodo2 = input("Ingrese el segundo periodo: ").strip()
            comp = comparar_periodos(programa, periodo1, periodo2)
            if comp:
                prom1 = comp.get("periodo1")
                prom2 = comp.get("periodo2")
                if prom1 is not None:
                    print(f"Promedio en {periodo1}: {prom1:.2f}")
                else:
                    print(f"No hay promedio para {periodo1}.")
                if prom2 is not None:
                    print(f"Promedio en {periodo2}: {prom2:.2f}")
                else:
                    print(f"No hay promedio para {periodo2}.")
            input("Presione Enter para continuar...")

        else:
            print("Opción inválida.")
            input("Presione Enter para continuar...")


def menu_calificaciones() -> None:
    """
    Menú para la gestión de calificaciones.
    """
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
            codigo_est = input("Ingrese el código del estudiante: ").strip()
            if not existe_estudiante(codigo_est, data["estudiantes"]):
                print("Estudiante no registrado.")
                input("Presione Enter para continuar...")
                continue

            codigo_asig = input("Ingrese el código de la asignatura (ej. IS2045, CB1015, etc.): ").strip().upper()
            if not existe_asignatura(codigo_asig, data["asignaturas"]):
                print("Asignatura no existe.")
                input("Presione Enter para continuar...")
                continue

            try:
                nota = float(input("Ingrese la nota (0 a 5): "))
            except Exception:
                print("Nota inválida.")
                input("Presione Enter para continuar...")
                continue

            if not validar_nota(nota):
                print("Nota fuera de rango (debe estar entre 0 y 5).")
                input("Presione Enter para continuar...")
                continue

            periodo = input("Ingrese el periodo (ej. '2023-1'): ").strip()
            nueva_cal = {
                "codigo_estudiante": codigo_est,
                "codigo_asignatura": codigo_asig,
                "nota": nota,
                "periodo": periodo
            }
            registrar_entidad(nueva_cal, data["calificaciones"])
            save_data(data)
            print("Calificación registrada exitosamente.")
            input("Presione Enter para continuar...")

        elif op == 2:
            break
        else:
            print("Opción inválida.")
            input("Presione Enter para continuar...")


def menu_reportes() -> None:
    """
    Menú para reportes generales.
    """
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
            todas_notas = [reg["nota"] for reg in data["calificaciones"]]
            stats = generar_estadisticas(todas_notas)
            if stats:
                print(f"Promedio: {stats['promedio']:.2f}")
                print(f"Mínimo: {stats['minimo']:.2f}")
                print(f"Máximo: {stats['maximo']:.2f}")
            input("Presione Enter para continuar...")

        elif op == 2:
            clear_screen()
            print("Top estudiantes")
            periodo = input("Ingrese el periodo (dejar vacío para global): ").strip()
            periodo = periodo if periodo else None
            top_est = identificar_top_estudiantes(5, periodo)
            if top_est:
                for est in top_est:
                    print(f"{est['codigo']} - {est['nombre']}: Promedio {est['promedio']:.2f}")
            else:
                print("No se encontraron estudiantes.")
            input("Presione Enter para continuar...")

        elif op == 3:
            break
        else:
            print("Opción inválida.")
            input("Presione Enter para continuar...")


def main_menu() -> None:
    """
    Menú principal de la aplicación.
    """
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
    data = load_data()
    main_menu()

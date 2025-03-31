# Datos de ejemplo para el Sistema de Análisis de Rendimiento Académico UDES
# ----------------------------------------------------------------------

# 1. Información de 10 estudiantes (código, nombre, programa, semestre)
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

# 2. Datos de 5 asignaturas (Ingeniería de Software y Ciencias Básicas)
asignaturas = [
    {"codigo": "IS2045", "nombre": "Fundamentos de Programación", "creditos": 4, "programa": "Ingeniería de Software"},
    {"codigo": "IS3067", "nombre": "Gestores de Bases de Datos", "creditos": 3, "programa": "Ingeniería de Software"},
    {"codigo": "IS4023", "nombre": "Diseño de Software I", "creditos": 3, "programa": "Ingeniería de Software"},
    {"codigo": "CB1015", "nombre": "Cálculo Diferencial", "creditos": 4, "programa": "Ciencias Básicas"},
    {"codigo": "CB1024", "nombre": "Física Mecánica", "creditos": 4, "programa": "Ciencias Básicas"}
]

# 3. Registro de 30 calificaciones (estudiante, asignatura, nota, periodo)
# Notas en escala de 0 a 5, donde 3.0 es la nota mínima aprobatoria
calificaciones = [
    # Periodo 2023-1
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
    
    # Periodo 2023-2
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
    
    # Periodo 2024-1
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

# Facultades y sus programas (información adicional útil)
facultades = {
    "Facultad de Ingenierías": ["Ingeniería de Software", "Ingeniería Civil", "Ingeniería Ambiental"],
    "Facultad de Ciencias de la Salud": ["Medicina", "Enfermería", "Psicología"],
    "Facultad de Ciencias Económicas, Administrativas y Contables": ["Administración de Empresas", "Contaduría Pública"],
    "Facultad de Ciencias Sociales, Políticas y Jurídicas": ["Derecho", "Comunicación Social"]
}

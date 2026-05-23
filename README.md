# 📋 Gestor de Tareas Pendientes — To-Do List CLI

Aplicación de consola desarrollada en **Python** para gestionar una lista de tareas pendientes. Permite agregar tareas, marcarlas como completadas, visualizarlas y contar las pendientes usando un **algoritmo recursivo**.

Desarrollado como proyecto académico aplicando principios de **programación modular**, **funciones con y sin retorno**, **recursividad** y **buenas prácticas de documentación en Python (PEP 257)**.

---

## 🚀 Demo rápido

```
=======================================================
        GESTOR DE TAREAS PENDIENTES  v1.0
=======================================================
  1. Ver lista de tareas
  2. Agregar nueva tarea
  3. Marcar tarea como completada
  4. Mostrar total de tareas pendientes
  5. Salir
=======================================================
  Seleccione una opción (1-5):
```

---

## 📁 Estructura del proyecto

```
mi_gestor_tareas/
│
├── mi_gestor_tareas.py   # Script principal — lógica completa del programa
└── README.md             # Documentación del proyecto
```

---

## ⚙️ Requisitos

- Python **3.6** o superior
- No requiere librerías externas (solo módulo `os` de la biblioteca estándar)

Verificar versión instalada:

```bash
python3 --version
```

---

## ▶️ Instalación y ejecución

**1. Clonar el repositorio**

```bash
git clone https://github.com/ocampogaviria1997-tech/mi_gestor_tareas.git
cd mi_gestor_tareas
```

**2. Ejecutar el script**

```bash
python3 mi_gestor_tareas.py
```

> En Windows puedes usar `python mi_gestor_tareas.py`

---

## 🧩 Módulos y funciones

El programa aplica el principio de **responsabilidad única**: cada función tiene un rol claro e independiente.

| Función | Parámetros | Retorno | Descripción |
|---|---|---|---|
| `obtener_tareas()` | Ninguno | `list` | Inicializa y retorna la lista de tareas de ejemplo |
| `mostrar_tareas(lista_tareas)` | `list` | `None` | Muestra las tareas numeradas con su estado `[X]` / `[ ]` |
| `agregar_tarea(lista_tareas, descripcion)` | `list`, `str` | `list` | Agrega una nueva tarea con estado pendiente |
| `marcar_completada(lista_tareas, posicion)` | `list`, `int` | `None` | Marca la tarea en la posición dada como completada |
| `contar_tareas_pendientes(lista_tareas, indice=0)` | `list`, `int` | `int` | Cuenta recursivamente las tareas pendientes |

---

## 🔁 Algoritmo recursivo

La función `contar_tareas_pendientes` resuelve el conteo mediante recursividad:

```python
def contar_tareas_pendientes(lista_tareas, indice=0):
    # Caso base: no quedan tareas por revisar
    if indice == len(lista_tareas):
        return 0

    # Caso recursivo: suma 1 si pendiente, luego avanza
    if not lista_tareas[indice]["completada"]:
        return 1 + contar_tareas_pendientes(lista_tareas, indice + 1)
    else:
        return contar_tareas_pendientes(lista_tareas, indice + 1)
```

**Traza de ejemplo** con 3 tareas `[pendiente, completada, pendiente]`:

```
contar(lista, 0) → 1 + contar(lista, 1)
contar(lista, 1) →     contar(lista, 2)
contar(lista, 2) → 1 + contar(lista, 3)
contar(lista, 3) → 0  ← caso base
────────────────────────────────────────
Resultado: 2 tareas pendientes
```

---

## 🛡️ Manejo de errores

La función `marcar_completada` usa `try-except` para capturar posiciones inválidas sin detener el programa:

```
✘ Error: La posición 99 no existe en la lista.
   Por favor ingrese un número entre 1 y 4.
```

---

## 📐 Buenas prácticas aplicadas

- ✅ **Docstrings (PEP 257)** en cada función — propósito, parámetros y retorno
- ✅ **Nomenclatura descriptiva** — `lista_tareas`, `marcar_completada`, `indice`
- ✅ **Modularización** — separación clara de responsabilidades
- ✅ **Comentarios de línea** explicando la lógica recursiva
- ✅ **Punto de entrada** con `if __name__ == "__main__"`
- ✅ **Manejo de errores** con `try-except` para entradas inválidas

---

## 📚 Referencias

- Trejos Buriticá, O. I. (2023). *Probabilidades y matemáticas aplicadas* — Cap. 11: Funciones (pp. 369-420). Ediciones de la U.
- Trejos Buriticá, O. I. (2023). *Probabilidades y matemáticas aplicadas* — Cap. 12: Consejos y reflexiones sobre programación (pp. 423-440). Ediciones de la U.
- Python Software Foundation. (2024). *PEP 257 – Docstring Conventions*. https://peps.python.org/pep-0257/

---

## 👤 Autor

**Jenifer Andrea Ocampo Gaviria**  
Curso: ALGORITMOS Y PROGRAMACIóN  
Universidad Compensar · 2026

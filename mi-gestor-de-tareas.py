# =============================================================================
# mi_gestor_tareas.py
# Gestor de Tareas Pendientes (To-Do List)
# Autor: Estudiante
# Curso: Programación - Funciones y Modularización
# =============================================================================

# Importamos la librería 'os' para limpiar la pantalla del menú
import os


# -----------------------------------------------------------------------------
# MÓDULO 1: Inicialización de datos
# -----------------------------------------------------------------------------

def obtener_tareas():
    """
    Inicializa y retorna una lista de tareas de ejemplo.

    Esta función no recibe parámetros. Actúa como módulo de inicialización
    del programa, proveyendo datos de muestra para comenzar la sesión.

    Returns:
        list: Una lista de diccionarios, donde cada diccionario representa
              una tarea con las claves:
              - 'descripcion' (str): Texto descriptivo de la tarea.
              - 'completada' (bool): True si está completada, False si está pendiente.
    """
    # Se define una lista inicial con 3 tareas de ejemplo
    lista_inicial = [
        {"descripcion": "Leer el capítulo 11 del libro de Trejos Buriticá", "completada": False},
        {"descripcion": "Entregar el informe técnico de buenas prácticas",   "completada": False},
        {"descripcion": "Revisar los apuntes de funciones recursivas",        "completada": True},
    ]
    return lista_inicial


# -----------------------------------------------------------------------------
# MÓDULO 2: Visualización de tareas
# -----------------------------------------------------------------------------

def mostrar_tareas(lista_tareas):
    """
    Muestra en consola la lista de tareas numeradas con su estado.

    Recorre la lista de tareas e imprime cada una indicando con [X] si está
    completada o con [ ] si está pendiente. No retorna ningún valor.

    Args:
        lista_tareas (list): Lista de diccionarios con las tareas a mostrar.
                             Cada diccionario debe tener las claves
                             'descripcion' y 'completada'.

    Returns:
        None
    """
    print("\n" + "=" * 55)
    print("           LISTA DE TAREAS PENDIENTES")
    print("=" * 55)

    # Verificamos si la lista está vacía antes de iterar
    if not lista_tareas:
        print("  (No hay tareas registradas aún.)")
    else:
        # enumerate() permite obtener el índice y el elemento al mismo tiempo
        for indice, tarea in enumerate(lista_tareas, start=1):
            # Definimos el símbolo según el estado de la tarea
            estado = "[X]" if tarea["completada"] else "[ ]"
            print(f"  {indice}. {estado} {tarea['descripcion']}")

    print("=" * 55 + "\n")


# -----------------------------------------------------------------------------
# MÓDULO 3: Agregar una nueva tarea
# -----------------------------------------------------------------------------

def agregar_tarea(lista_tareas, descripcion):
    """
    Agrega una nueva tarea a la lista con estado pendiente.

    Crea un diccionario con la descripción recibida y el estado 'completada'
    en False, luego lo añade al final de la lista de tareas.

    Args:
        lista_tareas (list): Lista actual de tareas (diccionarios).
        descripcion  (str):  Texto descriptivo de la nueva tarea a agregar.

    Returns:
        list: La misma lista de tareas con la nueva tarea añadida al final.
    """
    # Construimos el diccionario de la nueva tarea
    nueva_tarea = {
        "descripcion": descripcion,
        "completada": False   # Toda tarea nueva inicia como pendiente
    }
    lista_tareas.append(nueva_tarea)
    print(f"\n  ✔ Tarea '{descripcion}' agregada exitosamente.")
    return lista_tareas


# -----------------------------------------------------------------------------
# MÓDULO 4: Marcar una tarea como completada
# -----------------------------------------------------------------------------

def marcar_completada(lista_tareas, posicion):
    """
    Marca como completada la tarea ubicada en la posición indicada.

    Recibe un número de posición (basado en 1), valida que exista en la
    lista y cambia el campo 'completada' a True. Si la posición es inválida,
    maneja el error de forma amigable usando un bloque try-except.

    Args:
        lista_tareas (list): Lista de diccionarios con las tareas.
        posicion     (int):  Número de posición de la tarea (empieza en 1).

    Returns:
        None  (modifica la lista original directamente).
    """
    try:
        # Convertimos la posición basada en 1 a índice basado en 0
        indice_real = posicion - 1

        # Si el índice es negativo, lanzamos manualmente IndexError
        if indice_real < 0:
            raise IndexError

        # Accedemos a la tarea y cambiamos su estado
        tarea = lista_tareas[indice_real]

        if tarea["completada"]:
            # Informamos si la tarea ya estaba completada previamente
            print(f"\n  ℹ  La tarea {posicion} ya estaba marcada como completada.")
        else:
            tarea["completada"] = True
            print(f"\n  ✔ Tarea {posicion} marcada como completada: '{tarea['descripcion']}'")

    except IndexError:
        # Mensaje amigable al usuario cuando la posición no existe
        print(f"\n  ✘ Error: La posición {posicion} no existe en la lista.")
        print(f"     Por favor ingrese un número entre 1 y {len(lista_tareas)}.")


# -----------------------------------------------------------------------------
# MÓDULO 5: Contar tareas pendientes (función RECURSIVA)
# -----------------------------------------------------------------------------

def contar_tareas_pendientes(lista_tareas, indice=0):
    """
    Cuenta recursivamente el número de tareas con estado pendiente.

    Recorre la lista mediante autollamados incrementando el índice en cada
    paso. Suma 1 por cada tarea cuyo campo 'completada' sea False.

    Caso base   : Si el índice es igual al largo de la lista, retorna 0
                  (no quedan más tareas por revisar).
    Caso recursivo: Verifica la tarea en 'indice'. Si está pendiente, suma 1
                    y se llama a sí misma con indice+1. Si está completada,
                    solo se llama con indice+1 sin sumar.

    Args:
        lista_tareas (list): Lista de diccionarios con las tareas.
        indice       (int):  Posición actual en la lista (inicia en 0).

    Returns:
        int: Número total de tareas cuyo campo 'completada' es False.
    """
    # --- CASO BASE ---
    # Si el índice llega al final de la lista, no hay más tareas que contar
    if indice == len(lista_tareas):
        return 0  # No quedan tareas por revisar → aportamos 0

    # --- CASO RECURSIVO ---
    # Verificamos el estado de la tarea en la posición actual
    tarea_actual = lista_tareas[indice]

    if not tarea_actual["completada"]:
        # La tarea está PENDIENTE: contamos 1 y continuamos con la siguiente
        return 1 + contar_tareas_pendientes(lista_tareas, indice + 1)
    else:
        # La tarea está COMPLETADA: no sumamos, pero continuamos
        return contar_tareas_pendientes(lista_tareas, indice + 1)


# -----------------------------------------------------------------------------
# FLUJO PRINCIPAL – Menú de consola
# -----------------------------------------------------------------------------

def limpiar_pantalla():
    """
    Limpia la consola según el sistema operativo.

    Usa el comando 'cls' en Windows y 'clear' en sistemas Unix/Linux/macOS.
    Mejora la legibilidad del menú en cada iteración.

    Returns:
        None
    """
    os.system("cls" if os.name == "nt" else "clear")


def mostrar_menu():
    """
    Muestra el menú principal de opciones en consola.

    Imprime las opciones disponibles numeradas del 1 al 5 para que el
    usuario seleccione la acción que desea realizar.

    Returns:
        None
    """
    print("\n" + "=" * 55)
    print("        GESTOR DE TAREAS PENDIENTES  v1.0")
    print("=" * 55)
    print("  1. Ver lista de tareas")
    print("  2. Agregar nueva tarea")
    print("  3. Marcar tarea como completada")
    print("  4. Mostrar total de tareas pendientes")
    print("  5. Salir")
    print("=" * 55)


def main():
    """
    Función principal que controla el flujo del programa.

    Inicializa la lista de tareas y ejecuta el bucle del menú interactivo
    hasta que el usuario elija salir. Delega cada acción a la función
    correspondiente, manteniendo separación de responsabilidades.

    Returns:
        None
    """
    # Inicializamos la lista llamando al módulo de datos
    lista_tareas = obtener_tareas()
    print("\n  Bienvenido al Gestor de Tareas. Lista inicial cargada.")

    continuar = True  # Bandera de control del bucle principal

    while continuar:
        mostrar_menu()
        opcion = input("  Seleccione una opción (1-5): ").strip()

        if opcion == "1":
            # Opción 1: Mostrar todas las tareas
            mostrar_tareas(lista_tareas)

        elif opcion == "2":
            # Opción 2: Agregar una nueva tarea
            descripcion = input("\n  Ingrese la descripción de la nueva tarea: ").strip()
            if descripcion:
                lista_tareas = agregar_tarea(lista_tareas, descripcion)
            else:
                print("\n  ✘ La descripción no puede estar vacía.")

        elif opcion == "3":
            # Opción 3: Marcar una tarea como completada
            mostrar_tareas(lista_tareas)
            try:
                posicion = int(input("  Ingrese el número de la tarea a completar: "))
                marcar_completada(lista_tareas, posicion)
            except ValueError:
                print("\n  ✘ Error: debe ingresar un número entero válido.")

        elif opcion == "4":
            # Opción 4: Contar tareas pendientes usando la función recursiva
            pendientes = contar_tareas_pendientes(lista_tareas)
            print(f"\n  📋 Total de tareas pendientes: {pendientes} de {len(lista_tareas)}")

        elif opcion == "5":
            # Opción 5: Salir del programa
            print("\n  ¡Hasta luego! Recuerda completar tus tareas pendientes. 👋\n")
            continuar = False  # Cambiamos la bandera para salir del bucle

        else:
            print("\n  ✘ Opción no válida. Por favor ingrese un número del 1 al 5.")

        # Pausa breve para que el usuario pueda leer el resultado
        if continuar:
            input("\n  Presione ENTER para continuar...")
            limpiar_pantalla()


# Punto de entrada del script
# Garantiza que main() solo se ejecute si el script se corre directamente
if __name__ == "__main__":
    main()

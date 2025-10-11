tareas = [] # lista global para almacenar tareas

def mostrar_tareas():
    """muestra las tareas pendientes"""
    if tareas:
        print("\n--- TAREAS PENDIENTES ---")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")
    else:
        print("No hay tareas pendientes.")

def agregar_tarea():
    """agrega una nueva tarea a la lista"""
    nueva_tarea = input("Escriba el nombre de la tarea a agregar: ")
    
    if nueva_tarea:
        tareas.append(nueva_tarea)
        print("Tarea agregada con éxito.")
    else:
        print("El nombre de la tarea no puede estar vacío.")

def eliminar_tarea():
    """elimina una tarea por su índice"""
    mostrar_tareas()

    try:
        tarea = int(input("Escriba el índice de la tarea a eliminar: "))
        if 1 <= tarea <= len(tareas):
            tareas.pop(tarea-1)
            print("Tarea eliminada con éxito.")
        else:
            print("Número fuera de rango.")
    except ValueError:
        # evita que el usuario ingrese texto o símbolos en lugar de un número
        print("Por favor, ingrese un número válido.")

def main():
    """muestra el menú de opciones"""
    while True:
        print("\n--- MENÚ DE TAREAS ---")
        print("1. Mostrar tareas")
        print("2. Agregar tarea")
        print("3. Eliminar tarea")
        print("4. Salir")

        op = input("Seleccione una opción: ")

        if op == "1":
            mostrar_tareas()
        elif op == "2":
            agregar_tarea()
        elif op == "3":
            eliminar_tarea()
        elif op == "4":
            print("Saliendo del programa...")
            break

if __name__ == "__main__":
    main()
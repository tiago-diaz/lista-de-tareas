import json

tareas = [] # lista global para almacenar tareas

def cargar_tareas():
    """carga las tareas del json"""
    global tareas
    try:
        with open("tareas.json", "r", encoding="UTF-8") as archivo:
            try:
                tareas = json.load(archivo)

            except json.decoder.JSONDecodeError:
                with open("tareas.json", "w", encoding="UTF-8") as archivo:
                    json.dump([], archivo, indent=4)

    except FileNotFoundError:
        with open("tareas.json", "w", encoding="UTF-8") as archivo:
            json.dump([], archivo, indent=4)

def guardar_tareas():
    """guarda las tareas en el json"""
    global tareas
    with open("tareas.json", "w", encoding="UTF-8") as archivo:
        json.dump(tareas, archivo, indent=4)

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
        guardar_tareas()
        print("Tarea agregada con éxito.")
    else:
        print("El nombre de la tarea no puede estar vacío.")

def eliminar_tarea():
    """elimina una tarea por su índice"""
    if not tareas:
        print("No hay tareas pendientes.")
        return
    mostrar_tareas()
    try:
        tarea = int(input("Escriba el índice de la tarea a eliminar: "))
        if 1 <= tarea <= len(tareas):
            tareas.pop(tarea-1)
            guardar_tareas()
            print("Tarea eliminada con éxito.")
        else:
            print("Número fuera de rango.")
    except ValueError:
        # evita que el usuario ingrese texto o símbolos en lugar de un número
        print("Por favor, ingrese un número válido.")

def main():
    """muestra el menú de opciones"""
    cargar_tareas()
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
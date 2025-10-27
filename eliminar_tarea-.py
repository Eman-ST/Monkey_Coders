tareas = ["Revisar diseño", "Actualizar valores", "Completar informe"]

def eliminar_tarea(nombre_tarea):
    if nombre_tarea in tareas:
        tareas.remove(nombre_tarea)
        print("Tarea eliminada:", nombre_tarea)
    else:
        print("La tarea no existe.")

# Ejemplo
eliminar_tarea("Actualizar valores")

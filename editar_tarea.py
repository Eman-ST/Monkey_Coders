tareas = ["Revisar diseño", "Actualizar valores", "Completar informe"]

def editar_tarea(nombre_original, nuevo_nombre):
    if nombre_original in tareas:
        indice = tareas.index(nombre_original)
        tareas[indice] = nuevo_nombre
        print("Tarea actualizada:", nuevo_nombre)
    else:
        print("La tarea no existe.")

# Ejemplo
editar_tarea("Actualizar valores", "Actualizar base de datos")

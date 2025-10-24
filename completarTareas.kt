fun completarTarea(id: Int) {
    tareas.find { it.id == id }?.completada = true
}
//Creada por Daniel Ramirez Notario

fun main() {
    val tareas = mutableListOf("Estudiar", "Hacer ejercicio", "Leer")
    println("Tareas pendientes: $tareas")
    println("¿Qué tarea completaste?")
    val completada = readln()
    if (tareas.remove(completada)) {
        println("Completaste: $completada ")
    } else {
        println("Esa tarea no existe ")
    }
    println("Tareas restantes: $tareas")
}

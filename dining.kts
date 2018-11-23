class Philospher(val index: Int, val left: Any, val right: Any) {
    var count = 0
    var diner = Thread({
        while(true) {
            println("$index think : $count")
            synchronized(left) {
                synchronized(right) {
                    println("$index eat   : ${count++}")
                }
            }
        }
    })
    var eat = { diner.start() }
    fun isEating() : Boolean { return diner.isAlive() }
}

val size = 4
val forks = (0..size).map { Object() }
val loopedForks = forks + listOf(forks[0])
val philosphers = (0..size).map { i -> Philospher(i, loopedForks[i], loopedForks[i+1]) }

println("Start ...")
philosphers.forEach({it -> it.eat()})
println("... all eating")
var eating = true
while (eating) {
    Thread.sleep(1_000)
    var count = philosphers.count {it -> it.isEating()}
    eating = count != 0
    if (eating) println("... ${count} count still eating")
}
println("... end")




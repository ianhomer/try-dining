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
    fun eat() {
        diner.start()
    }

    fun isEating() : Boolean {
        return diner.isAlive()
    }
}

val size = 4
val forks = listOf(Object(), Object(), Object(), Object())
val philosphers = listOf(
            Philospher(1, forks[0], forks[1]),
            Philospher(2, forks[1], forks[2]),
            Philospher(3, forks[2], forks[3]),
            Philospher(4, forks[3], forks[0])
)

println("Start ...")
philosphers.forEach({it -> it.eat()})
println("... all eating")
var eating = true
while (eating) {
    Thread.sleep(1_000)
    var count = philosphers.count({it -> it.isEating()})
    eating = count != 0
    if (eating) println("... ${count} count still eating")
}
println("... end")




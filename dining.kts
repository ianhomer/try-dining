class Philospher(val index: Int, val left: Any, val right: Any) {
    var count = 0
    var eat = Thread({
        while(true) {
            println("$index think : $count")
            synchronized(left) {
                synchronized(right) {
                    println("$index eat   : ${count++}")
                }
            }
        }
    })
}

var size = 4
var forks = arrayOf(Object(), Object(), Object(), Object())
var philosphers = arrayOf(
            Philospher(1, forks[0], forks[1]),
            Philospher(2, forks[1], forks[2]),
            Philospher(3, forks[2], forks[3]),
            Philospher(4, forks[3], forks[0])
)

println("Start ...")
for (philospher in philosphers) {
    philospher.eat.start()
}
println("... all eating")
var finished = false
while (!finished) {
    Thread.sleep(1_000)
    var count = size
    for (philospher in philosphers) {
        if (!philospher.eat.isAlive()) {
            count++
        }
    }
    finished = (count == 0)
    if (!finished) {
        println("... ${count} count still eating")
    }
}
println("... end")




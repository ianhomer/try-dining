class Philospher(val name: String) {
    fun eat() {
        println("$name eating")
    }
}

var forks = arrayOf(Object())
var philosphers = arrayOf(Philospher("A"), Philospher("B"))
for (philospher in philosphers) {
    philospher.eat()
}



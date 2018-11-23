#!/usr/bin/python

import thread
import time
import random
from threading import Lock

# Define a function for the thread
def philosopher_eat( philosopher ):
    while 1:
        philosopher.eat()

forks = [Lock(), Lock(), Lock(), Lock(), Lock()]

class Waiter:
        def __init__(self, name, forks):
            self.name = name
            self.forks = forks

        def canEat(self, fork1, fork2):
            return fork1.acquire() and fork2.acquire()

        def release(fork1, fork2):
            fork1.release()
            fork2.release()

class Philosopher:
    def __init__(self, name, waiter, fork1, fork2):
        self.name = name
        self.waiter = waiter
        self.fork1 = fork1
        self.fork2 = fork2

    def eat(self):
        #time.sleep(random.random()/100)

        print self.name + " trying to eat"
        waiter.canEat(self.fork1, self.fork2)
        print self.name + " eating"
        #time.sleep(random.random()/100)
        waiter.release(self.fork1, self.fork2)
        print self.name + " finished eating"

waiter = Waiter("Waiter", forks)


philosophers = [
    Philosopher("A", waiter, forks[0], forks[1]),
    Philosopher("B", waiter, forks[1], forks[2]),
    Philosopher("C", waiter, forks[2], forks[3]),
    Philosopher("D", waiter, forks[3], forks[4]),
    Philosopher("E", waiter, forks[4], forks[0]),
]

# Create two threads as follows
for philosopher in philosophers:
    thread.start_new_thread( philosopher_eat, (philosopher, ) )


while 1:
   pass

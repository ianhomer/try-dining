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

class Philosopher:
    def __init__(self, name, fork1, fork2):
        self.name = name
        self.fork1 = fork1
        self.fork2 = fork2

    def eat(self):
        #time.sleep(random.random()/100)

        print self.name + " trying to eat"
        self.fork1.acquire()
        #time.sleep(random.random()/1000)

        self.fork2.acquire()
        print self.name + " eating"
        #time.sleep(random.random()/100)
        self.fork1.release()
        #time.sleep(random.random()/1000)

        self.fork2.release()
        print self.name + " finished eating"


philosophers = [
    Philosopher("A", forks[0], forks[1]),
    Philosopher("B", forks[1], forks[2]),
    Philosopher("C", forks[2], forks[3]),
    Philosopher("D", forks[3], forks[4]),
    Philosopher("E", forks[4], forks[0]),
]

# Create two threads as follows
for philosopher in philosophers:
    thread.start_new_thread( philosopher_eat, (philosopher, ) )


while 1:
   pass
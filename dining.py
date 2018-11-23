Nathan Phillips






Message List
1 new message since 10:16 AM on November 21st
Mark as read

Nathan Phillips [10:09 AM]
Ah, so you weren’t aware of something specifically wrong with it? Because it broke unittests when merged. So there is certainly something! I chatted with Kieran on Monday who had some ideas, I’ll follow through in down time today

Adam Birse [10:16 AM]
cool cool

Nathan Phillips [10:06 AM]
dining.py
#!/usr/bin/python
​
import thread
import time
import random
from threading import Lock
​
# Define a function for the thread
def philosopher_eat( philosopher ):
  philosopher.eat()
​
forks = [Lock(), Lock(), Lock(), Lock(), Lock()]
​
class Philosopher:
  def __init__(self, name, fork1, fork2):
    self.name = name
    self.fork1 = fork1
    self.fork2 = fork2
​
  def eat(self):
    print self.name + " trying to eat"
    self.fork1.acquire()
    self.fork2.acquire()
    print self.name + " eating"
    time.sleep(1)
    self.fork1.release()
    self.fork2.release()
​
​
​
philosophers = [
  Philosopher("A", forks[0], forks[1]),
  Philosopher("B", forks[1], forks[2]),
  Philosopher("C", forks[2], forks[3]),
  Philosopher("D", forks[3], forks[4]),
  Philosopher("E", forks[4], forks[0]),
]
​
​
# Create two threads as follows
for philosopher in philosophers:
  thread.start_new_thread( philosopher_eat, (philosopher, ) )
​
​
while 1:
  pass
Collapse

Message Input

Message Nathan Phillips

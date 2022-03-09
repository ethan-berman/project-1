import random
import numpy.random as random
from scipy.stats import truncnorm
from queue import PriorityQueue

#Customers in "the queue"
# * each customer has status/position in the queue

#For each line, track number of people in that line
Nlines = 3
#A list of the contents of each queue: customer + checkout time
Queues = [[] for i in range(Nlines)]

#Events that affect the state
# * Opening another line/closing a line
# * New customers arrive at checkout
def arrive():
    """This function adds a new customer to the checkout area, placing 
    them into a specific queue."""
    #Generate a checkout time for new customer
    checkouttime = 3.0 #
    print(checkouttime)
    #Place the customer in the line with the smallest total checkout time
    linetoplace = 0
    besttotal = sum(Queues[0])
    for line in range(len(Queues)):
        total = sum(Queues[line])
        if total < besttotal:
            linetoplace = line
            besttotal = total
    Queues[linetoplace].append(checkouttime)
    print("arrive", linetoplace)
    return linetoplace

# * Customer finished checking out
def checkout(line):
    """This function will remove a customer from the specified queue."""
    global Queues
    print("checkout", line)
    Queues[line] = Queues[line][1:]

# * Customers may shift lines
# * Customer abandons checkout
# * Customer adds more stuff to their cart

#Simulation loop
endt = 100.0
time = 0.0
checkouttimes = PriorityQueue() #
while time < endt:
    #determine which event happens next
    nextArrival = time + random.exponential(1) #arrival rate
    if not checkouttimes.empty():
        nextCheckout = checkouttimes.get()
        checkouttimes.put(nextCheckout) #No way to peek in the standard PQ

    if checkouttimes.empty() or nextArrival < nextCheckout[0]:
        time = nextArrival
        line = arrive()
        if len(Queues[line]) == 1:
            checkouttimes.put( (time + Queues[line][0], line))
    else:
        nextCheckout = checkouttimes.get() #Actually remove the item from the PQ
        time = nextCheckout[0]
        checkout(nextCheckout[1])
        if len(Queues[nextCheckout[1]]) > 0:
            checkouttimes.put( (time + Queues[line][0], nextCheckout[1]))
    print (Queues)



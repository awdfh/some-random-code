#!/usr/bin/env python

import random

def lottery():
    # returns 6 numbers between 1 and 40
    for i in xrange(6):
        yield random.randint(1,1000)

    # returns a 7th number between 1 and 15
    yield random.randint(1,50)

    for j in xrange(21):
        yield random.randint(1,999999)

for random_number in lottery():
    print "And the next number is... %d!" % random_number

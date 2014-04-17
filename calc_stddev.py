#! /usr/bin/env python
import sys
import math

def sum_sq_diff(series):
    total = sum(series)
    avg = float(total) / float(len(series))
    
    total_diff = 0.
    for item in series:
        diff = item - avg
        diff = diff**2
        total_diff += diff

    return total_diff / float(len(series))

def stddev(series):
    "Calculate the standard deviation of the given series."
    ssd = sum_sq_diff(series)
    return math.sqrt(ssd)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print >>sys.stderr, 'Usage: %s <filename>' % sys.argv[0]
        sys.exit(1)
        
    filename = sys.argv[1]
    print 'reading from', filename
    numbers = [ float(x) for x in open(filename) ]
    print 'Std dev is:', stddev(numbers)

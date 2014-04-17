#! /usr/bin/env python
import sys
import math

def sum_sq_diff(series):
    total = sum(series)
    avg = float(total) / float(len(series))
    
    total_diff = 0.

    series = [ (item-avg)**2 for item in series ]
    total_diff = sum(series)
    
    return total_diff

def stddev(series):
    "Calculate the standard deviation of the given series."
    ssd = sum_sq_diff(series) / float(len(series))
    return math.sqrt(ssd)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print >>sys.stderr, 'Usage: %s <filename>' % sys.argv[0]
        sys.exit(1)
        
    filename = sys.argv[1]
    print 'reading from', filename
    numbers = [ float(x) for x in open(filename) ]
    print 'Std dev is:', stddev(numbers)

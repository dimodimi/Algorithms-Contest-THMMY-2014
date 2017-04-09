from math import ceil

#Input file:
#An integer N specifying the cable's length
#N integers from 1 to N, each in a new line, specifying 
#the value of a cable of length i (1 <= i <= N)

def maxProfit():
    #input handling
    N = int(raw_input())
    prices = map(int, raw_input().split())
    
    #Create array m which holds maximum profit for
    #cable of length L in cell m[L-1]
    #
    #Break L in sums of i and L-i for i from 0 to L/2
    #(because of the symmetry of cuts)
    #and compare sums of m[i] + m[L-i] to the maximum
    #Initial maximum profit of cable with length L (whole cable)
    m = [];
    m.append(prices[0])

    for length in range(2, N+1):
        max = prices[length-1]
        for k in range(int( ceil( float(length)/2.0 ) )):
            temp = m[k] + m[length-k-2]
            if temp > max:
                max = temp
        m.append(max)

    return m[-1]

print maxProfit()
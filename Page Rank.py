import numpy as np
from numpy.linalg import inv

def input():
    n = int(raw_input())

    pages = []
    for i in range(n):
        pages.append(raw_input())

    M = np.array([map(float, raw_input().split())])
    for i in range(n-1):
        row = np.array([map(float, raw_input().split())])
        M = np.concatenate((M, row), axis=0)

    for i in range(n):
        M[:, i] /= float(np.count_nonzero(M[:, i]))

    return (n, pages, M)

def PageRank():
    (n, pages, M)   = input()
    beta            = 0.8
    numTrials       = 100

    v = np.array([1]*n) / float(n)
    bMn = (beta*M)**numTrials
    invbM = inv(np.identity(n) - beta*M)

    v_final = np.dot(( bMn + (1-beta) *np.dot(np.identity(n)-bMn, invbM)), v.T)
    
    max_index = np.argsort(-v_final)[:10]
    for index in max_index:
        print pages[index]

PageRank()
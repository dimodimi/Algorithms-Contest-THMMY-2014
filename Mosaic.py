#Sumof2 returns a list with powers of 2 that add up to a
# a = 9 returns [8, 1]
# a = 255 returns [128, 64, 32, 16, 8, 4, 2, 1]

def sumof2(a):
    binary = []
    temp = bin(a)
    while temp.count('1') > 0:
        if temp[0] == '1':
            binary.append(2**(len(temp)-1))
        temp = temp[1:]
    return binary


def mosaic():
    NM = map(int, raw_input().split())
    N = NM[0]
    M = NM[1]

    factorN = sumof2(N)
    factorM = sumof2(M)

    tiles = 0
    #split the mosaic in rectangular pieces of sides that are power of 2
    #if they are the same size then we just need 1 tile
    #if they are not, we use tiles of the smaller side and fill the largest one
    #so we use max(N, M)/min(N,M) tiles
    for i in range(len(factorN)):
        for j in range(len(factorM)):
            tiles += max(factorN[i], factorM[j])/min(factorN[i], factorM[j])

    return tiles

print mosaic()
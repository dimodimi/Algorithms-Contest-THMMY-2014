def string_matching():
	#input handling
	sizes = map(int, raw_input().split(','))
	N = sizes[0]
	M = sizes[1]
	
	s2 = raw_input()
	s1 = raw_input()
	
	#if any of the lengths are 0 then c[i][j] holds 
	#the value max(i, j)
	#Compare string s1[:i] to s2[:j]
	#c[i][j] is the minimum number of steps
	#to transform one to the other
	#3 choices:
	#1)find the minimum for s1[:i-1] and s2[:j-1] --> c[i-1][j-1]
	#and add cost of substitution if s1[i] != s2[j]
	#2)try to best fit s1[:i-1] to s2[:j] (c[i-1][j]) and add cost of insertion
	#3)try to best fit s1[:i] to s2[:j-1] (c[i][j-1]) and add cost of insertion
	c = []
	c.append(range(N+1))
	
	for i in range(1, M+1):
		c.append([i])
		for j in range(1, N+1):
			if s1[i-1] == s2[j-1]:
				c[i].append(c[i-1][j-1])
			else:
				c[i].append(min( [c[i-1][j] + 1, c[i][j-1] + 1, c[i-1][j-1] + 1] ))
	
	return c[M][N]
	
print string_matching()
	
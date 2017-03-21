import math

# Combination calc
def chooseGoose(x,y):
	print(x,y)
	print(x-y)
	return float(math.factorial(x)/(math.factorial(y)*math.factorial(x-y)))

# x = how many drawn of what you want
# n = how many total cards
# k = how many total in deck
# N = total deck size
# http://stattrek.com/probability-distributions/hypergeometric.aspx
def hypergeometric(x,k,n,N):
	x = float(x)
	N = float(N)
	n = float(n)
	k = float(k)
	return float(chooseGoose(k,x)*chooseGoose(N-k,n-x))/chooseGoose(N,n)*100.0

# x = 1 | k = 3 | n = 74 | N = 75
# 3,1 | 75-3, 74-1 | 75, 74

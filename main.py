import math

# Combination calc
def chooseGoose(x,y):
	return float(math.factorial(x)/(math.factorial(y)*math.factorial(x-y)))

# x = how many drawn of what you want
# n = how many total cards
# k = how many total in deck
# N = total deck size
# http://stattrek.com/probability-distributions/hypergeometric.aspx
def hypergeometric(x,N,n,k):
	x = float(x)
	N = float(N)
	n = float(n)
	k = float(k)
	return float(chooseGoose(k,x)*chooseGoose(N-k,n-x))/chooseGoose(N,n)

print(hypergeometric(2.0,52.0,5.0,26.0))
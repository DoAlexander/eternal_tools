import math, cmd

# Combination calc
def chooseGoose(x,y):
	return float(math.factorial(x)/(math.factorial(y)*math.factorial(x-y)))

# x = how many drawn of what you want
# n = how many total cards
# k = how many total in deck
# N = total deck size
# http://stattrek.com/probability-distributions/hypergeometric.aspx
def hypergeometric(x,n,k,N):
	x = float(x)
	N = float(N)
	n = float(n)
	k = float(k)
	return float(chooseGoose(k,x)*chooseGoose(N-k,n-x))/chooseGoose(N,n)*100.0

#Based off of example from python docs
class hyperShell(cmd.Cmd):
	intro = 'Welcome to the example scheduling algorithm.   Type help or ? to list commands.\n'
	prompt = '> '
	
	def do_quit(self, arg):
		'Quits the example.'
		raise SystemExit
	
	def do_hg_dist(self, arg):
		'Solves hypergeometric problem. For example you want 1 Seek Power in hand after 10 cards with 3 copies in 75 card deck. hg_dist 1 10 3 75 '
		print(hypergeometric(*parse(arg)))
		
def parse(arg):
	'Convert a series of zero or more numbers to an argument list'
	return list(map(int, arg.split()))

if __name__ == '__main__':
	hyperShell().cmdloop()
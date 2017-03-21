import cmd
import hypergeometry
from deck import *
from card import *
f_card = Card("siraf", 3, 'TJ', 3, 4, 'overwhelm', 'exhaust siraf to play a {T} unit and double its stats')

f_cards = [f_card]
print(f_cards[0].name)
f_deck = Deck(f_cards)


#Based off of example from python docs
class hyperShell(cmd.Cmd):
	intro = 'Welcome to the example scheduling algorithm.   Type help or ? to list commands.\n'
	prompt = '> '
	
	def do_quit(self, arg):
		'Quits the example.'
		raise SystemExit
	
	def do_hg_dist(self, arg):
		'Solves hypergeometric problem. For example you want 1 Seek Power in hand after 10 cards with 3 copies in 75 card deck. hg_dist 1 10 3 75 '
		input = parse(arg)
		chance = 0.0
		# for x in range(input[0],input[1]+1):
		chance += hypergeometry.hypergeometric( input[0],input[1],input[2],input[3] )
		# print(x,chance)
		print( '{first:3.2f}% chance that you have drawn {num_drawn:d} out of {num_copies:d} copies after {draws:d} draws with a {deck_size:d} card deck.'.format( first=chance,
		 num_drawn=input[0], num_copies=input[2], draws=input[1], deck_size=input[3] ) )
	
	def do_pr_cards(self,arg):
		for x in f_deck:
			for y in x.cards:
				print(y)


def parse(arg):
	'Convert a series of zero or more numbers to an argument list'
	return list(map(int, arg.split()))

if __name__ == '__main__':
	hyperShell().cmdloop()
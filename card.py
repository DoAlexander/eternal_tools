class Card:
	# Power Cost | Influence | Strength | Health Pool | Keywords | Card-Text
	def __init__(self, name, cost, inf, st, hp, kws, text):
		self.name = name
		self.inf = inf
		self.st = st
		self.hp = hp
		self.kws = kws
		self.text = text

	def __str__(self):
		return "METAGAME BRRRRRRRRRRRRRREAKDOWN"
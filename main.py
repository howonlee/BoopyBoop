import string
import sys

mongo_obj_id_settings = {
		length: 24,
		alphabet: string.hexdigits
		}

class BoopyBoop():
	def __init__(self, words=None, settings=None):
		if words == None:
			self.words = ["boopy","boop","word","letter","number","person","pen","class","people","sound","water","side","place","man","men","woman","women","boy","girl","year","day","week","month","name","sentence","line","air","land","home","hand","house","picture","animal","mother","father","brother","sister","world","head","page","country","question","answer","school","plant","food","sun","state","eye","city","tree","farm","story","sea","night","day","life","north","south","east","west","child","children","example","paper","music","river","car","foot","feet","book","science","room","friend","idea","fish","mountain","horse","watch","color","face","wood","list","bird","body","dog","family","song","door","product","wind","ship","area","rock","order","fire","problem","piece","top","bottom","king","space"]
		else:
			self.words = words
		if settings == None:
			self.settings = {}
		else:
			self.settings = settings

	def id_to_string(self, id_string):
		convert id string to normal number
		xor with some large constant

if __name__ == "__main__":
	id_arg = sys.argv[1]
	BoopyBoop()
	print str

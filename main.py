import string
import sys

mongo_obj_id_settings = {
		"length": 24,
		"alphabet": string.hexdigits
		}

class BoopyBoop():
	def __init__(self, words=None, settings=None):
		if words == None:
			self.words = ["boopy","boop","word","letter","number","person","pen","class","people","sound","water","side","place","man","men","woman","women","boy","girl","year","day","week","month","name","sentence","line","air","land","home","hand","house","picture","animal","mother","father","brother","sister","world","head","page","country","question","answer","school","plant","food","sun","state","eye","city","tree","farm","story","sea","night","day","life","north","south","east","west","child","children","example","paper","music","river","car","foot","feet","book","science","room","friend","idea","fish","mountain","horse","watch","color","face","wood","list","bird","body","dog","family","song","door","product","wind","ship","area","rock","order","fire","problem","piece","top","bottom","king","space"]
		else:
			self.words = words
		if settings == None:
			self.settings = mongo_obj_id_settings
		else:
			self.settings = settings
		self.len_words = len(self.words)

	def id_to_string(self, id_string):
		id_num = int(id_string, base=len(self.settings["alphabet"]))
		words = []
		while id_num > self.len_words:
			word_idx = id_num % self.len_words
			id_num = id_num // self.len_words
			words.append(self.words[word_idx])
		return words

if __name__ == "__main__":
	boop = BoopyBoop()
	print boop.id_to_string("23423412affeec")

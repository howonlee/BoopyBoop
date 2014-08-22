import string
import sys

mongo_obj_id_settings = {
		"length": 24,
		"alphabet": string.hexdigits
		}

class BoopyBoop():
	def __init__(self, words=None, settings=None):
		if words == None:
			#criteria:
			#not abstract, but concrete. must be able to sense it directly
			#not about people, but about things that are not people
			#about 100 of them: currently 35
			self.words = ["boopy","boop","pen","pencil","water","air","steam","wind","land","rock","steel","house","cat","school","plant","sun","star","tree","farm","sea","paper","chair","music","river","car","book","room","fish","mountain","horse","wood","bird","dog","song","door","ship","fire","bow","spoon","fork","roof","apple","cloth","wheat","boat","gold","drum","flute","ball","cube","triangle","square","hill","orange","grape","iron","brush"]
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

	def string_to_id(self, word_arr):
		id_num = 0
		for word in word_arr:
			id_num += self.words.index(word)
			id_num *= self.len_words
		#return the string formatted hex version, in the case of mongodb


if __name__ == "__main__":
	boop = BoopyBoop()
	print boop.id_to_string("507f1f77bcf86cd799439011")
	print len(boop.id_to_string("507f1f77bcf86cd799439011"))
	print boop.len_words

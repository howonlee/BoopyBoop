import string
import sys
from baseconv import BaseConverter

MONGO_OBJ_ID_SETTINGS = {
		"length": 24,
		"alphabet": string.hexdigits
		}

MD5_ID_SETTINGS = {
		"length": 16,
		"alphabet": string.hexdigits
		}

class BoopyBoop():
	def __init__(self, words=None, settings=None):
		if words == None:
			#criteria:
			#not abstract, but concrete. must be able to sense it directly
			#not about people, but about things that are not people
			#about 100 of them: currently 35
			self.words = ["pen","pencil","water","air","steam","wind","land","rock","steel","house","cat","school","plant","sun","star","tree","farm","sea","paper","chair","music","river","car","book","room","fish","mountain","horse","wood","bird","dog","song","door","ship","fire","bow","spoon","fork","roof","apple","cloth","wheat","boat","gold","drum","flute","ball","cube","triangle","square","hill","orange","grape","iron","brush"]
		else:
			self.words = words
		if settings == None:
			self.settings = MONGO_OBJ_ID_SETTINGS
		else:
			self.settings = settings
		self.len_words = len(self.words)
		self.base_conv = BaseConverter(self.settings["alphabet"])

	def id_to_string(self, id_string):
		id_num = int(id_string, base=len(self.settings["alphabet"]))
		words = []
		print "id_to_string id_num: ", id_num
		while id_num > 0:
			word_idx = id_num % self.len_words
			id_num = id_num // self.len_words
			print "curr id_num: ", id_num
			words.append(self.words[word_idx])
		return words

	def string_to_id(self, word_arr):
		id_num = 0
		word_arr.reverse()
		for idx, word in enumerate(word_arr):
			id_num += self.words.index(word)
			print "curr_id_num: ", id_num
			if idx < (len(word_arr) - 1):
				id_num *= self.len_words
		print "string_to_id id_num: ", id_num
		return self.base_conv.encode(id_num)

if __name__ == "__main__":
	boop = BoopyBoop()
	boop_res = boop.id_to_string("507f1f77bcf86cd799439011")
	print boop_res
	print len(boop_res)
	print boop.len_words
	print boop.string_to_id(boop_res)

import hashlib
import datetime

class Block: 
	def __init__(self, index, data, previousHash='00000'):
		self.index = index
		self.timestamp = str(datetime.datetime.now())
		self.data = data
		self.previousHash = previousHash
		self.hash = self.calculateHash()

	# for saving data into the block

	def update(self, dic):
		self.__dict__=dic
		return self

	# calculating the hash for previously saved files
	# uses save encoding 
	def calculateHash(self):
		return hashlib.sha256(str(self.index).encode('utf-8')
		+ self.previousHash.encode('utf-8')
		+ str(self.data).encode('utf-8')
		+ self.timestamp.encode('utf-8')).hexdigest()

	def isValid(self):
		return self.hash == self.calculateHash()

	def printBlock(self):
		return ("\nBlock %" + str(self.index)
			+ "\nData: " + str(self.data)
			+ "\nTimestamp: " + str(self.timestamp)
			+ "\nBlock Hash: " + str(self.hash)
			+ "\nBlock Previous hash: " + str(self.previousHash)
			+ "\n------------------")
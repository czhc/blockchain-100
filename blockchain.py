import json
import os
from block import Block 

class BlockChain:
	def __init__(self, file="block.chain"):
		self.chain = [Block(0, "Genesis")]
		self.file = file

	def getLatestBlock(self):
		return self.chain[len(self.chain)-1]

	def getNextIndex(self):
		return self.getLatestBlock().index+1

	def generateBlock(self, data):
		self.chain.append(Block(self.getNextIndex(), data, self.getLatestBlock().hash))

	def isChainValid(self):
		for i in range(1, len(self.chain)):
			if not self.chain[i].isValid():
				return False
			if self.chain[i].previousHash != self.chain[i-1].hash:
				return False
		return True

	def printBlockChain(self):
		return ''.join([self.chain[i].printBlock() for i in range(1, len(self.chain))])


	def save(self):
		if(self.isChainValid()):
			with open(self.file, 'w') as f:
				f.write(json.dumps(self, default=lambda obj:obj.__dict__))

	def open(self):
		if(os.path.exists(self.file)):
			with open(self.file) as f:
				data = json.load(f)
				self.__dict__ = data
				self.chain = [Block("","").update(dic) for dic in data["chain"]]
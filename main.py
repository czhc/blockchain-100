from blockchain import BlockChain

def main():
	blockchain = BlockChain()
	blockchain.generateBlock("Hello World!")
	blockchain.generateBlock(3)
	blockchain.generateBlock({"account": 123123, "mount": 100})

	print(blockchain.printBlockChain())
	print("Chain valid?" + str(blockchain.isChainValid()))
	blockchain.save()

	blockchain.chain[1].data = "Corrupt data"
	print(blockchain.printBlockChain())
	print("Chain valid?" + str(blockchain.isChainValid()))
	blockchain.save()

	test = BlockChain()
	test.open()
	print(test.printBlockChain())
	print("Chain valid? " + str(test.isChainValid()))
	test.save()

if __name__ == '__main__':
	main()
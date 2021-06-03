import hashlib
import json

#difficulty is set to 4

class Block():
    def __init__(self, nonce,time, data,prevHash=''):
        self.time = time
        self.data = data
        self.nonce = nonce
        self.prevHash = prevHash
        self.hash = self.mineBlocks()
    
    def calcHash(self):
        block_string = json.dumps({"nonce":self.nonce,"data":self.data,"prevHash":self.prevHash,"timeStamp":self.time}).encode()
        #print(block_string)
        hash = hashlib.sha256(block_string).hexdigest()
        #print(hash)
        return hash

    def mineBlocks(self):
        self.nonce = 0
        self.hash = self.calcHash()
        while(self.hash[:4]!='0000'):
            self.nonce += 1
            self.hash = self.calcHash()
        return self.hash

class BlockChain():
    def __init__(self):
        self.chain = [self.genesisBlock(),]

    def addBlock(self, nonce, time, data):
        block = Block(nonce, time, data, self.chain[-1].hash)
        self.chain.append(block)

    def genesisBlock(self):
        return Block(0,17/12/2000,"First block")
    
    def printChain(self):
        for i in self.chain:
            print("\nNonce: ",i.nonce)
            print("Time: ",i.time)
            print("Data: ",i.data)
            print("PrevHash: ",i.prevHash)
            print("Current data hash: ",i.hash,"\n")

    def isChainValied(self):
        for i in range(1, len(self.chain)):
            prevBlock = self.chain[i-1]
            currentBlock = self.chain[i]
            if(currentBlock.hash != currentBlock.calcHash()):
                return False
            if(currentBlock.prevHash != prevBlock.hash):
                return False
        return True

blockChain = BlockChain()
blockChain.addBlock(0,12/12/2002,"Second block")
blockChain.addBlock(1,13/12/2002,"third block")
blockChain.addBlock(2,14/12/2002,"fourth block")
blockChain.printChain()
blockChain.chain[1].data = "modified data"
print(blockChain.isChainValied())
    
    


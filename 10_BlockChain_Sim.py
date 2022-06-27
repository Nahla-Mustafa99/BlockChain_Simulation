from datetime import datetime
import random
import hashlib
import json
#########
class Blockchain:

    # This function is created to create the first block
    def __init__(self):
        self.chain = []
        str=""
        data0=str.join(['0','0'])
        data_hashed0 = hashlib.sha256(data0.encode()).hexdigest()
        block=self.create_block(data0,proof=0,previous_hash='0',N=4)
        block=self.proof_of_work(block)
        self.chain.append(block)

    # This function is created to add further blocks into the chain
    def create_block(self,data_hashed, proof, previous_hash,N):
        block = {'index': len(self.chain) ,#+ 1,
                 'timestamp':str(datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash,
                 #'loop':loop,
                 'difficulty':N,
                 'Tx_root':data_hashed
                 }
        return block

    # This function is created to return the previous block
    def print_previous_block(self):
        return self.chain[-1]

    # This function is created to return the first block
    def gen_block(self):
        return self.chain[0]
    # This is the function for proof of work and used to successfully mine the block
    def proof_of_work(self, block):
        new_proof = 0
        check_proof = False
        n=block['difficulty']
        while check_proof is False:
            hash_operation = self.hash(block)
            if hash_operation[:n] == n*'0':
                check_proof = True
                break;
            else:
                new_proof +=1
                block['proof'] = new_proof

        if(check_proof==True) :
            return block
        #else:
            #return -1



    def proof_of_work_Attack(self, block1,block2):
            new_proof1 = 0
            new_proof2=0
            check_proof = False
            no_of_loops=0
            n1 = block1['difficulty']
            n2=block2['difficulty']

            while check_proof is False:
                hash_operation1 = self.hash(block1)
                hash_operation2=self.hash(block2)
                if hash_operation1[:n1] == n1 * '0' or hash_operation2[:n2]==n2*'0':
                    check_proof = True
                    if(hash_operation1[:n1] == n1 * '0'):
                        is_User=True
                        block=block1
                        break;
                    elif(hash_operation2[:n2] == n2 * '0'):
                        block=block2
                        is_User=False
                        break;
                else:
                    if(no_of_loops%100!=1 and no_of_loops%100!=2 and no_of_loops%100!=3 and no_of_loops%100!=4 and no_of_loops%100!=5 and no_of_loops%100!=6 and no_of_loops%100!=7 and no_of_loops%100!=8 and no_of_loops%100!=9 and no_of_loops%100!=10 and no_of_loops%100!=11 and no_of_loops%100!=12 and no_of_loops%100!=13):
                        new_proof1 += 1
                    new_proof2+=1
                    block1['proof'] = new_proof1
                    block2['proof'] = new_proof2

                no_of_loops+=1

            if (check_proof == True):
                return [block,is_User]

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False

            previous_proof = previous_block['proof']
            proof = block['proof']
            N=block['difficulty']
            hash_operation = self.hash(block)


            if hash_operation[:N] != N*'0':
                return False
            previous_block = block
            block_index += 1

        return True
###########END OF CLASS
# Mining a new block
def mine_block(data, blockchain1):
        previous_block = blockchain1.print_previous_block()
        # difficulty = Get_Difficulty(previous_block)
        difficulty = Get_Difficulty(blockchain1)
        previous_hash = blockchain1.hash(previous_block)
        initial_block = blockchain1.create_block(data, 0, previous_hash, difficulty)
        proof = blockchain1.proof_of_work(initial_block)
        new_block = proof
        blockchain1.chain.append(new_block)


def valid():
    valid = blockchain.chain_valid(blockchain.chain)
    if valid:
       print("To ensure the integrity of The Blockchain after the blocks are appended:")
       print('The Blockchain is valid.')
       previous_block = blockchain.print_previous_block()
       genesisBlock = blockchain.gen_block()
       datetime_object11 = datetime.strptime(genesisBlock['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
       datetime_object22 = datetime.strptime(previous_block['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
       secondsPassed00 = (datetime_object22 - datetime_object11).total_seconds()
       print("time taken to append the previous blocks is "+str(secondsPassed00)," seconds")
    else:
        print('The Blockchain is not valid')


# Create the object of the class blockchain
blockchain = Blockchain()
#CHOOSE N OF ZEROS = DIFICULTY
genesisBlock=blockchain.gen_block() #1st block
def Get_Difficulty(blockchain__):
    last_block = blockchain__.print_previous_block()
    newDifficulty = last_block['difficulty']
    datetime_object = datetime.strptime(genesisBlock['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
    secondsPassed = (datetime.now()-datetime_object).total_seconds()
    if (len(blockchain__.chain) > secondsPassed) and (newDifficulty + 1) <6 :
      newDifficulty+=1
    elif (len(blockchain__.chain) < secondsPassed) and (newDifficulty - 1) > 0:
      newDifficulty-=1
    return newDifficulty

# D1,D2,,etc.  are actual blocks to be mined in the sys at a time(that is represented by the index  of the list)
#Normal scenario
blocks_in_sys_ex1=[['D1'],['D2'],['D3'],['D4'],['D5']]
#NORMAL SCENARIO! display and mining of each block
print("NORMAL SCENARIO! : No Attacks Or Wrong Blocks")
print("Blocks to be mined in the system (D1,D2,..etc. represents the data of each block to be mined in the system at a time ")
print(blocks_in_sys_ex1)
index=0
while index< len(blocks_in_sys_ex1):
    data_array=blocks_in_sys_ex1[index][0] #get
    mine_block(data_array,blockchain) # mine and append
    print("block of " + data_array, ": is appended")  # print
    index+=1
# Display blockchain in json format
print("")
print("The BlockChain:")
i=0
while i<len(blockchain.chain):
    print(blockchain.chain[i])
    i+=1
print("")
print("length of The Blockchain is "+str(len(blockchain.chain)))

# Check integrity of blockchain
valid()


#Attack scenario!
# To get the longest branch in attack case
def get_the_longest_path(blockchain_Users,blockchain_Attacker):
    if len(blockchain_Users.chain)>=len(blockchain_Attacker.chain) :
        blockchain.chain=blockchain_Users.chain
        print("")
        print("Attack Failed")
    else:
        blockchain.chain=blockchain_Attacker.chain
        print("")
        print("Attack Succeeded")
    i=0
    print("")
    print("THE BlockChain:")
    while i < len(blockchain.chain):
        print(blockchain.chain[i])
        i += 1
    print("")
    print("length of The Blockchain is "+str(len(blockchain.chain)))
    previous_block = blockchain.print_previous_block()
    genesisBlock = blockchain.gen_block()
    datetime_object11 = datetime.strptime(genesisBlock['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
    datetime_object22 = datetime.strptime(previous_block['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
    secondsPassed00 = (datetime_object22 - datetime_object11).total_seconds()
    print("time taken to append the previous blocks is " + str(secondsPassed00), "seconds")

# T6,T7,,etc.  are the lagal blocks to be mined in the sys at a time(that is represented by the index  of the list)
# f1,f2,,etc.  are the illlagal blocks to be mined in the sys at a time(that is represented by the index  of the list)
blocks_in_sys_Users=[['T6'],['T7'],['T8'],['T9'],['T10']]
blocks_in_sys_Attacker=[['f5'],['f6'],['f7'],['f8'],['f9']]
############
blockchain_Users = Blockchain()
blockchain_Users.chain = blockchain.chain
blockchain_Attacker = Blockchain()
blockchain_Attacker.chain = blockchain.chain[0:len(blockchain.chain) - 1]
def simulate_Attack():
    prev_block_of_attacker=blockchain.chain[len(blockchain.chain)-2]
    print("")
    print("ATTACK SIMULATION:")
    print("MAIN BLOCKS:")
    print(blocks_in_sys_Users)
    print("T6,T7,..etc. represents the data of the legal blocks to be mined in the sys at a time ")
    print("")
    print("Attacker BLOCKS:")
    print(blocks_in_sys_Attacker)
    print("f5,f6,..etc. represents the data of the Illegal blocks that the attacker tries to mine in the sys at a time ")
    print("")
    print("The attacker will try to append to a previous block which is as follows:")
    print(prev_block_of_attacker)
    print("")
    ## make 2 virtual blockchains until chhose the longest branch
    ##
    index_users=0
    index_attacker=0
    #there are blocks to be mined  in the system(of attacker and users)
    while index_users< len(blocks_in_sys_Users) and index_attacker<len(blocks_in_sys_Attacker):
        data1=blocks_in_sys_Users[index_users][0]
        #print(data1)
        #
        data2= blocks_in_sys_Attacker[index_attacker][0]
        #print(data2)
        # To make initial block of users
        previous_block = blockchain_Users.print_previous_block()
        difficulty1 = Get_Difficulty(blockchain_Users)
        previous_hash1 = blockchain_Users.hash(previous_block)
        # To make initial block of attacker
        previous_block = blockchain_Attacker.print_previous_block()
        difficulty2 = Get_Difficulty(blockchain_Attacker)
        previous_hash2 = blockchain_Attacker.hash(previous_block)
        # Choose the difficulty of this round
        if difficulty2<difficulty1 :
            difficulty=difficulty1
        else:
            difficulty=difficulty2
        # To make initial block of users
        initial_block1 = blockchain_Users.create_block(data1, 0, previous_hash1, difficulty)
        # To make initial block of Attacker
        initial_block2 = blockchain_Attacker.create_block(data2, 0, previous_hash2, difficulty)
        # WHO WINS THE ROUND!
        array_check=blockchain.proof_of_work_Attack(initial_block1,initial_block2)
        if(array_check[1]==True):
            blockchain_Users.chain.append(array_check[0])
            index_users+=1
            print(data1,"Block is appended to the Users(main) branch")
        elif(array_check[1]==False):
            blockchain_Attacker.chain.append((array_check[0]))
            index_attacker+=1
            print(data2, "Block is appended to the Attacker branch")
    i=0
    get_the_longest_path(blockchain_Users,blockchain_Attacker)



simulate_Attack()
#get_the_longest_path()
# print 2 versions
i=0
print("")
print("The BlockChain with Main Branch Version :")
while i < len(blockchain_Users.chain):
    print(blockchain_Users.chain[i])
    i += 1
print("")
print("length of This version is "+str(len(blockchain_Users.chain)))
print("")
print("The BlockChain with Atacker Branch Version :")
i = 0
while i < len(blockchain_Attacker.chain):
    print(blockchain_Attacker.chain[i])
    i += 1
print("")
print("length of This version "+str(len(blockchain_Attacker.chain)))


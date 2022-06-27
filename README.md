# BlockChain_Simulation
Implementing a blockchain Python application :
- That keeps track of blockchain branches and appends new 
blocks to the longest branch.
- In order to append a block, the block contain a 64bit nonce that causes the hash to start with N zeros.
- Each block should contain a random list of transactions.

# Objectives:
1) Control the puzzle hardness by varying N so that the block chain grows at 1 block per second.
2) Simulate an attack on the blockchain: There is a chance that an attacker appears and tries to grow 
his own branch of the blockchain, by appending to a previous block (not the latest verified block).
The attack speed is a predetermined parameter.
3) By experimentation,find the attack speed where an attack is successful (the main branch is 
replaced with the attacker’s branch), and compare it to the legit blockchain speed.

# Attack Simulation
In this implementation the attacker has about 53% percent of the compute capacity, and the attack may fail in this case or success but in most cases attack will success.

# Requirements 
- The script is written in python 3 so it need to ![1](https://user-images.githubusercontent.com/75391814/175976928-720ef9cf-ebb2-4648-8f72-a5dc6a268ee3.png)
be installed.
- libraries used : datetime, random, haslib ,json. 

## output screen samples
- Normal Scenario of blockchain (no attacks)
![Normal Scenario](https://user-images.githubusercontent.com/75391814/175977945-6bdfa246-f9a0-4955-a1a9-24e1400942ef.png)
- Attack simulation (Failed attack)
![2](https://user-images.githubusercontent.com/75391814/175978983-69c7a258-e466-474e-a42a-c584dd03ee44.png)

![3](https://user-images.githubusercontent.com/75391814/175978886-81255170-1a34-4282-91df-5dc6819270c3.png)

![4](https://user-images.githubusercontent.com/75391814/175979034-2e536dc1-a29a-4586-93bf-5707df19baec.png)
- A second normal scenario of blockchain (no attacks)
![11](https://user-images.githubusercontent.com/75391814/175979542-98a08114-e962-457c-92c5-acdf951b3e34.png)

-  Attack simulation (Attack succeeded)
![22](https://user-images.githubusercontent.com/75391814/175979584-6a20865e-14aa-4cbc-8227-c2037c281559.png)

![33](https://user-images.githubusercontent.com/75391814/175979607-0df639ac-193f-45d2-bc0b-399c0f3989a7.png)

![44](https://user-images.githubusercontent.com/75391814/175979639-5d17ea16-0117-4c04-9903-a60097c1728a.png)





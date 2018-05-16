# blockchain-graph-analysis
## Introduction
This work consists of four steps. The first three are data preprocessing. 
### 1. Blockchain data parsing
We parse the raw data in the bitcoin blockchain into transactions between public addresses as *tran.txt*. In *tran.txt*, each line represents one bitcoin transaction. The corresponding meanings of its columns:

<center>
  
| Column       | Corresponding meaning          | 
| ------------- |:-------------:|
| 1      | The public address of the sender | 
| 2      | The public address of the recepient     |  
| 3 | The value of the transaction      |  
| 4 | Data and time of the transaction      |  
| 5 | The block number of the transaction      |  

</center>

### 2. Linking related public addresses
We link the public addresses that are owned by the same user into *links.txt*, *along.txt*, *a2u.txt* and *u2a.txt*. 

Each line in *links.txt* is an undirected link between two public addresses. *along.txt* contains the addresses that are not linked to any other public addresses we have seen so far. Each line in *a2u.txt* is a *address:user_id* pair, mapping an public address to the id of its user. Each line in *u2a.txt* is a *user_id:addresses* pair, mapping an user id to the public addresses it owns, delimited by ','.

### 3. Creating the user graph 
We transform the transactions between public addresses in the step 1 into transactions between users and result in *user_graph.txt*. The corresponding meanings of its columns:

| Column       | Corresponding meaning          | 
| ------------- |:-------------:|
| 1      | The user id of the sender | 
| 2      | The user id of the recepient     |  
| 3 | The value of the transaction      |  
| 4 | Data and time of the transaction      |  
| 5 | The block number of the transaction      |  

The number of transactions between users will be less than the number of transactions between public addresses because multiple transactions between the same users at each timestamp are summed into one.

### 4. Graph analysis of the user graph

## Prerequisite for step 1

Requirements:
1. Please make sure that you have the bitcoin blockchain in your computer, otherwise go to https://bitcoin.org/en/full-node#ubuntu-1604.
2. python packages: plyvel, python-bitcoinlib, and bitcoin-blockchain-parser (https://github.com/alecalve/python-bitcoin-blockchain-parser)


You can install the required python packages by running the following commands Unix in terminal: 

```
  cd blockchain-graph-analysis
  chmod +x ./pkg.sh
  ./pkg.sh
```

## Instructions
For parsing, make sure you have the bitcoin blockchain ready in *blockchain_path*. You need to specify the date of the last blockchain you want to parse as *end_date*  and the directory for the parsing results as *out_dir* in *YYYY-MM-DD* format. 

Run in terminal:

```
python parsing.py blockchain_path end_date out_dir
```

For linking, you need to the parsed data ready and specify the directory of the results as *direc*. 

Run in terminal:

```
python linking.py direc
```

For creating the user graph, you need to the results from the previous steps and specify the directory of the results as *direc*. 

Run in terminal:

```
python ugraph.py direc
```

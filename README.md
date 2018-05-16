# blockchain-graph-analysis

This work consists of four steps:
1. Blockchain data parsing
2. Linking related public addresses
3. Creating user graph
2. Graph analysis of the user graph

## Prerequisite for step 1

Requirements:
1. Please make sure that you have the bitcoin blockchain in your computer, otherwise go to https://bitcoin.org/en/full-node#ubuntu-1604.
2. python packages: plyvel, python-bitcoinlib, and bitcoin-blockchain-parser (https://github.com/alecalve/python-bitcoin-blockchain-parser)


You can install the required python packages by running the following commands Unix in terminal: 

1.
```
  cd blockchain-graph-analysis
```
2. 
```
  chmod +x ./pkg.sh
```
3. 
```
./pkg.sh
```

## Instructions
For parsing, make sure you have the bitcoin blockchain ready in *blockchain_path*. Then you need to specify the date of the last blockchain you want to parse as *end_date*  and the directory your want to save the parsing results as *out_dir* in *YYYY-MM-DD* format. 

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











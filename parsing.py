import sys
import os
import datetime
import psutil
import time
from blockchain_parser.blockchain import Blockchain

COINBASE = "0000000000000000000000000000000000000000000000000000000000000000"

def isvalid(output):
    return (len(ou.addresses)>0 and not ou.is_unknown() and ou.value>0)

def parsing(blockchain_path, index_path, end, out_dir):
    tran_file = open(out_dir+'tran.txt','a')
    logging = open(out_dir+'parsing_log.txt','a')
    trans = dict()

    blk_count = 0
    t0 = time.time()
    blockchain = Blockchain(os.path.expanduser(blockchain_path))
    for block in blockchain.get_ordered_blocks(os.path.expanduser(index_path)):
        if block.header.timestamp>end:
            break
        else:
            for t in block.transactions:
                try:
                    outputs = []
                    total_val = 0
                    for ou in t.outputs:
                        if isvalid(ou):
                            outputs.append( {'value':ou.value,\
                                            'address':ou.addresses[0].address})
                            total_val += ou.value
                    # store the indexed outputs in memory
                    if len(outputs)>0:
                        trans[t.hash] = dict(zip(range(len(outputs)),outputs))
                    else:
                        continue
                    for ou in t.outputs:
                        if not isvalid(ou):
                            continue
                        fraction = ou.value/total_val
                        for i in t.inputs:
                            if i.transaction_hash != COINBASE:
                                prev_hash = i.transaction_hash
                                index = i.transaction_index
                                if not prev_hash in trans or \
                                               not index in trans[prev_hash]:
                                    continue
                                prev_ou = trans[prev_hash][index]
                                prev_addr = prev_ou['address']
                                tran_file.write(prev_addr+","+\
                                    ou.addresses[0].address+","+t.hash+\
                                    ','+str(round(prev_ou['value']*fraction,2))+\
                                    ","+str(block.header.timestamp)+","+\
                                    str(block.height)+"\n")
                                del trans[prev_hash][index]
                                if len(trans[prev_hash])==0:
                                    del trans[prev_hash]
                except:
                    continue
        blk_count+=1
        if blk_count%100==0:
            if blk_count>100:
                logging.write('===================================================\n')
            logging.write('Blocks:'+str(blk_count)+'\n')
            logging.write('Time:'+str(time.time()-t0)+'\n')
            logging.write('CPU_percent:'+str(psutil.cpu_percent())+'\n')
            logging.write('Memory:'+str(psutil.virtual_memory())+'\n')
        del block
    logging.write('Total_time:'+str(time.time()-t0)+'\n')
    logging.close()
    tran_file.close()
    print('Done')

if __name__ == '__main__':
    _blockchain_path = sys.argv[1]
    _end = sys.argv[2].split('-')
    _out_dir = open(sys.argv[3],'a')

    end = datetime.datetime(int(_end[0]),int(_end[1]),int(_end[2]))
    if out_dir[0:2]=='./':
        out_dir = _out_dir
    else:
        out_dir = './'+_out_dir

    if out_dir[-1]=='/':
        out_dir = out_dir
    else:
        out_dir = out_dir+'/'

    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)

    index_path = blockchain_path + 'index'

    parsing(blockchain_path, index_path, end, out_dir)



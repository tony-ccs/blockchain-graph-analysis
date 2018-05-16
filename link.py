import sys
import os
import time
import pandas as pd
import os.path
import networkx as nx
def find_links(tran=None):
    p1 = 'links.txt'
    p2 = 'along.txt'
    if os.path.isfile(p1) and os.path.isfile(p2):
        return pd.read_csv(p1,header=None), pd.read_csv(p2,header=None)
    else:
        f1 = open(p1,'a')
        f2 = open(p2,'a')
        prev_tid = ''
        group = []
        tran = tran.append(tran.loc[0,:])
        t0 = time.time()
        logging = open('linking_log.txt','a')
        for t in tran.iterrows():
            if t[1][2]==prev_tid:
                group.append(t[1][0])
            else:
                if len(group)>1:
                    for i in range(1,len(group)):
                        f1.write(group[i-1]+','+group[i]+'\n')
                elif len(group)==1:
                    for a in group:
                        f2.write(a+'\n')
                group = [t[1][0]]
                prev_tid = t[1][2]
        logging.write('Time for linking:'+str(time.time()-t0)+'\n')
        logging.close()
        f1.close()
        f2.close()
        return pd.read_csv(p1,header=None), pd.read_csv(p2,header=None)

def get_users(linked_df=None, along_df=None):
    p1 = 'a2u.txt'
    p2 = 'u2a.txt'
    if os.path.isfile(p1) and os.path.isfile(p2):
        a2u_file = open('a2u.txt','r')
        u2a_file = open('u2a.txt','r')
        a2u = dict()
        u2a = dict()
        a2u_lines = a2u_file.readlines()
        for line in a2u_lines:
            l = line[:-1].split(":")
            a2u[l[0]] = l[1]
        u2a_lines = u2a_file.readlines()
        for line in u2a_lines:
            l = line[:-1].split(":")
            u2a[l[0]] = l[1].split(',')
        a2u_file.close()
        u2a_file.close()
        return a2u, u2a
    else:
        t0 = time.time()
        logging = open('linking_log.txt','a')
        G = nx.from_pandas_edgelist(linked_df, 0,1)
        del linked_df
        G.add_nodes_from(along_df[0].values)
        del along_df
        groups = nx.connected_components(G)
        del G
        uid = 0
        a2u = dict()
        u2a = dict()
        a2u_file = open(p1,'a')
        u2a_file = open(p2,'a')
        for grp in groups:
            u2a[str(uid)] = grp
            u2a_file.write(str(uid)+':'+','.join(grp)+'\n')
            for a in grp:
                a2u[a] = str(uid)
                a2u_file.write(a+':'+str(uid)+'\n')
            uid += 1
        logging.write('Time for parsing:'+str(time.time()-t0)+'\n')
        logging.close()
        u2a_file.close()
        a2u_file.close()
        return a2u, u2a

if __name__ == '__main__':
    _dir = sys.argv[1]
    if not _dir[0:2]=='./':
        os.chdir('./'+_dir)
    else:
        os.chdir(_dir)
    tran = pd.read_csv('tran.txt',header=None)
    linf_df, along_df = find_links(tran)
    del tran
    get_users(link_df, along_df)

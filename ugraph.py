import pandas as pd
from link import get_users

def to_uid(x):
        if x in a2u:
            return a2u[x]
        else:
            return x

def make_ugraph():
	tran = pd.read_csv('tran.txt',header=None)
	a2u = get_users()[0]

	tran[0] = tran[0].apply(lambda x: a2u[x])
	tran[1] = tran[1].apply(to_uid)
	tran = tran.groupby([0,1,2,4,5], as_index=False).sum()
	tran = tran.sort_values(by=[4])
	tran.to_csv('user_graph.txt', index=False, header=False)

if __name__ == '__main__':
	_dir = sys.argv[1]
	if not _dir[0:2]=='./':
        os.chdir('./'+_dir)
    else:
    	os.chdir(_dir)
    make_ugraph()

	
import requests
import sys
import tqdm
import multiprocessing

def checkurl(target):
    url = URLBASE + target + "/"
#    print("Working on {}".format(url))
    r = aws.get(url)
    if r.status_code == 200:
        return(target)
    else:
        return

URLBASE = "https://s3.amazonaws.com/"

filename = sys.argv[1]
procs = int(sys.argv[2])

aws = requests.Session()

q = multiprocessing.Queue()

if __name__ == '__main__':
    with open(filename,"r") as f:
        buckets = [line.strip() for line in f]

    pool = multiprocessing.Pool(processes=procs)
    results = [pool.apply_async(checkurl, args=(x,)) for x in buckets]
    output = [p.get() for p in results]
    for i in output:
        if i:
            print(i)

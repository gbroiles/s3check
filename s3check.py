import requests
import sys
import tqdm

URLBASE = "https://s3.amazonaws.com/"

filename = sys.argv[1]

aws = requests.Session()

with open(filename,"r") as f:
    buckets = [line.strip() for line in f]

working_buckets = []

for bucket in tqdm.tqdm(buckets):
    url = URLBASE + bucket + "/"
    print("Working on {}".format(url))
    r = aws.get(url)
#    print(r.status_code)
    if r.status_code == 200:
        working_buckets.append(bucket)

print("Working buckets:")
for bucket in working_buckets:
    print(bucket)

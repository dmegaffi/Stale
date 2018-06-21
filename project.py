import json
from pprint import pprint
import re
import requests
r = requests.get('https://api.github.com/orgs/tendermint/repos?page=1&per_page=100')
r.json()


for x in r:
    print(x)


def main():
  with open("output.txt", 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
      fd.write(chunk)

with open ("output.txt") as f:
  data = json.load(f)

pprint(data)
#
##iterate through list of dictionaries, find value for key ("name")
repos = [re["name"] for re in data]
print(repos)

print(len(repos))
if __name__ == '__main__':
  
  main()

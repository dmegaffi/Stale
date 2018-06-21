
import json
from pprint import pprint
import re
import requests

#pushes byte chunk
def last_update(file,key1,key2,r):
  with open(file, 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
      fd.write(chunk)
  with open (file) as f:
    data = json.load(f)
##iterate through list of dictionaries
  repos = [re[key1] for re in data]
  last_update = [re[key2] for re in data]
  print(len(repos))
  
  for x,y, in zip(repos, last_update):
    print("\n\t\t",x, " --- repo was last updated on --- ", y)

def main():
  r = requests.get('https://api.github.com/orgs/tendermint/repos?page=1&per_page=100')
  r.json()
  
  last_update("output.txt", "name", "pushed_at",r)

if __name__ == '__main__':
  
  main()

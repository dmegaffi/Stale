
import json
from pprint import pprint
import re
import requests
r = requests.get('https://api.github.com/orgs/tendermint/repos?page=1&per_page=100')
r.json()

#pushes byte chunk
def decoder(file,key):
  with open(file, 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
      fd.write(chunk)
  with open (file) as f:
    data = json.load(f)
  pprint(data)
##iterate through list of dictionaries, find value for key ("name")
  repos = [re[key] for re in data]
  print(repos)
  print(len(repos))

def main():
    decoder("output.txt", "name")

if __name__ == '__main__':
  
  main()

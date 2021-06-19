import re
import os
from datetime import datetime
import pandas as pd

fname = 'michaeljburry-20210619172112.md'

file = open(fname, "r")
raw  = file.read().split('any Twitter client.', 1)[-1]
data = os.linesep.join([s for s in raw.splitlines() if s])

def get_date(input):
  out = datetime.strptime(input, '%d %B %Y')
  return(out)

def get_url(raw):
  out = re.search('\((.*)\)\:', raw).group(1)
  return(out)

def get_id(url):
  out = re.sub('.*status/', '', url)
  out = re.search('\d+',out).group(0)
  return(out)

def get_text(raw):
  out = re.search('\)\:\s(.*)',raw).group(1)
  return(out)

df = pd.DataFrame(data.splitlines(), columns=['raw'])
df['date'] = df['raw'].str.extract('\[(\s?\d+\s+[A-z]+\s+\d+)\]')
df['date'] = df['date'].apply(get_date)
df['url'] = df['raw'].apply(get_url)
df['id'] = df['url'].apply(get_id)
df['text'] = df['raw'].apply(get_text)

df.to_csv(fname+'.csv', index=False)
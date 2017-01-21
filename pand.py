

import re
import pandas as pd
import time
from datetime import datetime

#get the current date
today = time.strftime("%d/%m/%Y")


#loading data
data = pd.read_csv(
    'access.log', 
    sep=r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)(?![^\[]*\])', 
    engine='python',     
    usecols=[0, 3],
    names=['ip', 'time'])




#cleaning of data

data = data.tail(n=10)	# to save the last top 10 ip address

data['time'] = data['time'].str.strip('[]') #remove brackets from time
data.set_index('ip', inplace=True)# to remove the index
print data

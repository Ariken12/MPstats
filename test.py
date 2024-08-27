import requests as r
import datetime as dt
import time as t

token = '66c83e9a0ea899.5280906501a06672de4c5f55c764555248370db6'
hashed_token = sum([int(char) << (i*8) for i, char in enumerate(tuple(token.encode('utf-8')))]) 
token_length = 55
decoded_token = ''.join([bytes(((hashed_token >> (i*8)) % 256,)).decode('utf-8') for i in range(token_length)])

date1 = t.strftime('%Y-%m-%d', t.localtime(t.time() - 60 * 60 * 24 * 60))
date2 = t.strftime('%Y-%m-%d')
print(date1, date2)
# print(hashed_token)
# print(decoded_token)

parameters = {
    'auth-token': decoded_token,
    'fbs': 0,
    'd1': date1,
    'd2': date2,
    'path': 'TRIS' 
}
headers = {
    #'X-Mpstats-TOKEN': decoded_token,
    'Content-Type': 'application/json'
}
a = r.post(f'https://mpstats.io/api/wb/get/brand', params=parameters, headers=headers)

with open('test_output.json', 'w', encoding='utf-8') as ofile:
    print(a.text, file=ofile)


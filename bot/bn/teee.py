import requests

res = requests.get('http://127.0.0.1:8000/mohammed/')

# print(res.content)
json = res.json()
bz='efjefn'
data = []
for x in json:
    y = x['fields']
    z = y['username']
    data.append(z)

print(data)

if bz in data:
    print('done')
else:
    print('ohh')
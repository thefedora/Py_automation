import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')

type(res)

res.status_code == requests.codes.ok

len(res.text)

print(res.text[:250])
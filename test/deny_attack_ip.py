#! python3
# -*- coding:utf8 -*
# Deny Attack IP

import pyperclip, re, time


ipv4_address = re.compile(r'\d+\.\d+\.\d+\.\d+')
#ipv4_address = re.compile(r'\d\.\d\.\d\.\d')
text = str(pyperclip.paste())
#print(text)
matches = []

for groups in ipv4_address.findall(text):
    matches.append(groups)

now = time.gmtime(time.time())

print('*'*80)
print()
print('conf t')
print(now.tm_mon)
for i in range(len(matches)):
    print('ip address %s' %matches[i])
 
print ('wr')
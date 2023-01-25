import re
s='''
 <html>
  <head> 
  <title>Current IP Address Allocations 
  </title>
   </head>
    <body>
IP Address are 172.45.78.109
LoopBack Address: 127.0.0.1
Computer 1: 10.67.89.101
Computer 2: 11.67.98.102
Computer 3: 12.68.98.102 
</body> 
</html>
'''
info = re.findall(r'[\d.-]+', s)
#ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', s )
ipp = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
findIP = re.findall(ipp,s)
print(ipp)
print(findIP)
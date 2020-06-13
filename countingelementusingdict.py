string=input()
map1={};
for i in range(len(string)):
    map1.setdefault(string[i],[]).append(i)
print(map1)    
'''l=map1['h']
print(len(l[:l.index(15)]))'''
for i in map1:
    print(len(map1[i]),end=" ")
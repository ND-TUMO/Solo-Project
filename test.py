from random import randint 
lst1 = ['abcdefghijklmnopqrstuvwxyz1234567890']
nmb = input('enter a number:')
assert isinstance(nmb,int),'Your variable nmb is not of type==int()'

total = ''
for i in range(1,nmb):
  total=total+lst1[randint(len(lst1))]
  print(total)

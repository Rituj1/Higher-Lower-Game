import random

'''dict = [{'Rituj1':'Rituj2', 'Rituj3':'Rituj4'}, {'Rituj5':'Rituj5', 'Rituj6':'Rituj7'}]
print(dict)

A = random.choice(dict)
print(A)
print(dict[pos(A)])
del dict[A]
print(dict)
'''

list = [1,2,3]
A = random.choice(list)
print(A)
B = random.choice(list)
if B==A:
    B = random.choice(list)
print(B)
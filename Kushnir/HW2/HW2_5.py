from random import randint

lst = []
for i in range(10):
    lst.append(randint(0, 100))
lst = sorted(lst, reverse = True)

print(lst, chr(65))


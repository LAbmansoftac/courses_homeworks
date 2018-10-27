n = int(input("Введите число: "))
lis = [0] * n 
for i in range(n): 
    lis[i] = i 
 

lis[1] = 0
 
m = 2 
while m < n: 
    if lis[m] != 0: 
        j = m * 2 
        while j < n:
            lis[j] = 0 
            j = j + m 
    m += 1
 
# Вывод простых чисел на экран 
lis2 = []
for i in lis:
    if lis[i] != 0:
        lis2.append(lis[i])
 
del lis
print ('Простые числа до числа ', n, ':\n', lis2)

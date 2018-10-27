array = [1, 12, 23, 10, 15, 8, 19]

print('The list of numbers before buble sorting: \n', array)

array2 = []

j = 1
for i in range(len(array), 0, -1):
	for j in range(0, len(array) - 1):
		if array[j] > array[j + 1]:
			array[j], array[j+1] = array[j+1], array[j]
			array2.append(array[j]) 

array2 = array
print('The list of numbers after buble sorting: \n', array2)

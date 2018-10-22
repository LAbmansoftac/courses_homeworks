x = int(input('Enter number: '))
i = 1

width = x + (x - 1)


for i in range (1, x):
    print("{0:^{1}.{2}}".format("*" * (i + (i - 1)), width, width))

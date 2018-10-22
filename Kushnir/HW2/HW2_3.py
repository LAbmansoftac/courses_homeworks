piramid = []
text = str('*')
quantity = int(input('Enter number: '))
step = int(0)

while step < quantity:
    piramid.append(text)
    print(text + '\n' + text)
    step += 1
    text = text + '*'

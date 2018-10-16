import random
user_number = int(input("Please enter number (more than 0): " ))
if user_number <=  0:
    print("Error! Please enter number again.")
else:
    print(user_number)
    random_choice = random.randint(0, user_number)
    print("Random number is", random_choice)
    result = random.sample( range(0, user_number), random_choice)
    print(result)
print ("Lets move on the next task!")
random_number = random.randint(1000, 1000000)
print("Random number is ", random_number)
print("Fourth element of random number is ", ((random_number % 10000) - (random_number % 1000))//1000)

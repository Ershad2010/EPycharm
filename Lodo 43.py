import random
lodo = [1,2,3,4,5,6,7,8,9]
random_number = random.choice(lodo)
# print(random_number)
if random_number == 9:
    print('***Congratulation You Won***')
else:
    print(random_number,'is not 9')
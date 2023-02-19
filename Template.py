import random

person = ['Sharmin', 'Cumilla']
name = person[0]
loction = person[1]
sentence_one_group = [f'This is {name}.', f'I am {name}.', f'My name is {name}.', f'{name} is my name.']
sentence = random.choice(sentence_one_group)
sentence_two_group = [f'I live in {loction}', f'{loction} is my home town']
sentence_two = random.choice(sentence_two_group)
print(sentence_two)
import random

print('The magic 8ball knows all.')

predictions = ['It is certain', 'Yes definitely', 'Most likely', 'Signs point to yes', 'Reply hazy try again',
               'Concentrate and ask again', 'Don\'t count on it', 'My sources say no']

question = input('What do you wish to know? ')

while question != 'done':
    if question.find('Will') == 0 or question.find('will') == 0:
        print(random.choice(predictions))
        question = input('Ask another question or type \'done\': ')
    else:
        question = input('Please ask a yes or no question: ')





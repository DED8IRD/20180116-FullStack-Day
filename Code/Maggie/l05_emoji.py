import random

EYES = [':', ';', 'B', '8', 'X', '};', ']:']
NOSES = [ '', '\'', '>', 'o', '0', '^', '\'']
MOUTHS = [')', 'D', '(', '[', ']', '/', 'P', 'p']

def emoji():
    i = 0
    print('Emoji Generator. \nHere are your five faces:\n')
    while i < 5:
        print(random.choice(EYES) + random.choice(NOSES) + random.choice(MOUTHS) + '\n')
        i += 1


if __name__ == '__main__':
    emoji()
from random import choice, randint

smells = ['stinky', 'fragrant', 'decaying', 'effervescent', 'purple']
feels = ['jubilant', 'weird', 'aroused', 'sleepy', 'anxious']
looks = ['light', 'dark', 'decrepit', 'new', 'expensive']


def start():
    name = greet()
    adventure = make_adventure()
    do_adventure(name, adventure)


def make_adventure():
    adventure = []
    height = randint(2, 3)
    width = randint(2, 3)
    for i in range(height):
        adventure.append([])
        for j in range(width):
            room = {
                'description': random_description(),
                'visited': False
            }
            adventure[i].append(room)

    return adventure


def random_description():
    look = choice(looks)
    smell = choice(smells)
    feel = choice(feels)
    return 'It looks {}. You smell {}. You feel {}'.format(look, smell, feel)


def do_adventure(name, adventure):
    position = (0, 0)
    while True:
        position = read_description_and_move(position, adventure)


def read_description_and_move(position, adventure):
    height = len(adventure)
    width = len(adventure[0])
    i, j = position
    message = []

    if not adventure[i][j]['visited']:
        message.append('You have entered a new room')
        adventure[i][j]['visited'] = True
    else:
        message.append('You have returned to a previously visited room')

    message.append(adventure[i][j]['description'])
    available_directions = find_available_directions(position, adventure)

    message.append(
        'You can see doors to the {}'.format(
            ','.join(available_directions)))
            
    print('. '.join(message))

    direction = ''
    while direction not in available_directions:
        print('Select a direction to move')
        if position == (0, 0):
            print('Type Exit to exit the dungeon')
        direction = input()
        if direction == 'Exit':
            exit()
    return update_position(direction, position)


def update_position(direction, position):
    i, j = position
    if direction == 'South':
        return (i + 1, j)
    if direction == 'North':
        return (i - 1, j)
    if direction == 'East':
        return (i, j + 1)
    if direction == 'West':
        return (i, j - 1)


def find_available_directions(position, adventure):
    i, j = position
    height = len(adventure)
    width = len(adventure[0])
    available_directions = []

    if i > 0:
        available_directions.append('North')
    if i < height - 1:
        available_directions.append('South')

    if j > 0:
        available_directions.append('West')
    if j < width - 1:
        available_directions.append('East')

    return available_directions


def greet():
    print('enter your name')
    name = input()
    print('hello {}'.format(name))
    return name


if __name__ == '__main__':
    start()

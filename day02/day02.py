import re

cube_bag = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def fits_in_bag(cube_count):
    return cube_count['red'] <= cube_bag['red'] and cube_count['green'] <= cube_bag['green'] and cube_count['blue'] <= cube_bag['blue']


with open('input1') as input_file:
    id_count = 0
    for line in input_file:
        game_info = re.search(r'([0-9]+):(.*)', line)
        game_id = game_info.group(1)
        game = game_info.group(2)
        rounds = game.split(';')
        rounds_valid = True
        for game_round in rounds:
            cube_amounts = re.findall(r'([0-9]+) (blue|green|red)', game_round)
            cube_count = {
                'red': 0,
                'green': 0,
                'blue': 0
            }
            for (amount, color) in cube_amounts:
                cube_count[color] = int(amount)
            rounds_valid = rounds_valid and fits_in_bag(cube_count)
        if rounds_valid:
            id_count += int(game_id)
    print(id_count)


with open('input2') as input_file:
    power_count = 0
    for line in input_file:
        game_info = re.search(r'([0-9]+):(.*)', line)
        game_id = game_info.group(1)
        game = game_info.group(2)
        rounds = game.split(';')
        cube_count = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        for game_round in rounds:
            cube_amounts = re.findall(r'([0-9]+) (blue|green|red)', game_round)
            for (amount, color) in cube_amounts:
                if cube_count[color] < int(amount):
                    cube_count[color] = int(amount)
        power_count += (cube_count['red'] * cube_count['green'] * cube_count['blue'])
    print(power_count)



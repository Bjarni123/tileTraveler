# possibly better to divide this into more folders later on

def allowed_directions(position: list[2] = [1, 1]) -> list[4]:
    """
    Takes in position and returns which directions are not blocked by a wall.
    Returns: [North: bool, East: bool, South: bool, West: bool]
    """
    return [True, True, True, True]

def get_level_list(file_name: str) -> list[list]:
    """Opens txt file given and returns it as a list containing a list with each line as a list."""
    return reversed([
        ['w', 'w', 'w', 'w', 'w', 'w', 'w'],
        ['w', '0', '0', '0', '0', '0', 'w'],
        ['w', '0', 'w', 'w', 'w', '0', 'w'],
        ['w', '0', '0', '0', 'w', '0', 'w'],
        ['w', '0', 'w', '0', 'w', '0', 'w'],
        ['w', '0', 'w', '0', 'w', '0', 'w'],
        ['w', 'w', 'w', 'w', 'w', 'w', 'w']
    ])

thing = (get_level_list('nan'))

for x in thing:
    print(x)
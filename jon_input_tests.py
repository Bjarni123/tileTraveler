from classes.player import Player
def main():
    while True:
        user_input = input('Select a direction')
        move(user_input)

def move(user_input):
    player = Player()
    match user_input:
        case 'N':
            player.playe_move_north()
        case 'E':
            player.playe_move_east()
        case 'S':
            player.playe_move_south()
        case 'W':
            player.playe_move_west()

    player_location = player.get_location()
    print(player_location)
if __name__ == '__main__':
    main()
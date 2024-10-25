print(f'Welcome to Yahtzee!')

print('\n')

while True:
    num_players = input("How many player are playing today? ")

    if num_players == '1':
        num_players = int(num_players)
        break

    elif num_players == '2':
        num_players = int(num_players)
        break

    elif num_players == '3':
        num_players = int(num_players)
        break

    elif num_players == '4':
        num_players = int(num_players)
        break

    elif num_players == '5':
        num_players = int(num_players)
        break

    else:
        print('\n')
        print('Invalid Response.')
        print('\n')
        continue


players = []
while True :

    if len(players) == num_players:
        break
    print('\n')
    player = input('Please enter your name here: ')
    print(f'Welcome in, {player}.')

    players.append(player)



player_dict = {}

numbers = [*range(1 , num_players+1)]

for player, number in zip(players, numbers):
    player_dict[player] = number

print('\n')

response = input('Would You Like to Read The Rules? (yes/no) ')
if response == 'yes':
    print('Each player takes a score card. To decide who goes first, each player in turn rolls all 5 dice.'
          ' The player with the highest total goes first. Play then passes to the left.')
else:
    print('Starting Game')


from roll_dice import roll_1, roll_2, roll_3, roll_4, roll_5

possible_scores = {'ones' : 0, 'twos' : 0, 'threes' : 0, 'fours' : 0, 'fives' : 0, 'sixes' : 0,
          'three of a kind' : 0, 'two of a kind' : 0,
          'small straight' : 0, 'large straight' : 0, 'full house' : 0}

score = {'ones' : 0, 'twos' : 0, 'threes' : 0, 'fours' : 0, 'fives' : 0, 'sixes' : 0,
          'three of a kind' : 0, 'two of a kind' : 0,
          'small straight' : 0, 'large straight' : 0, 'full house' : 0}

rolls = 0
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0

def start_roll():
    global dice1, dice2, dice3, dice4, dice5
    dice1 = roll_1()
    dice2 = roll_2()
    dice3 = roll_3()
    dice4 = roll_4()
    dice5 = roll_5()
    print(f"Here's the dice you rolled:"
          f"\n\t{dice1} {dice2} {dice3} {dice4} {dice5}")

def roll_again(rolls):
    global dice1, dice2, dice3, dice4, dice5
    while True:
        if rolls < 2:
            re_roll = [i for i in input(f"\nWhich dices do you want to re-roll? Place spaces between the dices you want to re-roll."
                  f"\nEnter n to not roll again.  ").split()]
            if 'n' in re_roll:
                break
            if '1' in re_roll:
                    dice1 = roll_1()
            if '2' in re_roll:
                    dice2 = roll_2()
            if '3' in re_roll:
                    dice3 = roll_3()
            if '4' in re_roll:
                    dice4 = roll_4()
            if '5' in re_roll:
                    dice5 = roll_5()
            rolls += 1
            print(f"Here's your new roll:"
                  f"\n\t{dice1} {dice2} {dice3} {dice4} {dice5}")
        else:
            break

def ones(one):
    if 1 == dice1:
        one += 1
        possible_scores['ones'] = one

    if 1 == dice2:
        one += 1
        possible_scores['ones'] = one

    if 1 == dice3:
            one += 1
            possible_scores['ones'] = one

    if 1 == dice4:
            one += 1
            possible_scores['ones'] = one

    if 1 == dice5:
            one += 1
            possible_scores['ones'] = one

def twos(two):
    if 2 == dice1:
        two += 2
        possible_scores['twos'] = two

    if 2 == dice2:
        two += 2
        possible_scores['twos'] = two

    if 2 == dice3:
        two += 2
        possible_scores['twos'] = two

    if 2 == dice4:
        two += 2
        possible_scores['twos'] = two

    if 2 == dice5:
        two += 2
        possible_scores['twos'] = two

def threes(three):
    if 3 == dice1:
        three += 3
        possible_scores['threes'] = three

    if 3 == dice2:
        three += 3
        possible_scores['threes'] = three

    if 3 == dice3:
        three += 3
        possible_scores['threes'] = three

    if 3 == dice4:
        three += 3
        possible_scores['threes'] = three

    if 3 == dice5:
        three += 3
        possible_scores['threes'] = three


def fours(four):
    if 4 == dice1:
        four += 4
        possible_scores['fours'] = four

    if 4 == dice2:
        four += 4
        possible_scores['fours'] = four

    if 4 == dice3:
        four += 4
        possible_scores['fours'] = four

    if 4 == dice4:
        four += 4
        possible_scores['fours'] = four

    if 4 == dice5:
        four += 4
        possible_scores['fours'] = four

def fives(five):
    if 5 == dice1:
        five += 5
        possible_scores['fives'] = five

    if 5 == dice2:
        five += 5
        possible_scores['fives'] = five

    if 5 == dice3:
        five += 5
        possible_scores['fives'] = five

    if 5 == dice4:
        five += 5
        possible_scores['fives'] = three

    if 5 == dice5:
        five += 5
        possible_scores['fives'] = five

def sixes(six):
    if 6 == dice1:
        six += 6
        possible_scores['sixes'] = six

    if 6 == dice2:
        six += 6
        possible_scores['sixes'] = six

    if 6 == dice3:
        six += 6
        possible_scores['sixes'] = six

    if 6 == dice4:
        six += 6
        possible_scores['sixes'] = six

    if 6 == dice5:
        six += 6
        possible_scores['sixes'] = six

def bonus(bonus):
    pass

start_roll()

roll_again(rolls)
ones(one)
twos(two)
threes(three)
fours(four)
fives(five)
sixes(six)

print(possible_scores)
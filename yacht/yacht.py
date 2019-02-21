def little_straight(dice):
    if dice.count(1) == 1 and dice.count(2) == 1 and dice.count(3) == 1 and dice.count(4) == 1 and dice.count(5) == 1:
        return 30
    else:
        return 0

def big_straight(dice):
    if dice.count(2) == 1 and dice.count(3) == 1 and dice.count(4) == 1 and dice.count(5) == 1 and dice.count(6) == 1:
        return 30
    else:
        return 0

def four_of_a_kind(dice):
    if dice.count(1) >= 4:
        return 4*1
    elif dice.count(2) >= 4:
        return 4*2
    elif dice.count(3) >= 4:
        return 4*3
    elif dice.count(4) >= 4:
        return 4*4
    elif dice.count(5) >= 4:
        return 4*5
    elif dice.count(6) >= 4:
        return 4*6
    else:
        return 0

def full_house(dice):
    if dice.count(1) == 3 or dice.count(2) == 3 or dice.count(3) == 3 or dice.count(4) == 3 or dice.count(5) == 3 or dice.count(6) == 3:
        if dice.count(1) == 2 or dice.count(2) == 2 or dice.count(3) == 2 or dice.count(4) == 2 or dice.count(5) == 2 or dice.count(6) == 2:
            return sum(dice)
        else:
            return 0
    else:
        return 0
    

# Score categories
# Change the values as you see fit
YACHT = lambda dice: 50 if dice[0] == dice[1] == dice[2] == dice[3] == dice[4] else 0
ONES = lambda dice: dice.count(1)*1
TWOS = lambda dice: dice.count(2)*2
THREES = lambda dice: dice.count(3)*3
FOURS = lambda dice: dice.count(4)*4
FIVES = lambda dice: dice.count(5)*5
SIXES = lambda dice: dice.count(6)*6
FULL_HOUSE = full_house
FOUR_OF_A_KIND = four_of_a_kind
LITTLE_STRAIGHT = little_straight
BIG_STRAIGHT = big_straight
CHOICE = lambda dice: sum(dice)

    
def score(dice, category):
    if category == YACHT:
        return YACHT(dice)
    if category == ONES:
        return ONES(dice)
    if category == TWOS:
        return TWOS(dice)
    if category == THREES:
        return THREES(dice)
    if category == FOURS:
        return FOURS(dice)
    if category == FIVES:
        return FIVES(dice)
    if category == SIXES:
        return SIXES(dice)
    if category == FULL_HOUSE:
        return FULL_HOUSE(dice)
    if category == FOUR_OF_A_KIND:
        return FOUR_OF_A_KIND(dice)
    if category == CHOICE:
        return CHOICE(dice)
    if category == LITTLE_STRAIGHT:
        return LITTLE_STRAIGHT(dice)
    if category == BIG_STRAIGHT:
        return BIG_STRAIGHT(dice)


        
    

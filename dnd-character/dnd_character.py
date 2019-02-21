import random
import math

class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)
        
    def ability(self):
        scores = [random.choice([1,2,3,4,5,6]) for i in range(4)]

        min_score = min(scores)
        scores.remove(min_score)

        return sum(scores)


def modifier(constitution):
    return math.floor((constitution - 10)/2)

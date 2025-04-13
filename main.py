# add next letter
# check all words for match
# if match, add to set
# once all words <= 10 letters long are found, connect them by first and last letter
class Letter:
    def __init__(self, char, side):
        self.char = char
        self.side = side
    def __str__(self):
        return self.char + " " + str(self.side)
    def __repr__(self):
        return str(self.char) + ": " + str(self.side)

sides = [['e','s','i'],['j','a','u'],['r','x','o'],['v','n','m']]

with open('words.txt', 'r') as f:
    words = {word[:-1] for word in f.readlines()}

found = set()
building = set()
for i,side in enumerate(sides):
    for char in side:
        building.add(Letter(char,i))
MAX_LENGTH = 8
count=0
for s,side in enumerate(sides):
    for char in side:
        for o,other_side in enumerate(sides):
            if s != o:
                for each in sides:
                    each1 = each + other_side[0]
                    each2 = each + other_side[1]
                    each3 = each + other_side[2]
                    building.add(each1)
                    building.add(each2)
                    building.add(each3)

    count+=1
    if count >= MAX_LENGTH:
        break

print(building)

            


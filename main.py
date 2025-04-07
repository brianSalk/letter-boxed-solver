# add next letter
# check all words for match
# if match, add to set
# once all words <= 10 letters long are found, connect them by first and last letter
class Letter:
    def __main__(self, char, side):
        self.char = letter
        self.side = side

sides = [['e','s','i'],['j','a','u'],['r','x','o'],['v','n','m']]

with open('words.txt', 'r') as f:
    words = {word[:-1] for word in f.readlines()}


found = {}


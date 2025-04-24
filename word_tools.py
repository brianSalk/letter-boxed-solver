import re
from collections import defaultdict
from random import shuffle


def get_valid_words(letters, sides):
    pattern = '^[' + "".join(letters) + ']{5,}$'
    print(f'{pattern=}')
    ans = []
    with open('words.txt', 'r') as f:
        for word in f.readlines():
            word = word[:-1]
            if re.match(pattern, word):
                ans.append(word)
    letter_to_number = {}
    for i,side in enumerate(sides):
        for letter in side:
            letter_to_number[letter] = i
    res = []
    for word in ans: 
        last_number = -1
        is_valid = True
        for letter in word:
            letter = letter.lower()
            if last_number == letter_to_number[letter]:
                is_valid = False
            last_number = letter_to_number[letter]
        if is_valid:
            res.append(word)
    return res


def get_chains(words, depth):
    shuffle(words)
    chains = [[word] for word in words]
    count = 1
    first_letter = defaultdict(list)
    # create dict of last_letter
    for word in words:
        first_letter[word[0]].append(word)
    # create all chains
    while count <= depth:
        new_chains = []
        for chain in chains:
            for word in first_letter[chain[-1][-1]]:
                new_chains.append(chain + [word])
        chains = new_chains
        count += 1
    valid_chains = defaultdict(set)
    for chain in chains:
        ls = set()
        for i,word in enumerate(chain):
            ls.update([c for c in word]) 
            if len(ls) == 12:
                valid_chains[i+1].add(tuple(chain[:i+1]))
                break

    return valid_chains

def get_best_words(words):
    m = 0
    best_words = []
    for word in words:
        if len(set(word)) > m:
            m = len(set(word))
            best_words = [word]
        elif len(set(word)) == m:
            best_words.append(word)
    return best_words
    
if __name__ == "__main__":
    sides = [
        list("qno"), list("adu"), list("ewc"), list("rtl")
        ]
    letters = set()
    for side in sides:
        for letter in side:
            letters.add(letter)
    words = get_valid_words(letters, sides)
    print('got words')
    chains = get_chains(words, 2)
    print(chains[2])

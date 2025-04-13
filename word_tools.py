import re

def get_valid_words(letters, sides):
    pattern = '^[' + "".join(letters) + ']{3,}$'
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
    chains = [[word] for word in words]
    count = 1
    while count <= depth:
        new_chains = []
        for chain in chains:
            for word in words:
                if chain[-1][-1] == word[0]:
                    new_chains.append(chain + [word])
        chains.extend(new_chains)
        count += 1
    return chains



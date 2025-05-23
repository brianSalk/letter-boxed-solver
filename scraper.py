import selenium
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from itertools import permutations
from random import shuffle

import word_tools



driver = webdriver.Chrome()
driver.get('https://www.nytimes.com/puzzles/letter-boxed')
continue_button = driver.find_element(By.CLASS_NAME, "purr-blocker-card__button")

driver.execute_script("arguments[0].click();", continue_button)
play_button = driver.find_element(By.XPATH, '//button[text()="Play"]')
driver.execute_script("arguments[0].click();", play_button)
element = driver.find_element(By.CLASS_NAME, "lb-square-container")

# Scroll it into view
driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", element)
sleep(2)

actions = ActionChains(driver)
def get_sides_and_letters(driver):
    actions = ActionChains(driver)
    letters = list('qwertyuiopasdfghjklzxcvbnm')
    letters_set = set()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        actions.send_keys(letter).perform()
        for span in WebDriverWait(driver, 2).until(
                EC.presence_of_all_elements_located((By.TAG_NAME, "span"))
                ):
            try:
                span.text
            except Exception:
                continue
            if span and span.text and span.text.lower() == letter:
                letters_set.add(span.text.lower())
        actions.send_keys(Keys.BACKSPACE).perform()
    print('these are the letter:', letters_set)


    # find which letters are on which side
    sides = []
    found = set()
    for letter in letters_set:
        side = [letter]
        found_next_letter = False
        if letter in found:
            continue
        for next_letter in letters_set:
            found_next_letter = False
            actions.send_keys(letter + next_letter).perform()
            for span in  driver.find_elements(By.TAG_NAME, "span"):
                if span.text != '' and span.text.lower() == next_letter:
                    found_next_letter = True
                    actions.send_keys(Keys.BACKSPACE)
                    break
            if not found_next_letter:
                print(letter, 'is on same side as', next_letter)
                side.append(next_letter)
                found.add(next_letter)
            actions.send_keys(Keys.BACKSPACE)
            actions.send_keys(Keys.BACKSPACE)
        sides.append(side)
    four_sides = set()
    for side in sides:
        four_sides.add(frozenset(side))
    actions.send_keys(Keys.BACKSPACE).perform()
    actions.send_keys(Keys.BACKSPACE).perform()
    return four_sides, list(letters_set)


if __name__ == "__main__":
    sides, letters = get_sides_and_letters(driver)

    words = word_tools.get_valid_words(letters, sides)
    print("best words:", word_tools.get_best_words(words))
    chains_dict = word_tools.get_chains(words, 2)
    chains = []
    for cs in chains_dict.values():
        for c in cs:
            chains.append(c)
    chains.sort(key=lambda x: len(x))
    print(f'{chains=}')
    for chain in chains:
        print('next chain:')
        for word in chain:
            for char in word:
                actions.send_keys(char).perform()
                print(char,end='')
            print(' ', end='')
            sleep(1)
            actions.send_keys(Keys.ENTER).perform()
            n = len(word)
            sleep(n)
            try:
                driver.find_element(By.CLASS_NAME, "modal-congrats-body")
                input("solved! press any key to exit")
                driver.quit()
            except Exception:
                ...
        sleep(2)
        for _ in range(50):
            actions.send_keys(Keys.BACKSPACE).perform

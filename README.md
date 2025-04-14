# Letter Boxed Solver
This program uses Selenium to solve todays Letter Boxed by New York Times.  
In order to solve the daily Letter Boxed, the following actions must take place:
* Use the Selenium web driver to open the Letter Boxed page
* Figure out which letters there are and what sides they are on
* Read through all dictionary words that can be created on the Letter Boxed board
* Create chains of these words
* Attempt all chains that contian every letter until the board is solved.

## Use the Selenium web driver to open the Letter Boxed page
This step simply involves importing selenium, instantiating a webdriver and opening the the url for the daily Letter Boxed page.  
## Figure out which letters there are and what sides they are on
This is a bit more challenging than you probably think.  Becuase the main board is a `canvas` html element, you cannot simply target each letter in the board.  
Instead, I had to have selenium press each letter key, and then scrape the text-input to see if the letter appeared on the text.  If the letter appears in the text-input, that means it is on the board.   
After getting all 12 of the letters, I find which side each letter is on by entering two of the letters in a row.  If both letters appear in the text box, then that means there are on different sides.  If only the first letter appears, the letters are on the same side.  I build a map of the board using this technique.  
## Read through all dictionary words that can be created on the Letter Boxed board
First I filtered the words in my dictionary to only contain words that consist of the 12 letters on our board.  
I created a `dict` that maps each letter to a side.  If any word has two letters on the same side, it is discarded.
## Create chains of these words
All of the remaining words can be created with the Letter Boxed board.  
I create a `dict` that maps each letter to a list of all words that begin with that letter.  
I use this `dict` find all the words that start with the same letter as the last letter of the pervious word.  
Each chain is started using one of the remaining words.  Due to the innefficient nature of this algorithm, I can only create chains of three or fewer words.  This however, is not usually a problem because most Letter Boxed's can be solved using just two words.  
I then remove all chains that do not contian each letter at least once.  
## Attempt all chains that contian every letter until the board is solved.
Because I might have some words in my dictionary that do not exist in Letter Boxed's dictionary, I attempt to solve the board with each chain by iterating over each chain.

Aiden Sanghyeop Hyun
#260974945
 
import wordle_utils
 
 
 
 
WORDLE_WORD_LENGTH = 5 #(the length of the words in the game)
 
MAX_NUM_OF_GUESSES = 6 #(how many incorrect guesses the player is allowed to enter) 
 
CHAR_GREEN = '\x1b[6;30;42m'
 
CHAR_YELLOW = '\x1b[6;30;43m'
 
CHAR_GRAY = '\x1b[6;30;47m'
 
CHAR_END = '\x1b[0m'
 
def is_valid_word(word,list_word):
    
   
    ''' (str, list)-> bool
 
checks if the length of the word and whether it is in the given list.
 
>>> is_valid_word('about', ['abounds', 'abouts', 'above', 'aboveboard'])
 
False
 
>>> is_valid_word('coffee', ['beans', 'starbucks', 'water', 'latte', 'coffee'])
 
False
 
>>> is_valid_word('latte', ['beans', 'starbucks', 'water', 'latte', 'coffee'])
 
True'''
   
   #checks the length and membership
    if (len(word) != WORDLE_WORD_LENGTH) or (word not in list_word):
        
        return False
    
    else: 
         
        return True 
 
 
def print_string_list(list_word):
   
    '''(list)-> str, str, str, str, str
 
takes a list of strings and prints each string in the list on a new line.
 
>>> print_string_list(['beans', 'starbucks', 'water', 'latte', 'coffee'])
 
beans
starbucks
water
latte
coffee
 
>>> print_string_list(['abounds', 'about', 'abouts', 'aboveboard', 'abovedeck'])
 
abounds
about
abouts
aboveboard
abovedeck
 
>>> print_string_list(['headphones', 'airpods', 'iphones', 'macbook', 'mcgill'])
 
headphones
airpods
iphones
macbook
mcgill
 
'''
    for i in list_word:
        print(i)
 
def color_string(word,color):
    
    '''(str,str) -> (str)
 
takes two strings (word and color) and change the color of the string
and return it
 
>>> color_string('abc','black')
Invalid Color.
 
>>> color_string('abc','yellow')
'\x1b[6;30;43mabc\x1b[0m'
 
>>> a = color_string('abc','green')
 
>>> print(a)
abc
 
'''
    
    color_list = ['green', 'yellow', 'gray']
    
    #checks the color membership
    
    if color not in color_list:
        
        print('Invalid color.')
        
        return word
    
    #modify the string accordingly
    
    else:
        
        if color == 'green':
            
            return CHAR_GREEN+word+CHAR_END
        
        elif color == 'yellow':
            
            return CHAR_YELLOW+word+CHAR_END
        
        elif color == 'gray':
            
            return CHAR_GRAY+word+CHAR_END
    
            
            
 
def get_all_5_letter_words(word_list):
    
    '''(list) -> list
takes a list of strings and returns a list that has lengh of
global variable WORDLE_WORD_LENGTH
 
>>> get_all_5_letter_words(['abcde','12345'])
 
['abcde', '12345']
 
>>> get_all_5_letter_words(['abcde','12345','americano','computer','water'])
 
['abcde', '12345', 'water']
 
>>>get_all_5_letter_words(['abs', 'about', 'abouts', 'above', 'aboveboard', 'aloft'])
 
['about', 'above', 'aloft']
 
'''
    result = []
    
    for i in word_list:
        
        #put the words with the given length in a list
        
        if len(i) == WORDLE_WORD_LENGTH:
            
            result += [i]
    
    return result
 
 
 
def choose_mode_and_wordle(word_list):
    '''(list)-> str
 
takes a list of words. Let the user choose the player mode 
and return a random wordle from the list
 
 >>> choose_mode_and_wordle(['canada', 'america', 'mexico', 'mcgill','pepsi' ])
 
Enter the number of players: 2
 
***** Player 1's turn. ***** 
 
input the wordle.pepsi
 
***** Player 2's turn. ***** 
 
'pepsi'
 
>>> choose_mode_and_wordle(['canada', 'america', 'mexico', 'mcgill','pepsi' ])
Enter the number of players: canada
Wordle can be played with 1 or 2 players. Please only enter 1 or 2.
Enter the number of players: 1
'pepsi'
 
>>>  choose_mode_and_wordle(['about', 'above', 'aloft', 'aeons'])
Enter the number of players: 1
'above'
 
'''
    
    import random
    
    #infinite loop until the player enters the correct input
    
    while 1 == 1:
        
        mode = input("Enter the number of players: ")
        
        if mode=='1' or mode =='2':
        
           break
 
        else:
            
            print("Wordle can be played with 1 or 2 players. Please only enter 1 or 2.")
        
    #player one mode
    if mode == '1':
        
        list_len = len(word_list)
 
        random_index= random.randint(0,list_len-1)
 
        return (word_list[random_index])
    
    #player 2 mode
    if mode == '2':
        
        print("\n***** Player 1's turn. ***** \n")
        
        #asks the user to choose wordle
        
        wordle = input_wordle(word_list)
        
        print( "\n***** Player 2's turn. ***** \n")
        
        return wordle
    
def input_wordle(word_list):
    '''(list)-> str
asks a user for the wordle and checks the validity of the word
 
#no examples needed
'''
    
    #infinite loop until the word is valid
    
    while 1 ==1:
        
        wordle = wordle_utils.input_and_hide("Input today's word: ")
        
        wordle = wordle.lower()
        
        validity = is_valid_word(wordle,word_list)
        
        #if it is valid word break the loop
        if validity == True:
            break
        
        else:
            print('Not a valid word, please enter a new one.')
    
    return wordle
 
def generate_random_wordle(word_list):
    '''(list)-> str
it picks a random word from the word_list
 
>>> generate_random_wordle(['abcde','12345','americano','computer','water'])
'computer'
 
>>> generate_random_wordle(['abcde','12345','americano','computer','water'])
'12345'
 
>>> generate_random_wordle(['abcde','12345','americano','computer','water'])  
'americano'
 
'''
    
    import random
    
    len_word_list = len(word_list)
    
    #measure the length and picks a random index num
    
    random_index = random.randint(0,len_word_list-1)
    
    wordle = word_list [random_index]
    
    return wordle
 
def compare_and_color_word(guess, wordle):
    '''(str,str) -> str
it compares the two words and print out a colored wordle
based on correctness.
 
>>>  compare_and_color_word('mount', 'about')
 
'\x1b[6;30;47mm\x1b[0m\x1b[6;30;43mo\x1b[0m\x1b
[6;30;43mu\x1b[0m\x1b[6;30;47mn\x1b[0m\x1b[6;30;42mt\x1b[0m'
 
>>>  compare_and_color_word('unity', 'unite')
 
'\x1b[6;30;42mu\x1b[0m\x1b[6;30;42mn\x1b[0m\x1b[6;30;42mi\x1b
[0m\x1b[6;30;42mt\x1b[0m\x1b[6;30;47my\x1b[0m'
 
>>>  compare_and_color_word('color', 'collar')
 
'\x1b[6;30;42mc\x1b[0m\x1b[6;30;42mo\x1b[0m\x1b[6;30;42ml\x1b
[0m\x1b[6;30;43mo\x1b[0m\x1b[6;30;43mr\x1b[0m'''
    
    wordle_letters = []
    
    #put each character of wordle in a list
    
    for i in wordle:
        
        wordle_letters += [i]
    
    colored_wordle= ''    
        
    for i in range(WORDLE_WORD_LENGTH):
                
                #same index, same character
                if guess[i] == wordle[i]:
                    
                    colored_wordle += color_string(guess[i], 'green')
                
                #same character, different index
                elif guess[i] in wordle_letters:
                    
                    colored_wordle += color_string(guess[i], 'yellow')
                
                #none of the above
                else:
                    
                    colored_wordle += color_string(guess[i],'gray')
    
    return colored_wordle
 
def play_with_word(wordle,word_list):
    '''(str,list) - > int
 
asks the user to guess the wordle and print their guesses
with colors, after their guess enter the number of guesses
they used, if they used all without a correct guess, return it
with +1. 
 
>>> play_with_word('caper', ['cable', 'cater', 'crane', 'carve', 'caper', 'calls'])
Enter a guess:cater
cater
Enter a guess:invalid..word
Not a valid word, please enter a new one.
Enter a guess:carve
cater
carve
Enter a guess:caper
cater
carve
caper
3
 
play_with_word('count', ['mount', 'pound', 'tooth', 'carve', 'kites', 'calls'])
Enter a guess:mount
mount
Enter a guess:pound
mount
pound
Enter a guess:tooth
mount
pound
tooth
Enter a guess:count
mount
pound
tooth
count
4
 
>>> play_with_word('count', ['mount', 'pound', 'tooth', 'carve', 'kites', 'calls'])
Enter a guess:karve
Not a valid word, please enter a new one.
Enter a guess:carve
carve
Enter a guess:pount
Not a valid word, please enter a new one.
Enter a guess:tooth
carve
tooth
Enter a guess:pound
carve
tooth
pound
Enter a guess:calls
carve
tooth
pound
calls
Enter a guess:kites
carve
tooth
pound
calls
kites
Enter a guess:kites
carve
tooth
pound
calls
kites
kites
7
 
'''
 
    count = 0
    
    guess_letters = []
    
    colored_wordle = ''
        
    while count  < MAX_NUM_OF_GUESSES:
        
        #counts one before getting the answer from the player
        
        count += 1
        
        #asks user for a guess
        
        guess = input('Enter a guess:')
        
        guess = guess.lower()
        
        #if they got the answer, break the loop
        if guess == wordle:
            
            break
        
        #if they did not get the answer,
        else:
                
                #check if it was a valid word
                valid_word = is_valid_word(guess,word_list)
                
                #if it was invalid
                
                if valid_word == False:
                        
                    print('Not a valid word, please enter a new one.')
                    
                    #cancel counting an invalid answer as a guess
                    count -= 1
                
                # if it was valid
                if valid_word == True: 
                    
                    #add a new line character if it is the second and after
                    if colored_wordle != '':
                        
                        colored_wordle += '\n'
                    
                    #generate the colored string and add it to colored_wordle
                    colored_wordle += compare_and_color_word(guess, wordle)
                        
                    print(colored_wordle)
    
    #when the player failed add one to the count
    if guess != wordle:
         
         count +=1
    
    #if they correctly guessed, generate green colored string
    elif guess == wordle:
        
        if colored_wordle != '':
                
                colored_wordle += '\n'
        
        colored_wordle += compare_and_color_word(guess, wordle)
                
        print(colored_wordle)
    
    return count
 
 
 
def print_final_message(count, wordle):
    '''(int,str)-> str
 
prints the number of guesses and whether they
won or lost
 
>>> print_final_message(1,'count')
You won! It took you 1 guess.
 
>>> print_final_message(5,'count')
You won! It took you 5 guesses.
 
>>> print_final_message(7,'count')
You lost! The word was count
 
'''
    if count == 1:
        
        print("You won! It took you 1 guess.")
    
    elif count <= MAX_NUM_OF_GUESSES:
        
        print("You won! It took you", str(count), 'guesses.')
    
    elif count == MAX_NUM_OF_GUESSES+1:
        
        lost = color_string(wordle,'green')
        
        print("You lost! The word was",lost)
    
    
def play(word_list):
    '''(list) - > none
asks the user to choose the mode and wordle
play the game and check how many guess they took
to win or lose and print it with a message.
 
#example not needed'''
 
    wordle = choose_mode_and_wordle(word_list)
    
    count = play_with_word(wordle,word_list)
    
    print_final_message(count, wordle)
    
def main():
    '''() -> None
list all the words and recollect the wordle length words
in another list, and call the function, play.
 
#example not needed'''
    
    word_list = wordle_utils.load_words()
    
    word_list = get_all_5_letter_words(word_list)
    
    play(word_list)
    
    
 

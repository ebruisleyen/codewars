# Complete the function that takes a non-negative integer n as input, and returns a list of all the powers of 2 with the exponent ranging from 0 to n ( inclusive ).

# Examples
# n = 0  ==> [1]        # [2^0]
# n = 1  ==> [1, 2]     # [2^0, 2^1]
# n = 2  ==> [1, 2, 4]  # [2^0, 2^1, 2^2]




def powers_of_two(n):
    lis=[]
    
    for i in range(n+1):
        
        lis.append(2**i)
        
    return lis



# Let's play! You have to return which player won! In case of a draw return Draw!.

# Examples(Input1, Input2 --> Output):

# "scissors", "paper" --> "Player 1 won!"
# "scissors", "rock" --> "Player 2 won!"
# "paper", "paper" --> "Draw!"
def rps(p1, p2):
   
    if p1==p2:
        return "Draw!"
    elif p1=="scissors" and p2=="paper":
        return "Player 1 won!"
    elif p1=="rock" and p2=="scissors":
        return "Player 1 won!"
    elif p1=="rock" and  p2=="paper":
        return "Player 1 won!"
    else:
        return "Player 2 won!"
    

#   Write a function that checks if a given string (case insensitive) is a palindrome. A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards, such as madam or racecar, the date and time 12/21/33 12:21, and the sentence: "A man, a plan, a canal – Panama".  


def is_palindrome(s):
    slm = s.lower()
    reversed_word = slm[::-1]
    if slm == reversed_word:
        return True
    else:
        return False
#     You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.

# Array can contain numbers or strings. X can be either.

# Return true if the array contains the value, false if not.


def check(seq, elem):
    if elem in seq:
        return True
    else:
        return False
   
#      Create a function that accepts a string and a single character, and returns an integer of the count of occurrences the 2nd argument is found in the first one.

# If no occurrences can be found, a count of 0 should be returned.

# ("Hello", "o")  ==>  1
# ("Hello", "l")  ==>  2
# ("", "z")       ==>  0
# str_count("Hello", 'o'); // returns 1
# str_count("Hello", 'l'); // returns 2
# str_count("", 'z'); // returns 0
# Notes
# The first argument can be an empty string
# In languages with no distinct character data type, the second argument will be a string of length 1



def str_count(strng, letter):
    count=0
    for  x in strng:
        if x==letter:
            count+=1
    return count
#  You take your son to the forest to see the monkeys. You know that there are a certain number there (n), but your son is too young to just appreciate the full number, he has to start counting them from 1.

# As a good parent, you will sit and count with him. Given the number (n), populate an array with all numbers up to and including that number, but excluding zero.

# For example(Input --> Output):

# 10 --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#  1 --> [1]
def monkey_counts(n):
 
 return list(range(1,n+1))

# Create a function that gives a personalized greeting. This function takes two parameters: name and owner.

# Use conditionals to return the proper message:

# case	return
# name equals owner	'Hello boss'
# otherwise	'Hello guest'
def greet(name, owner):
    if name==owner:
        return 'Hello boss'
    else:
        return 'Hello guest'
#     0-9 arasında bir sayı verildiğinde, onu kelimelerle döndürün.

# Giriş :: 1

# Çıktı :: "Bir".

# Diliniz destekliyorsa, bir switch deyimi kullanmayı deneyin .

def sayiyi_kelimeye_donustur(sayi):
    if sayi == 0:
        return "Sıfır"
    elif sayi == 1:
        return "Bir"
    elif sayi == 2:
        return "İki"
    elif sayi == 3:
        return "Üç"
    elif sayi == 4:
        return "Dört"
    elif sayi == 5:
        return "Beş"
    elif sayi == 6:
        return "Altı"
    elif sayi == 7:
        return "Yedi"
    elif sayi == 8:
        return "Sekiz"
    elif sayi == 9:
        return "Dokuz"
    else:
        return "Geçersiz sayı!"



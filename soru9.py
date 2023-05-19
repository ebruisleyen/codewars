# Trolls are attacking your comment section!

# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

# Your task is to write a function that takes a string and return a new string with all vowels removed.

# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

# Note: for this kata y isn't considered a vowel.
def disemvowel(string_):
    sesli_harf="aeıuioAEIOU"
    list=""
    for i in string_:
        if i not in sesli_harf:
            list+=i
    return list
# Create a function that checks if a number n is divisible by two numbers x AND y. All inputs are positive, non-zero numbers.

# Examples:
# 1) n =   3, x = 1, y = 3 =>  true because   3 is divisible by 1 and 3
# 2) n =  12, x = 2, y = 6 =>  true because  12 is divisible by 2 and 6
# 3) n = 100, x = 5, y = 3 => false because 100 is not divisible by 3
# 4) n =  12, x = 7, y = 5 => false because  12 is neither divisible by 7 nor 5


def is_divisible(n,x,y):
    if n % x ==0 and n % y ==0:
        return True
    else:
        return False
#     Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

# Note: a and b are not ordered!

# Examples (a, b) --> output (explanation)
# (1, 0) --> 1 (1 + 0 = 1)
# (1, 2) --> 3 (1 + 2 = 3)
# (0, 1) --> 1 (0 + 1 = 1)
# (1, 1) --> 1 (1 since both are same)
# (-1, 0) --> -1 (-1 + 0 = -1)
# (-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)
# Your function should only return a number, not the explanation about how you get that number.

def get_sum(a,b):
    if a==b:
        return a
    elif a<b:
        return sum(range(a,b+1))
    else:
        return sum(range(b,a+1))
#  Ardışık tek sayılar üçgeni verildiğinde:

#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...
# Bu üçgenin n . satırındaki sayıların toplamını hesaplayın (1. indeksten başlayarak) örneğin: ( Giriş --> Çıkış )

# 1 -->  1
# 2 --> 3 + 5 = 8   

def row_sum_odd_numbers(n):
    ilk_sayi = n * (n - 1) + 1
    toplam = n * (ilk_sayi + ilk_sayi + 2 * (n - 1)) // 2
    return toplam
# Nathan loves cycling.

# Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

# You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.

# For example:

# time = 3 ----> litres = 1

# time = 6.7---> litres = 3

# time = 11.8--> litres = 5
def litres(time):
    return int(time*0.5)



# A hero is on his way to the castle to complete his mission. However, he's been told that the castle is surrounded with a couple of powerful dragons! each dragon takes 2 bullets to be defeated, our hero has no idea how many bullets he should carry.. Assuming he's gonna grab a specific given number of bullets and move forward to fight another specific given number of dragons, will he survive?

# Return true if yes, false otherwise :)
def hero(bullets, dragons):
    if dragons * 2 <= bullets:
        return True
    else:
        return False
#   After a hard quarter in the office you decide to get some rest on a vacation. So you will book a flight for you and your girlfriend and try to leave all the mess behind you.

# You will need a rental car in order for you to get around in your vacation. The manager of the car rental makes you some good offers.

# Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total. Alternatively, if you rent the car for 3 or more days, you get $20 off your total.

# Write a code that gives out the total amount for different days(d).
def rental_car_cost(d):
   
    if d>=7:
        return  40*d -50
    elif d>=3:
        
        return 40 * d - 20
    else:
        return 40 *d
    



# This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.

def simple_multiplication(number) :
    if number%2==0:
        return number * 8
    else:
        return number * 9
    

# We need a function that can transform a number (integer) into a string.

# What ways of achieving this do you know?
def number_to_string(num):
    return str(num)


# Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.

# Examples (input -> output)
# 6, "I"     -> "IIIIII"
# 5, "Hello" -> "HelloHelloHelloHelloHello"
def repeat_str(repeat, string):
    
    return repeat * string



# You are given two interior angles (in degrees) of a triangle.

# Write a function to return the 3rd.

# Note: only positive integers will be tested.

# https://en.wikipedia.org/wiki/Triangle
def other_angle(a, b):
    return 180 - a - b
# Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

# Write a function which takes a list of strings and returns each line prepended by the correct number.

# The numbering starts at 1. The format is n: string. Notice the colon and space in between.

# Examples: (Input --> Output)

# [] --> []
# ["a", "b", "c"] --> ["1: a", "2: b", "3: c"]
def number(lines):
    
    numbered_list = []
    for i, s in zip(range(1, len(lines)+1), lines):
        numbered_list.append(f"{i}: {s}")
    return numbered_list
# Hamamböceği en hızlı böceklerden biridir. Hızını km/saat cinsinden alan ve bunu tamsayıya (= taban) yuvarlatılmış olarak cm/saniye cinsinden döndüren bir fonksiyon yazın.

# Örneğin:

# 1.08 --> 30
# Not! Giriş bir Gerçek sayıdır (gerçek tür dile bağlıdır) ve >= 0'dır. Sonuç bir Tamsayı olmalıdır.

def cockroach_speed(s):
   
#       return int(s * 1000/36)
# 3 a, b, c tamsayı değerini kabul eden bir işlev gerçekleştirin. İşlev, kenarları verilen uzunlukta bir üçgen oluşturulabiliyorsa doğru, diğer durumlarda yanlış olarak dönmelidir.

# (Bu durumda, kabul edilmesi için tüm üçgenlerin yüzeyi 0'dan büyük olmalıdır).



def is_triangle(a, b, c):
    if a>0 and b>0 and c>0:
        if a + b > c and a + c > b and b + c > a:
            return True
        else:
            return False
    else:
        
        return False





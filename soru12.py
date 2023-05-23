# In this simple exercise, you will create a program that will take two lists of integers, a and b. Each list will consist of 3 positive integers above 0, representing the dimensions of cuboids a and b. You must find the difference of the cuboids' volumes regardless of which is bigger.

# For example, if the parameters passed are ([2, 2, 3], [5, 4, 1]), the volume of a is 12 and the volume of b is 20. Therefore, the function should return 8.

# Your function will be tested with pre-made examples as well as random ones.

# If you can, try writing it in one line of code.


def find_difference(a, b):
    list1 = 1
    list2 = 1
    for num in a:
        list1 *=num
    for i in b:
        list2*=i
    return abs(list1 -list2)


# This function should test if the factor is a factor of base.

# Return true if it is a factor or false if it is not.

# About factors
# Factors are numbers you can multiply together to get another number.

# 2 and 3 are factors of 6 because: 2 * 3 = 6

# You can find a factor by dividing numbers. If the remainder is 0 then the number is a factor.
# You can use the mod operator (%) in most languages to check for a remainder
# For example 2 is not a factor of 7 because: 7 % 2 = 1

# Note: base is a non-negative number, factor is a positive number.
def check_for_factor(base, factor):
    
    if base % factor ==0:
        
        return True
    else:
                
        return False
            
# The starship Enterprise has run into some problem when creating a program to greet everyone as they come aboard. It is your job to fix the code and get the program working again!

# Example output:

# Hello, Mr. Spock    
def say_hello(name):
    
    return "Hello," +" "+ name    
        
    
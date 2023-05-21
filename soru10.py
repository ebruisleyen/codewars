# İki parametre alan setAlarm adlı bir işlev yazın. İstihdam edilen ilk parametre, çalıştığınız her zaman doğrudur ve ikinci parametre olan tatil , tatilde olduğunuz her zaman doğrudur.

# İşlev, tatilde değil de çalışıyorsanız doğru olarak dönmelidir (çünkü bunlar bir alarm kurmanız gereken durumlardır). Aksi takdirde false döndürmelidir. Örnekler:

# setAlarm(true, true) -> false
# setAlarm(false, true) -> false
# setAlarm(false, false) -> false
# setAlarm(true, false) -> true

def set_alarm(employed, vacation):
    if employed == True and vacation == True:
        return False
    elif employed == False and vacation == True:
        return False
    elif employed == False and vacation == False:
        return False
    else:
        return True
#     Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "
def double_char(s):
    tekrarlanan =""
    for karakter in s:
        tekrarlanan += karakter *2
    return tekrarlanan
# Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

# Example:
# ["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]

# None of the arrays will be empty, so you don't have to worry about that!
def remove_every_other(my_list):
    list =[]
    for indeks,eleman in enumerate(my_list):
        if indeks % 2 == 0:
            list.append(eleman)
    return list



# In this kata you get the start number and the end number of a region and should return the count of all numbers except numbers with a 5 in it. The start and the end number are both inclusive!

# Examples:

# 1,9 -> 1,2,3,4,6,7,8,9 -> Result 8
# 4,17 -> 4,6,7,8,9,10,11,12,13,14,16,17 -> Result 12
# The result may contain fives. ;-)
# The start number will always be smaller than the end number. Both numbers can be also negative!

# I'm very curious for your solutions and the way you solve it. Maybe someone of you will find an easy pure mathematics solution.

# Have fun coding it and please don't forget to vote and rank this kata! :-)

# I have also created other katas. Take a look if you enjoyed this kata!   


def dont_give_me_five(start,end):
    sayac=0
    for sayi in range(start,end+1):
        if "5" not in str(sayi):
            sayac+=1
    return sayac
            
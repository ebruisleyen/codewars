# Given an array of integers, return a new array with each value doubled.

# For example:

# [1, 2, 3] --> [2, 4, 6]
def maps(a):
    lis=[]
    for i in a:
        lis.append(i*2)
    return lis


# Ben'in biraz kar elde etmek için çok basit bir fikri var: Bir şey alıyor ve tekrar satıyor. Tabii ki, sadece aynı fiyattan alıp satarsa, bu ona hiçbir kazanç sağlamaz. Bunun yerine, onu mümkün olan en düşük fiyattan alacak ve en yüksek fiyattan satacak.

# Görev
# Verilen listenin/dizinin hem minimum hem de maksimum sayısını döndüren bir işlev yazın.

# Örnekler (Giriş --> Çıkış)
# [1,2,3,4,5] --> [1,5]
# [2334454,5] --> [5,2334454]
# [1]         --> [1,1]
def min_max(lst):
    liste=[]
    sortd=sorted(lst)
    min=sortd[0]
   
    
    liste.append(min)
    
    max=sortd[-1]
    liste.append(max)
    return liste


# Deoksiribonükleik asit (DNA), hücrelerin çekirdeğinde bulunan ve canlı organizmaların gelişimi ve işleyişi için "talimatlar" taşıyan bir kimyasaldır.

# Daha fazlasını öğrenmek istiyorsanız: http://en.wikipedia.org/wiki/DNA

# DNA dizilerinde "A" ve "T" sembolleri "C" ve "G" gibi birbirinin tamamlayıcısıdır. İşleviniz DNA'nın bir tarafını alır (sicim, Haskell hariç); diğer tamamlayıcı tarafı iade etmeniz gerekiyor. DNA sarmalı asla boş değildir veya hiç DNA yoktur (yine Haskell hariç).

# Daha fazla benzer alıştırma şu adreste bulunabilir: http://rosalind.info/problems/list-view/ (kaynak)

# Örnek: ( giriş --> çıkış )

# "ATTGC" --> "TAACG"
# "GTAT" --> "CATA"
def DNA_strand(dna):
    liste= ""
    for i in dna:
        if i =="A":
            liste += "T"
        elif i=="T":
            liste+="A"
        elif i=="G":
            liste+="C"
        else:
             liste+="G"
    return liste
# Terminal game move function
# In this game, the hero moves from left to right. The player rolls the dice and moves the number of spaces indicated by the dice two times.

# Create a function for the terminal game that takes the current position of the hero and the roll (1-6) and return the new position.

# Example:
# move(3, 6) should equal 15
def move(position, roll):
    return position + (roll*2)
 
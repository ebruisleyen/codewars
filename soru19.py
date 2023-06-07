# Belirli bir dizeden tüm ünlem işaretlerini kaldıran RemoveExclamationMarks işlevini yazın.
def remove_exclamation_marks(s):
    return s.replace("!","")
# Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
def grow(arr):
    i =1
    for k in arr:
        i*=k
    return i
# Messi üç ligde gol atan bir futbolcu:

# La Liga
# Kral Kupası
# Şampiyonlar
# Üç ligdeki toplam gol sayısını döndürmek için işlevi tamamlayın.

# Not: giriş her zaman geçerli olacaktır.

# Örneğin:

# 5, 10, 2  -->  17   
def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague
# Büyük şehirde bonus zamanı! Şişkolar beklenti içinde patilerini ovuşturuyor... ama en çok parayı kim kazanacak?

# İki bağımsız değişken (maaş, ikramiye) alan bir işlev oluşturun. Maaş bir tamsayı ve bonus bir boole olacaktır.

# Bonus doğru ise maaş 10 ile çarpılmalıdır. Bonus yanlış ise fatcat yeterli parayı kazanmamıştır ve sadece belirtilen maaşını almalıdır.

# Kişinin alacağı toplam rakamı "£" (= "\u00A3", JS, Go, Java, Scala ve Julia), "$" (C#, C++, Ruby, Clojure, Elixir, PHP, Python, Haskell) ile başlayan bir dize olarak döndürün , ve Lua) veya "¥" (Pas).

def bonus_time(salary, bonus):
    if bonus == True:
        return "$" + str(salary * 10)
    else:
        return  "$" + str(salary)

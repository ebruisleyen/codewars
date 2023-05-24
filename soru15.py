# sually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

# Your task is to write a function maskify, which changes all but the last four characters into '#'.



def maskify(cc):
    if len(cc)<=4:
        return cc
    else:
         return "#" * (len(cc) - 4) + cc[-4:]
    
   Size bir kelime verilecek. İşiniz kelimenin orta karakterini döndürmektir. Kelimenin uzunluğu tek ise, ortadaki karakteri döndürün. Kelimenin uzunluğu çift ise, ortadaki 2 karakteri döndürün.

#Örnekler:

# Kata.getMiddle("test") should return "es"

# Kata.getMiddle("testing") should return "t"

# Kata.getMiddle("middle") should return "dd"

# Kata.getMiddle("A") should return "A"
# #Giriş

# Uzunlukta bir kelime (dize) 0 < str < 1000(Javascript'te, test durumlarındaki bir hata nedeniyle bazı test durumlarında 1000'den biraz fazla alabilirsiniz). Bunun için test yapmanıza gerek yoktur. Bu, yalnızca çözümünüzün zaman aşımına uğraması konusunda endişelenmenize gerek olmadığını söylemek için burada.

# #Çıktı

# Bir dize olarak temsil edilen kelimenin orta karakter(ler)i.

def get_middle(s):
    

    length = len(s)
    middle_index = length // 2

    if length % 2 == 0:
        return s[middle_index - 1 : middle_index + 1]
    else:
        return s[middle_index : middle_index + 1]



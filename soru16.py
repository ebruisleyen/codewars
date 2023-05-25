# Kodlamada yeniyim ve şimdi iki dizinin toplamını almak istiyorum... Aslında tüm elemanlarının toplamı. Yardımın için minnettar olacağım.

# Not: Her dizi yalnızca tamsayı sayıları içerir. Çıktı da bir sayıdır.

def array_plus_array(arr1,arr2):
    return sum(arr1) + sum(arr2)


# Will Smith'in oğlu Jaden Smith, The Karate Kid (2010) ve After Earth (2013) gibi filmlerin yıldızıdır. Jaden, Twitter aracılığıyla sunduğu bazı felsefeleriyle de tanınır . Twitter'da yazarken, neredeyse her kelimeyi büyük harfle yazmasıyla tanınır. Basit olması için, her kelimeyi büyük harfle yazmanız gerekecek, aşağıdaki örnekte kısaltmaların nasıl olması beklendiğini kontrol edin.

# Göreviniz, dizeleri Jaden Smith tarafından yazılacakları şekle dönüştürmektir. Dizeler, Jaden Smith'ten gerçek alıntılardır, ancak orijinal olarak yazdığı şekilde büyük harfle yazılmazlar.

# Örnek:

# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"
# Jaden'in eski Twitter hesabına @officialjaden ile archive.org üzerinden bağlantı
def to_jaden_case(string):

        
        return " ".join(word.capitalize() for word in string.split())

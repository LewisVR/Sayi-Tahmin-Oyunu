from random import randint

rand = randint(1, 100)
sayac = 0

while True:
    sayac += 1
    sayi=input("1 ile 100 arasında değer girin (q çıkış):")
    if(sayi=="q"):
        print("Çıkış yapıldı")
        break
    else:
        sayi = int(sayi)
    if sayi < rand:
        print("Daha Yüksek Bir Sayı Girin.")
        continue
    elif sayi > rand:
        print("Daha Düşük Bir Sayı Girin.")
        continue
    else:
        print("Bildiiniz!! Say: {0}".format(rand))
        print("Tahmin sayınız {0}".format(sayac))
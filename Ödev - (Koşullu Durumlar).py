#Problem 1#

kilo = int(input("Kilonuzu giriniz: "))
boy = float(input("Boyunuzu giriniz: "))
BKİ = kilo / boy**2

if BKİ < 18.5:
    print("Beden kitle indeksiniz: {} (zayıf)".format(BKİ))
elif BKİ < 25:
    print("Beden kitle indeksiniz: {} (normal)".format(BKİ))
elif BKİ < 30:
    print("Beden kitle indeksiniz: {} (fazla kilolu)".format(BKİ))
else:
    print("Beden kitle indeksiniz: {} (obez)".format(BKİ))

#Problem 2#

a = float(input("Birinci sayıyı giriniz: "))
b = float(input("İkinci sayıyı giriniz: "))
c = float(input("Üçüncü sayıyı giriniz: "))

print(max(a,b,c))

#Problem 3#

x = int(input("İlk vize notunuzu giriniz: "))
y = int(input("İkinci vize notunuzu giriniz: "))
z = int(input("Final notunuzu giriniz: "))

toplam_not = 0.3*x + 0.3*y + 0.4*z

if toplam_not >=90:
    print("AA")
elif toplam_not >= 85:
    print("BA")
elif toplam_not >= 80:
    print("BB")
elif toplam_not >= 75:
    print("CB")
elif toplam_not >= 70:
    print("CC")
elif toplam_not >= 65:
    print("DC")
elif toplam_not >= 60:
    print("DD")
elif toplam_not >= 55:
    print ("FD")
else:
    print("FF")

#Problem 4#

tip = input("Lütfen şeklin tipini giriniz: ")

if tip == "Dörtgen":
    print("Dörtgenin kenarlarını giriniz: ")
    d = int(input("Kenar-1:"))
    e = int(input("Kenar-2:"))
    f = int(input("Kenar-3:"))
    g = int(input("Kenar-4:"))

    if d == e and d == f and d == g:
        print("Kare")
    elif a == c and b == d:
        print("Dikdörtgen")
    else:
        print("Dörtgen")

elif tip == "Üçgen":
    print("Üçgenin kenarlarını giriniz: ")
    h = int(input("Kenar-1:"))
    j = int(input("Kenar-2:"))
    k = int(input("Kenar-3:"))

    if abs(h+j) > k and abs(h+k) > j and abs(j+k) > h:
        if h == j and h == k:
            print("Eşkenar üçgen")
        elif (h == j and h != k) or (h == k and h != j) or (j == k and j != k):
            print("İkizkenar üçgen")
        else:
            print("Çeşitkenar üçgen")
    else:
        print("Üçgen belirtmiyor")

else:
    print("Geçersiz şekil")
import random
karaketerler = '+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
uzunluk = int(input("parolanın uzunluğu:"))
parola = ''
for i in range(uzunluk):
    parola += random.choice(karaketerler)
print(parola)

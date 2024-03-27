#Vize-Final Ortalama Hesaplama

"""
 Puan          Harf Notu                   Durumu
90-100           AA                       Başarılı
85-89            BA                       Başarılı
80-84            BB                       Başarılı
70-79            CB                       Başarılı
60-69            CC                       Başarılı
50-59            DC                       Başarısız
40-49            DD                       Başarısız
0-40             FF                       Başarısız
"""

vize=int(input("Vize notunuzu giriniz:"))
final=int(input("Final notunuzu giriniz:"))
ort=(vize*0.4)+(final*0.6)
print("Ortalama=",ort)

if(90<=ort<=100):
    print("AA aldınız.\nDurum:Başarılı")
elif(85<=ort<=89.9):
    print("BA aldınız.\nDurum:Başarılı")
elif(80<=ort<=84.9):
    print("BB aldınız.\nDurum:Başarılı")
elif(70<=ort<=79.9):
    print("CB aldınız.\nDurum:Başarılı")
elif(60<=ort<=69.9):
    print("CC aldınız.\nDurum:Başarılı")
elif(50<=ort<=59.9):
    print("DC aldınız.\nDurum:Başarısız")
elif(40<=ort<=49.9):
    print("DD aldınız.\nDurum:Başarısız")
else:
    print("FF aldınız.\nDurum:Başarısız")

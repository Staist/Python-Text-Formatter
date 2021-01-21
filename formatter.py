dosyaadi = input("Dosya adı giriniz: ")
dosyaadi = str(dosyaadi + ".txt")

with open(dosyaadi, 'r') as file :
  dosyaicerigi = file.read()

silinecek = str(input("Silinecek yazıyı giriniz: "))
dosyaicerigi = dosyaicerigi.replace(silinecek, '')

with open(dosyaadi, 'w') as file:
  file.write(dosyaicerigi)
  file.close()
  print("-" * 30)
  print("İşlem başarılı!")
  print("-" * 30)
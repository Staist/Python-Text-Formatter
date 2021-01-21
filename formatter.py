dosyaadi = input("Enter file name: ")
dosyaadi = str(dosyaadi + ".txt")

with open(dosyaadi, 'r') as file :
  dosyaicerigi = file.read()

silinecek = str(input("Enter the text that you wish to delete: "))
dosyaicerigi = dosyaicerigi.replace(silinecek, '')

with open(dosyaadi, 'w') as file:
  file.write(dosyaicerigi)
  file.close()
  print("-" * 30)
  print("Successfully deleted!")
  print("-" * 30)

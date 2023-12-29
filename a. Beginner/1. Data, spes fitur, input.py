# Tipe Data / Variable 
# string (str) gowo sembarang tanda kutip
jengen_awal = 'Hilmy'
jengen_akhir = 'Zaini'
jengen_lengkap= jengen_awal + ' '+jengen_akhir
print ('Aku '+jengen_lengkap)
# print (type (jengen_awal)) > ngeprin tipe data

# integer (int) data angka
umur = 16
umur += 1 #seng dieksekusi seng ngisor
print('Umurku ' + str(umur))

# float > data desimal
duwur = 147.5
print ('Duwurku '+str(duwur)+'cm')

# boolean (bool) True / False
wong = True
print('Aku uwong: '+str(wong) )

print('-------------------------------')

# Multiple Assignment 
#bedo value-ne
negara , provinsi , maju = 'Indonesia' , 34 , False
print(negara)
print(provinsi)
print(maju)
#podo value-ne
kudus = jepara = solo = 'kota'
print(kudus)
print(jepara)
print(solo)

print('-------------------------------')

#Useful Fitur (kusus string)
nama='Hilmy Zaini'
desa='medini'
gang = '06'
print(len(nama))
print(nama.find('a')) #mulai 0, spasi diitung
print(desa.capitalize ())
print(desa.upper())
print(nama.lower())
print(gang.isdigit()) #angka biasa gk desimal
print(desa.isalpha()) #alfabet tanpa spasi
print(nama.count ('i'))
print(desa.replace ('i' , 'o'))
print(nama*3)

print('-------------------------------')

#Ngubah Tipe Data
a= 'anj' #str
b= 3.5 #float
x= 4 #int
y= 3.0 #float
z= '2'#str

x= float(x)
z= int(z)

# print(4 + int(a)) > str gk iso int di disi'i
print('z = '+ str(z))
print(5 + b) #float mbi str iso digabung
print(x/2.2) #float
print(int(y)) #int
print(z*4) #int

print('-------------------------------')

# Input + materi durunge

# BMI Calc tak edit 24/12/23
print('Standar Abot Awak')
jeneng = input('Sopo jengenem? ')
bb = float(input('Pirang kilo bobotem? '))
dhuwur = float(input('Pirang senti dhuwurem? '))
bmi= bb/(dhuwur/100)**2 #niron google 

if bmi > 15 and bmi <18.5 :
  print ('Kurang gizi kuwe ' +jeneng)
elif bmi >=18.5 and bmi <25:
  print ('Normal bobotem ' +jeneng)
elif bmi >=25 and bmi <30:
  print('Kabotan awak kuwe ' +jeneng)
elif bmi>=30 and bmi <45:
  print("Waduh.. obesitas kuwe " +jeneng)
else:
  print ('Wess.. ora uwong iki')
# print('Oi ' + jeneng.capitalize())
# print('Bobotem ' + str(bb)+ ' kilo temune')
# print('Dhuwurem '+ str(dhuwur)+ ' senti jebule' )
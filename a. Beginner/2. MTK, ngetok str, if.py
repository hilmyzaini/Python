# MaTematiKa/
import math #> kudune nganggo kuwi

anj= 3.3
bbi= -2
clg= 4

print(round(anj)) #bulatno
print(math.ceil(anj)) #bulatno duwur
print(math.floor(anj)) #bulatno ngisor
print(abs(bbi))
print(pow(bbi,3)) #pangkat
print(math.sqrt(clg)) #akar, dadi float
print(min(anj,bbi,clg))
print(max(anj,bbi,clg))

print('-------------------------------')

#Ngetok string
#indexing[start:stop:step] > start awet0 , liyane awet1
jengen ='Hilmy Zaini'
start= jengen[3] #mulaine, mek 1 tok nk liyane gk ditulis
stop= jengen[:10] #mandek tekan< , start-e nk gk diisi, ditulis kawet seng awal
step = jengen[::3] #blenjat/maju <langkah , awalane ditulis , stop-e nk gk diisi dianggep gk ono akhire
kualik = jengen[::-1] #diwalek nk isine min(-) , seng iso - cumak step

print(start)
print(stop)
print(step)
print(kualik)
print(jengen[3:8:2])

#slice() 
alfabet='abcdefghijklmnopqrstuvwxyz'
#w1='https://google.com/'
#w2='https://wikipedia.com/'

#slice = slice(8,-5) #nge'i nilai slice
alf_aw= alfabet[slice(5)] #dijipuk sg awal
alf_ak= alfabet[slice(-4)] #diketok sg akhir
alf_cmp= alfabet[slice(2,-5)] #diketok aw n ak
#print(w1[slice]) #hasile "google"
#print(w2[slice]) #hasile "wikipedia"
print(alf_aw)
print(alf_ak)
print(alf_cmp)
print(alfabet[slice(10,20)]) #diketok 10 sg awal, ditulis ngasi 20 sg awal

print('-------------------------------')

#if Statement & Logical Operator

# = = auto dadi == sama dengan
# ! = auto dadi != tidak sama dengan
#  > lebih dari
#  < kurang dari
#  > = auto dadi >= lebih dari sama dengan
#  < = auto dadi <= kurang dari sama dengan
#  operator:  and , or , not
#Dieksekusi kawet duwur, nk gk ono ngisore..., ngasi else

print('Jenis-jenis umur')
umur = int(input('Umur piro? '))

if umur < 0 and umur > -5:
  print('Ijeh ndok weteng')
elif umur >=0 and umur <=2:
  print('Bayi')
elif not(umur <3 or umur >8):
  print('Cah cilik')
elif umur == 16:
  print('Umure Hilmy, Cah nom')
elif umur >=9 and umur <=20:
  print('Cah nom')
elif umur >=21 and umur <= 50:
  print('Wong gede')
elif umur >=51 and umur <=80:
  print('Wong tuwo')
elif umur >=81 and umur <=120:
  print('Semestine wes mati')
else :
  print('Ora wong')
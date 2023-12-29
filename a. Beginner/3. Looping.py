import time #import module kudune paling dhuwur
import datetime
# Unli Loop

# while 6==6:
#   print('Ngelag Woooiii...')

ketik = None
while not ketik :
  ketik = input ('Ketik angger: ')
print ('Lanjut 👇')

print('-------------------------------')

# Limited Loop
for a in range(1+2): #awet0
  print(a-3)
print('---------')
# Gowo indexing tapi , gk :
for b in range(8,60,10):
  print(b+3)
print('---------')
# Gowo string
for c in 'Hilmy':
  print(c)
print('---------')
#Itung Mundur
detik= int(input('Timer, pirang detik? '))
for d in range(detik,0,-1):
  print (d)
  time.sleep(0.9)
  
print('-------------------------------')

#Nested Loop
print ('Wajik Aneh')
dowu= int(input('Sepiro gedhene? '))
isi= input('Opo isine? ')
for m in range(dowu):
  for n in range(dowu-m):
    print('  ' , end='')
  for o in range(2*m+1):
    print(isi , end='')
  print('')

print ('-------------------------------')

# Kontrol Loop

# #Break: ngendekno
current_date = datetime.datetime.now()
tanggal = current_date.day
while True:
  tgl= int(input('Tanggal piro iki? '))
  if tgl == tanggal:
    break
  print('Salah!')
print('Bener!')
print('---------')

# Continue: blenjati value sg diisi
no_hp = '0857-7385-8842'
for e in no_hp:
  if e == '-':
    continue
  print(e , end='')
print('')
print('---------')

# Pass: ngilangno value sg diisi
for f in range(1,6):
  if f == 3:
    pass
  else:
    print(f , end='')
print('')
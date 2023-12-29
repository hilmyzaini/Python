# List
HP=['Xiaomi','Samsung','Asus','Oppo']
#HP[0]='Vivo'
HP.append('Nokia') #nambahno nilai terakhir
HP.remove('Asus')
HP.pop() #busak nilai terakhir
HP.insert(1,'Ipong') #nylempitno nilai
HP.sort() #urut abjad
#HP.clear() #busak kabeh
#print(HP[0]) #exclusive 

for a in HP:
  print(a)

print('-------------------------------')

#Lists in list (2D list)
pakanan=['sego', 'bubur','fretciken']
ombenan=['teh','sirup','wedang']
cemilan=['keripik','kerupuk','rempeyek']
mg_awan=[pakanan,ombenan,cemilan]
print(mg_awan)
print(mg_awan[1][2])

print('-------------------------------')

#Tuple koyo list
aku=('Hilmy',16,'lanang','lanang')
print(aku.count('lanang'))
print(aku.index('Hilmy'))

print('-------------------------------')

#Set koyo list ng gk dwe urutan
ongko={'1','2','3'}
huruf={'1','a','b','c'}

ongko.add('4')
ongko.remove('2')
#ongko.clear()
#ongko.update(huruf) #nambahno nilai huruf ng ongko
#passw=ongko.union(huruf) #podo gabungno ng ndok var liyo
#print(passw)
for b in ongko:
  print(b)
print(ongko.difference(huruf))#nyetak sg ono ndok ongko ng gk ono ndok huruf
print(huruf.intersection(ongko)) #sg ono kabeh

print('-------------------------------')

# Dictionary {key:value}
kunci={3:'kamar1',6:'kamar2',9:'kamar3'}
kunci.update({5:'kamar4'})
kunci.update({9:'kamar5'})
kunci.pop(3) #busak<
#kunci.clear() #busak kabeh

print(kunci[6])
#print(kunci[4]) #error nk gk ono ndok datane
print(kunci.get(4)) #iki sg aman ben gk error
print(kunci.keys())
print(kunci.values())
for key,value in kunci.items():
  print(key,value)
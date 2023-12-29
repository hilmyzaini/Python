# Function
def tagihan (jengen,jumlah,tgl): #(parameter)
  jengen=jengen.capitalize()
  jumlah=str(jumlah)
  #print(f'Oi {jengen}! Utangem ijeh {jumlah}k kawet tanggal {tgl}')
  return 'Oi ' +jengen+'! Utangem ijeh '+jumlah+'k kawet tanggal '+tgl
#tagihan('Alif',40,'13/12')
a=tagihan('alif',40,'13/12') #(argument)
print(a)

print('-------------------------------')

#Default Argument
def rego_ak(rego_aw,diskon=0,pajek=11):
  return rego_aw * (1-diskon/100) *(1+pajek/100)
print('Rp '+str(round(rego_ak(30000,30))))

print('-------------------------------')

# Keyword Argument : urutane penulisane gk penting
#1. positional 2. default 3. keyword 4. arbitration
def ehem(salam,titel,jengen):
  print(f'{salam}{titel}{jengen}')
ehem('Selamat Pagi, ',jengen='Hilmy',titel='Prof. ')

print('-------------------------------')
# * = args, tipe: tuple > kanggo ngisi multiple non keyword argument
# ** = kwargs, tipe: dictionary > kanggo ngisi multiple keyword argument
def resi(*nama, **alamat):
    for arg in nama:
        print(arg, end=" ")
    print()

    if "pobox" in alamat and "jalan" in alamat:
        print(f"{alamat.get('pobox')} {alamat.get('desa')}, {alamat.get('jalan')}")
    elif "pobox" in alamat:
        print(f"{alamat.get('pobox')} {alamat.get('desa')}")
    elif "jalan" in alamat:
        print(f"{alamat.get('desa')}, {alamat.get('jalan')}")
    else:
        print(f"{alamat.get('desa')}")

    print(f"{alamat.get('kec')}, {alamat.get('kota')}, {alamat.get('prov')}")

resi("Dr.", "Hy", "Zen",
               desa='Medini Gg 6',
               jalan="Purwodadi km 14",
               #pobox="6000",
               kota="Kudus",
               prov="Jawa Tengah",
               kec="Undaan")
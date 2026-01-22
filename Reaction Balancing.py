# === Muhammad Hussein ===
# Reaksi : C6H5CHO + KOH -> C6H5CH2OH + C6H5COOK

from chempy import balance_stoichiometry, Reaction # <-- Masukkan library chempy yang berfungsi untuk bisa menyetarakan suatu reaksi yaitu Reaction dan balance_stoichiometry

r1 = Reaction.from_string('C6H5CHO + KOH -> C6H5CH2OH + C6H5COOK') # <-- Panggil reaksi tersebut dengan menggunakan .from_string

r , p = balance_stoichiometry(['C6H5CHO', 'KOH'],['C6H5CH2OH','C6H5COOK']) # Membuat dua variable yang di panggil jadi satu, r: reaktan dan p: produk, agar lebih fleksibel dan gampang dibuat reaksi tersebut. Disetarakan dengan memanggil balance_stoichiometry()

print(f'Reaksi yang terjadi: {r1}\n')
print(f'Reaktan: {r}\n')
print(f'Produk: {p}')

Balance = {} # Membuat Inisiasi dictionary (dictionary initialization) Balance = {} atau membuat object dictionary kosong dan menyimpannya ke variable

for x, y in r.items(): # For loop dengan dictionary unpacking (items()) atau iterasi dictionary menggunakan .items() dengan tuple unpacking
    Balance[x] = -y # <-- x dan y merupakan tuple unpacking
for x,y in p.items():  # For loop dengan dictionary unpacking (items()) atau iterasi dictionary menggunakan .items() dengan tuple unpacking
    Balance[x] = y # <-- x dan y merupakan tuple unpacking

print(f'\n{Balance}') # <-- Panggil reaksi tersebut dengan menggunakan perintah print()
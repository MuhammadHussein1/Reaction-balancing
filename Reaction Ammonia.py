from chempy import Reaction
from chempy import balance_stoichiometry

r = Reaction.from_string('N2 + H2 -> NH3')

print(r)

reac, produk = balance_stoichiometry({'N2', 'H2'},{'NH3'})
print(reac)
print(produk)

balance = {}

print('\nREACTION AMMONIA')
print(f"{'Spesies'}\t{'Peran'}\t{'Koefisien'}\n")
for x, y in reac.items():
    #balance[x] = -y
    print(f"{x}\t{'Reaktan'}\t{y}")
for x, y in produk.items():
    #balance[x] = y
    print(f"{x}\t{'Produk'}\t{y}")


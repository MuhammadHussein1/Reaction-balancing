from chempy import Reaction, balance_stoichiometry
import time

Proses = {}
Reactant = {}
Product = {}
Mol_weight = {}
day = 330 # 1 year
hr = 24 # 1 day

while True:
    Ask_user = input('Ask (Continue/Stop): ').capitalize()
    if Ask_user == "Stop":
        break
    elif Ask_user == 'Continue':
        print('Next')
    else:
        print("Can't be anything other than a choice (Continue/Stop)")
        continue
        
    Name_process = input('Name process: ')
    capacity = int(input('Enter capacity (ton/year): '))

    # Reactant
    Reactant = {}
    BM_Reactant = {}
    print('REACTANT')
    in_Reactant = int(input('How munch compound reactant: '))

    for x in range(in_Reactant):
        Name = input(f"Enter compound Reactant {x+1}: ").upper()
        BM = int(input(f"Enter molecular weight {x+1}: "))
        Reactant[Name] = 1
        BM_Reactant[Name] = BM

    # Product
    Product = {}
    BM_Product = {}
    print('\nPRODUCT')
    in_Product = int(input('How munch compound product: '))
    
    for y in range(in_Product):
        Name = input(f'Enter compound {y+1}: ').upper()
        BM = int(input(f'Enter molecular weight {y+1}: '))
        Product[Name] = 1
        BM_Product[Name] = BM
    
    reac, prod = balance_stoichiometry(Reactant, Product) # <-- Penyetaraan reaksi

    # Hanya menampilkan koefisien saja
    r = Reaction(reac, prod) # <-- Menampilkan reaksi
    print(r)
    coef_reac = list(reac.values())
    coef_prod = list(prod.values())
    print('\nStoichiometry Coefficients')
    print(f'Reactant {coef_reac}')
    print(f'Product {coef_prod}')

    #==============
    # Calcul Mol produk
    #==============
    product_main = list(Product.keys())[0]
    BM_main = BM_Product[product_main]
    tot_mol_product = capacity / BM_main

    #==============
    # Calcul Mol produk
    #==============
    print('\nReactant requirement (mol/year)')
    coef_main_prod = prod[product_main]

    for compound, coef in reac.items():
        reactant_mol = coef / coef_main_prod * tot_mol_product
        print(f'{compound}: {reactant_mol: .2f}') 

    # Countdown calculate 
    for t in range(5, 0, -1): 
        print(f'Wait {t}', end="\r")
        time.sleep(1)
        
    print(f'Need mol product per year: {tot_mol_product: .2f}') # <-- Requirement product per year


    print(f'\nFactory design with method {Name_process} and capacity {capacity} ton/year') # Tittle Thesis

print('\nEND')
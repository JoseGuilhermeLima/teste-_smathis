import random

Lista1 = []
Lista2 = []

count = 0 

while count < 1000:
    
    #Para ficar mais legivel no if, atribui o valor aleatorio à variavel var_intNumero
    var_intNumero = random.randint(1, 10)
    
    if var_intNumero > 5:
        Lista1.append(var_intNumero)  
    else:
        Lista2.append(var_intNumero)  

    count += 1  

# Verifica o tamanho das listas
print(f"Tamanho da Lista1: {len(Lista1)}")
print(f"Tamanho da Lista2: {len(Lista2)}")

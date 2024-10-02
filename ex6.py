import random #Biblioteca que gera números aleatórios

def sorteio() ->list:
    """
    Sorteia 6 números únicos entre 1 e 60
    
    Parâmetros:
    
    Retorna:
       - list: Retorna os números em forma de lista por ordem crescente
    """
    var_listNumeroSorteados = random.sample(range(1,61), 6)
    return sorted(var_listNumeroSorteados)


print(f"Os números sorteados foram:\n{sorteio()}")
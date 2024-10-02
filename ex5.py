def numero_maximo_caixas(arg_intAdesivosDisponiveis: int) -> int:
    """
    Calcula o número máximo de caixas que podem ser numeradas com um determinado número de adesivos.

    Parâmetros:
        arg_intAdesivos_disponiveis (int): O número total de adesivos disponíveis.

    Retorna:
        int: O número máximo de caixas que podem ser numeradas.
    """
    
    # Inicializando variáveis com 0 
    var_intTotalAdesivos = 0
    var_intNumeroCaixas = 0

    while True:
        # O próximo número da caixa que precisa ser numerado
        var_intNumeroCaixas += 1
        
        # Calculando a quantidade de adesivos necessários para o número atual
        var_intAdesivosNecessarios = len(str(var_intNumeroCaixas))

        # Verificando se há adesivos suficientes
        if var_intTotalAdesivos + var_intAdesivosNecessarios > arg_intAdesivosDisponiveis:
            break
        
        # Atualiza o total de adesivos usados
        var_intTotalAdesivos += var_intAdesivosNecessarios
    
    return var_intNumeroCaixas - 1  # Retorna o número máximo de caixas que podem ser numeradas

# Exemplo
print(f"Exemplo 1: Se há 14 adesivos disponíveis, é possível numerar: {numero_maximo_caixas(14)} caixas")

# Loop testes do código.
while True:
    try:
        var_intAdesivos = int(input("Digite o valor de adesivos ou '0' para sair: "))
        if var_intAdesivos<0:
            print("Valor indisponível. Insira um valor positivo")
        # Verifica se o usuario quer parar
        elif var_intAdesivos == 0:
            print("Encerrando o programa.")
            break
        else:
            var_intMaximoCaixas = numero_maximo_caixas(var_intAdesivos)
            print(f"Com {var_intAdesivos} adesivos disponíveis, é possível numerar {var_intMaximoCaixas} caixas.")
    except ValueError:
        print("OPS! Parece que você não digitou um número inteiro. Digite um número inteiro.")


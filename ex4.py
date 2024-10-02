def sacar(arg_intValorSaque: int) ->str:
    """
    Recebe como entrada o valor que se deseja sacar e retorne a menor quantidade de notas que o compõem
    
    Parâmetros:
       - arg_intValorSaque(int): Valor em reais que se deseja sacar. Deve ser um múltiplo de 5.
    Retorna:
       - str: Uma string informando a quantidade de notas de R$ 50, R$ 20 e R$ 5 necessárias para compor o valor
    """
    #Verificação para valores validos
    if arg_intValorSaque <=0:
        return "Valor indisponível. Insira um valor positivo." 
    if arg_intValorSaque % 5 != 0:
        return "Valor indisponível. Insira um valor múltiplo de 5."

    var_intNotas50 = var_intNotas20 = var_intNotas5 = 0

    # Calcula a quantidade de notas de 50
    var_intNotas50 = arg_intValorSaque // 50
    arg_intValorSaque %= 50

    # Calcula a quantidade de notas de 20
    var_intNotas20 = arg_intValorSaque // 20
    arg_intValorSaque %= 20

    # Calcula a quantidade de notas de 5
    var_intNotas5 = arg_intValorSaque // 5

    return f"Notas de R$ 50: {var_intNotas50}, Notas de R$ 20: {var_intNotas20}, Notas de R$ 5: {var_intNotas5}"

# Exemplos de uso
print("Exemplo 1: Para um saque de R$ 25 é necessario:\n",sacar(25))
print("Exemplo 2: Para um saque de R$ 175 é necessario:\n",sacar(175))
print("Sua vez!!!")

# Loop testes do código.
while True:
    try:
        var_intValorSaque = int(input("Digite o valor do saque ou '0' para sair: "))

        # Verifica se o usuario quer parar
        if var_intValorSaque == 0:
            print("Encerrando o programa.")
            break

        # Exibe o resultado do saque
        print(sacar(var_intValorSaque))
    except ValueError:
        print("OPS! Parece que você não digitou um número inteiro.\n Por favor digite um número inteiro.")
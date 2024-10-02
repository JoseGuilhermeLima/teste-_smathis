import random #Biblioteca que gera números aleatórios

def RPABet() -> str:
    """
    Gera um número aleatório dentro de um intervalo escolhido pelo próprio jogador, que servirá como resposta, e solicitar que o usuário tente adivinhá-lo.
    
    Parâmetros:
    
    Retorna:
       - str: a. Se o palpite do usuário for errado, o jogo deve informar ao usuário se foi maior ou menor que a resposta correta e solicitar um novo chute.
              b. Se o palpite for correto, o jogo deve avisar ao usuário que ele acertou e informar o número de tentativas utilizadas.
    """
    
    print("#######Bem-vindo a RPABet!#######")
    
    #Inicializia as tentativas
    var_intTentativas = 0    
    print("Parece que você ainda não fez seu palpite! Vamos definir o intervalo de números.")
    
    #Loop para escolher o intervalo
    while True:
        try:
            var_intValorMenor = int(input("1º: Digite o menor valor do intervalo: "))
            var_intValorMaior = int(input("2º: Digite o maior valor do intervalo:" ))
            #Verificando se o valor menor não é maior que o valor valor maior do intervalo
            if var_intValorMenor>= var_intValorMaior:
                print("O valor menor deve ser menor que o valor maior. Tente novamente!")
                continue
            break
        except ValueError:
            print("OPS! Parece que você não digitou um número inteiro.\nPor favor digite um número inteiro.")

    #Sorteia o valor aleatório dentro do intervalo
    var_intNumeroAleatorio = random.randint(var_intValorMenor, var_intValorMaior)
    
    #Loop para a adivinhação
    while True:
        try:
            var_intTentativas +=1
            print(f"{var_intTentativas}ª tentativa!!!")
            var_intPalpite = int(input(f"Qual o seu palpite entre os números {var_intValorMenor} e {var_intValorMaior}: "))
            #Verificando se o palpite está dentro do limite
            if var_intPalpite < var_intValorMenor or var_intPalpite > var_intValorMaior:
                print(f"O seu palpite está fora do intervalo. Por favor, insira um número dentro do intervalo({var_intValorMenor} a {var_intValorMaior})")
                continue
            #
            if var_intPalpite < var_intNumeroAleatorio:
                print("QUE PENA DEU RED! Seu palpite foi menor que o número correto.")
            elif var_intPalpite > var_intNumeroAleatorio:
                print("QUE PENA DEU RED! Seu palpite foi maior que o número correto.")
            else:
                print(F"DEU GREEN!!!!! Você acertou o número {var_intNumeroAleatorio} em {var_intTentativas} tentativas!")
                break
        except ValueError:
            print("OPS! Parece que você não digitou um número inteiro.\nPor favor digite um número inteiro.")

#Loop para testes e para jogar varias vezes sem precisar rodar toda hora
while True:
    RPABet()
    # Pergunta se o usuário deseja jogar novamente
    var_strContinuar = input("Deseja jogar novamente? (s/n): ").strip().lower()
    if var_strContinuar == 'n':
        print("Obrigado por jogar RPABet!")
        break
    elif var_strContinuar != 's':
        print("Opção inválida. Por favor, responda com 's' ou 'n'.")


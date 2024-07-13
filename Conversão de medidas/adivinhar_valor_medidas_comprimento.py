def converter_metros_para_unidade(metros, unidade):
    if unidade == 'centímetros':
        return metros * 100
    elif unidade == 'milímetros':
        return metros * 1000
    elif unidade == 'quilômetros':
        return metros / 1000
    else:
        return None

def main():
    print("Bem-vindo ao conversor de medidas!")
    
    # Pergunta a medida em metros
    metros = float(input("Digite a medida em metros: "))
    
    # Pergunta a unidade para converter
    unidade = input("Para qual unidade de comprimento você quer converter (centímetros, milímetros, quilômetros)? ")
    
    # Converte a medida
    medida_convertida = converter_metros_para_unidade(metros, unidade)
    
    if medida_convertida is None:
        print("Unidade inválida. Tente novamente.")
        return
    
    # Jogo de adivinhação
    print(f"Tente adivinhar o valor convertido de {metros} metros para {unidade}.")
    tentativa = float(input("Digite seu palpite: "))
    
    if tentativa == medida_convertida:
        print("Parabéns! Você acertou!")
    else:
        print(f"Você errou. O valor correto é {medida_convertida} {unidade}.")
    
if __name__ == "__main__":
    main()


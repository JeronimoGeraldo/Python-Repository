def converter_metros_quadrados_para_unidade(metros_quadrados, unidade):
    if unidade == 'centímetros quadrados':
        return metros_quadrados * 10000
    elif unidade == 'milímetros quadrados':
        return metros_quadrados * 1000000
    elif unidade == 'quilômetros quadrados':
        return metros_quadrados / 1000000
    elif unidade == 'hectares':
        return metros_quadrados / 10000
    elif unidade == 'acres':
        return metros_quadrados / 4046.86
    else:
        return None

def main():
    print("Bem-vindo ao conversor de medidas de superfície!")
    
    metros_quadrados = float(input("Digite a medida em metros quadrados: "))
    
    unidade = input("Para qual unidade de superfície você quer converter (centímetros quadrados, milímetros quadrados, quilômetros quadrados, hectares, acres)? ")
    
    medida_convertida = converter_metros_quadrados_para_unidade(metros_quadrados, unidade)
    
    if medida_convertida is None:
        print("Unidade inválida. Tente novamente.")
        return
    
    print(f"Tente adivinhar o valor convertido de {metros_quadrados} metros quadrados para {unidade}.")
    tentativa = float(input("Digite seu palpite: "))
    
    if tentativa == medida_convertida:
        print("Parabéns! Você acertou!")
    else:
        print(f"Você errou. O valor correto é {medida_convertida} {unidade}.")
    
if __name__ == "__main__":
    main()

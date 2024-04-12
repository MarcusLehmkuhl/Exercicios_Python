altura = float(input("Digite a altura da pessoa em metros: "))
sexo = input("Digite o sexo da pessoa (M para masculino, F para feminino): ")
if sexo.upper() == 'M':
    peso_ideal = (72.7 * altura) - 58
    print("O peso ideal para um homem com essa altura é:", peso_ideal)
elif sexo.upper() == 'F':
    peso_ideal = (62.1 * altura) - 44.7
    print("O peso ideal para uma mulher com essa altura é:", peso_ideal)
else:
    print("Sexo inválido. Por favor, insira M para masculino ou F para feminino.")

cobertura_por_litro = 3
tamanho_lata = 18
preco_lata = 80.00
area_a_ser_pintada = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
litros_necessarios = area_a_ser_pintada / cobertura_por_litro
latas_necessarias = litros_necessarios / tamanho_lata
latas_necessarias = int(latas_necessarias) if latas_necessarias.is_integer() else int(latas_necessarias) + 1
preco_total = latas_necessarias * preco_lata
print("Quantidade de latas de tinta necessárias:", latas_necessarias)
print("Preço total: R$", preco_total)

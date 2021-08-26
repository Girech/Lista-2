numero = input("Digite um numero:")
verificacao = bool(numero.isdecimal())
verificacao2 = bool(numero.isnumeric())
if ((verificacao == True) or (verificacao2 == True)):
    print(numero)
if((verificacao == False) and (verificacao2 == False)):
    print("Digite um valor valido")
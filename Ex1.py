numero = input("Digite um numero:")
verificacao = bool(numero.isnumeric())
if (verificacao == True):
    print(numero)
if(verificacao == False):
    print("Digite um valor valido")
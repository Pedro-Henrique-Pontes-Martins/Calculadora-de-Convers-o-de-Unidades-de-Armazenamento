from Calculadora_de_Unidades_de_Memória import converterStringParaFloat, bitParaByte, byteParaBit, byteParaKB, KBParaByte, KBParaMB, MBParaKB, MBParaGB, GBParaMB, GBParaTB, TBParaGB, TBParaPB, PBParaTB

print(' Escreva 1 para converter de bit para byte \n Escreva 2 para converter de byte para bit \n Escreva 3 para converter de byte para KB \n Escreva 4 para converter de KB para byte \n Escreva 5 para converter de KB para MB \n Escreva 6 para converter de MB para KB \n Escreva 7 para converter de MB para GB \n Escreva 8 para converter de GB para MB \n Escreva 9 para converter de GB para TB \n Escreva 10 para converter de TB para GB \n Escreva 11 para converter de TB para PB \n Escreva 12 para converter de PB para TB \n')

print('Selecione um valor do índice')
funcEscolha = input()

if(funcEscolha == '1'):
    print('Insira o valor a ser convertido')
    entradaDoTecladoValorASerConvertida  = converterStringParaFloat(input())
    valorConvertido = bitParaByte(entradaDoTecladoValorASerConvertida)
    print(valorConvertido)

elif(funcEscolha == '2'):
    print('Insira o valor a ser convertido')
    entradaDoTecladoValorASerConvertida  = converterStringParaFloat(input())
    valorConvertido = byteParaBit(entradaDoTecladoValorASerConvertida)
    print(valorConvertido)

elif(funcEscolha == '3'):
    print('Insira o valor a ser convertido')
    entradaDoTecladoValorASerConvertida  = converterStringParaFloat(input())
    valorConvertido = byteParaKB(entradaDoTecladoValorASerConvertida)
    print(valorConvertido)

elif(funcEscolha == '4'):
    print('Insira o valor a ser convertido')
    entradaDoTecladoValorASerConvertida  = converterStringParaFloat(input())
    valorConvertido = KBParaByte(entradaDoTecladoValorASerConvertida)
    print(valorConvertido)

elif(funcEscolha == '5'):
    print('Insira o valor a ser convertido')
    entradaDoTecladoValorASerConvertida  = converterStringParaFloat(input())
    valorConvertido = KBParaMB(entradaDoTecladoValorASerConvertida)
    print(valorConvertido)

elif(funcEscolha == '6'):
    print('Insira o valor a ser convertido')
    entradaDoTecladoValorASerConvertida  = converterStringParaFloat(input())
    valorConvertido = MBParaKB(entradaDoTecladoValorASerConvertida)
    print(valorConvertido)

elif(funcEscolha == '7'):
    print('Insira o valor a ser convertido')
    entradaDoTecladoValorASerConvertida  = converterStringParaFloat(input())
    valorConvertido = MBParaGB(entradaDoTecladoValorASerConvertida)
    print(valorConvertido)

elif(funcEscolha == '8'):
    print('Insira o valor a ser convertido')
    entradaDoTecladoValorASerConvertida  = converterStringParaFloat(input())
    valorConvertido = GBParaMB(entradaDoTecladoValorASerConvertida)
    print(valorConvertido)

elif(funcEscolha == '9'):
    print('Insira o valor a ser convertido')
    entradaDoTecladoValorASerConvertida  = converterStringParaFloat(input())
    valorConvertido = GBParaTB(entradaDoTecladoValorASerConvertida)
    print(valorConvertido)

elif(funcEscolha == '10'):
    print('Insira o valor a ser convertido')
    entradaDoTecladoValorASerConvertida  = converterStringParaFloat(input())
    valorConvertido = TBParaGB(entradaDoTecladoValorASerConvertida)
    print(valorConvertido)

elif(funcEscolha == '11'):
    print('Insira o valor a ser convertido')
    entradaDoTecladoValorASerConvertida  = converterStringParaFloat(input())
    valorConvertido = TBParaPB(entradaDoTecladoValorASerConvertida)
    print(valorConvertido)

elif(funcEscolha == '12'):
    print('Insira o valor a ser convertido')
    entradaDoTecladoValorASerConvertida  = converterStringParaFloat(input())
    valorConvertido = PBParaTB(entradaDoTecladoValorASerConvertida)
    print(valorConvertido)

else:
    print('Valor não encontrado no índice')
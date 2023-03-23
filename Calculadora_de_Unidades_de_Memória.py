Const_ValorParaConverção = 1024

def converterStringParaFloat(value):
    return float(value)

def bitParaByte(valorASerConvertido):
    print('Valor convertido de bit para byte')
    bytesCalculado = valorASerConvertido / 8
    return bytesCalculado

print('Insira o valor a ser convertido')
entradaDoTecladoValorASerConvertida  = converterStringParaFloat(input())
valorConvertido = bitParaByte(entradaDoTecladoValorASerConvertida)
print(valorConvertido)
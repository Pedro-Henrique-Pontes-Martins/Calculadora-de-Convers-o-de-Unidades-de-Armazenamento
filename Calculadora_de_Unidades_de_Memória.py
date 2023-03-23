Const_ValorParaConverção = 1024

def converterStringParaFloat(value):
    return float(value)

def bitParaByte(valorASerConvertido):
    print('Valor convertido de bit para byte')
    bytesCalculado = valorASerConvertido / 8
    return bytesCalculado

def byteParaBit(valorASerConvertido):
    print('Valor convertido de byte para bit')
    bitsCalculado = valorASerConvertido * 8
    return bitsCalculado

def byteParaKB(valorASerConvertido):
    print('Valor convertido de byte para KB')
    kilobytesCalculado = valorASerConvertido / Const_ValorParaConverção
    return kilobytesCalculado

def KBParaByte(valorASerConvertido):
    print('Valor convertido de KB para Byte')
    bytesCalculado = valorASerConvertido * Const_ValorParaConverção
    return bytesCalculado

def KBParaMB(valorASerConvertido):
    print('Valor convertido de KB para MB')
    megabytesCalculado = valorASerConvertido / Const_ValorParaConverção
    return megabytesCalculado

print('Insira o valor a ser convertido')
entradaDoTecladoValorASerConvertida  = converterStringParaFloat(input())
valorConvertido = KBParaMB(entradaDoTecladoValorASerConvertida)
print(valorConvertido)
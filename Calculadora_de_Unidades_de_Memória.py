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

def MBParaKB(valorASerConvertido):
    print('Valor convertido de MB para KB')
    kilobytesCalculado = valorASerConvertido * Const_ValorParaConverção
    return kilobytesCalculado

def MBParaGB(valorASerConvertido):
    print('Valor convertido de MB para GB')
    gigabytesCalculado = valorASerConvertido / Const_ValorParaConverção
    return gigabytesCalculado

def GBParaMB(valorASerConvertido):
    print('Valor convertido de GB para MB')
    megabytesCalculado = valorASerConvertido * Const_ValorParaConverção
    return megabytesCalculado

def GBParaTB(valorASerConvertido):
    print('Valor convertido de GB para TB')
    terabytesCalculado = valorASerConvertido / Const_ValorParaConverção
    return terabytesCalculado

print('Insira o valor a ser convertido')
entradaDoTecladoValorASerConvertida  = converterStringParaFloat(input())
valorConvertido = GBParaTB(entradaDoTecladoValorASerConvertida)
print(valorConvertido)
unidadesDeMedidas = ['Bit', 'Byte', 'KB', 'MB', 'GB', 'TB', 'PB' ]

def calcularFatorDeConversão(unidadeInicial, unidadeDeConversão):
    contador = 0
    for i in unidadesDeMedidas:
        if (unidadeInicial == i):
            unidadeInicial = contador

        if (unidadeDeConversão == i):
            unidadeDeConversão = contador

        contador += 1
    fatorDeConversão = unidadeInicial - unidadeDeConversão
    return int(fatorDeConversão)

def conversão(unidadeInicial, unidadeDeConversão, númeroParaConversão):
    fatorDeConvesão = 1024 ** calcularFatorDeConversão(unidadeInicial, unidadeDeConversão)
    print (fatorDeConvesão)
    númeroConvertido = númeroParaConversão
    if(unidadeInicial == 'Bit' or unidadeDeConversão == 'Bit'):
        print('Em breve!')
    else:
        if (fatorDeConvesão < 0):
            númeroConvertido *= fatorDeConvesão
            
        if (fatorDeConvesão > 0):
            númeroConvertido *= fatorDeConvesão
    return númeroConvertido

print('Digite a unidade de medida inicial:')
unidadeInicial = input()
print('Digite a unidade para qual o valor será convertido:')
unidadeDeConversão = input()
print(calcularFatorDeConversão(unidadeInicial, unidadeDeConversão))
print('Digite o número a ser convertido:')
numeroParaConversão = float(input())

print(conversão(unidadeInicial, unidadeDeConversão, numeroParaConversão))
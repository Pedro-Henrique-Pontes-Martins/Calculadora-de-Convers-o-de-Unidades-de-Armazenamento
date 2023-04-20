unidadesDeMedidas = ['Bit', 'Byte', 'KB', 'MB', 'GB', 'TB', 'PB' ]

def fatorDeConversão(unidadeInicial, unidadeDeConversão):
    contador = 0
    for i in unidadesDeMedidas:
        if (unidadeInicial == i):
            unidadeInicial = contador

        if (unidadeDeConversão == i):
            unidadeDeConversão = contador

        contador += 1
    return unidadeInicial - unidadeDeConversão

def conversão(unidadeInicial, unidadeDeConversão, númeroParaConversão):
    fatorDeConversão = 1024 ** fatorDeConversão(unidadeInicial, unidadeDeConversão)
    númeroConvertido = númeroParaConversão
    if(unidadeInicial != 'Bit' and unidadeDeConversão != 'Bit'):
        if (fatorDeConversão > 0):
            númeroConvertido *= fatorDeConversão
            
        if (fatorDeConversão < 0):
            númeroConvertido /= fatorDeConversão * -1


print('Digite a unidade de medida inicial:')
unidadeInicial = input()
print('Digite a unidade para qual o valor será convertido:')
unidadeDeConversão = input()

print('Digite o número a ser convertido:')
numeroParaConversão = float(input())


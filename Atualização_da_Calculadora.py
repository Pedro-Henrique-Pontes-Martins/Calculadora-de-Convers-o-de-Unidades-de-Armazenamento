unidadesDeMedidas = ['Bit', 'Byte', 'KB', 'MB', 'GB', 'TB', 'PB' ]

def mostrarUnidadesDeMedida(unidadesDeMedidas):
    print('Unidades de Medida Disponíveis:')
    for i in unidadesDeMedidas:
        print(i)

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
    fatorDeConversão = calcularFatorDeConversão(unidadeInicial, unidadeDeConversão)
    númeroConvertido = númeroParaConversão

    if(unidadeInicial == 'Bit' or unidadeDeConversão == 'Bit'):
        if(unidadeInicial == 'Bit'):
            númeroConvertido /= 8
            fatorDeConversão += 1 
        if(unidadeDeConversão == 'Bit'):
            númeroConvertido *= 8 
            fatorDeConversão -= 1 

    if (fatorDeConversão < 0):
        fatorDeConversão *= -1
        fatorDeConversão = 1024 ** fatorDeConversão
        númeroConvertido /= fatorDeConversão
    elif(fatorDeConversão > 0):
        fatorDeConversão = 1024 ** fatorDeConversão
        númeroConvertido *= fatorDeConversão
        
    return númeroConvertido

mostrarUnidadesDeMedida(unidadesDeMedidas)

print('Digite a unidade de medida inicial do valor:')
unidadeInicial = input()
print('Digite a unidade para qual o valor será convertido:')
unidadeDeConversão = input()
print('Digite o número a ser convertido:')
numeroParaConversão = float(input())

print('Resultado da conversão:')
print(str(conversão(unidadeInicial, unidadeDeConversão, numeroParaConversão)) + ' ' + unidadeDeConversão + 's')
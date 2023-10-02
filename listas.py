#para estos desafios criei uma lista chamada peças que contém peças de automóveis no primeiro desafio faz uma contagem de quantas peças de molas tem na lista 
# e no segundo desafio é tipo consulta para saber si existe em estoque a peça consultada.

# Desafio 1

pecas = ['Vela de ignição','Molas','Pistão','Válvula','Filtro de ar','Molas','Amortecedor','Pistão','Válvula','Pistão','Molas']
contador = 0

for pecas in pecas:
    if pecas== 'Molas':
        contador +=1
        
print('Numero de molas na lista:' ,contador)        


#Desafio 2

pecas = ['Vela de ignição','Molas','Pistão','Válvula','Filtro de ar','Molas','Amortecedor','Pistão','Válvula','Pistão','Molas']
pesquisa_pecas = input('Digite o nome da peça:')

if pesquisa_pecas in pecas:
    print('A peça do carro esta disponível em estoque')
else:
    print('A peça do carro não esta disponível em estoque') 
    
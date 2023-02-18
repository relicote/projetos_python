"""
Faça uma lista de compras com listas
o usuário deve ter a possibilidade de 
inserir, apagar e listar os valores da sua lista
Não permita que  o programa quebre com erros de indices inexistentes na lsita  
"""
#menu inicial
#digitar apenas 1 ou 2 (corrigir entrada para somente int após o primeiro aviso)
import os
lista_de_compras = []

while True:
    # Solicitando o item para o usuário
    item = input('Digite um item para adicionar a lista: ')

    # Adicionando o item a lista de compras (repetidor)
    lista_de_compras.append(item)

    # Condição para excluir item da lista
    del_item = input('Deseja deletar algum item da lista?\
        [1] - Sim ou [2] - Não.')

    #Condição para receber somente numeros
    if del_item.isnumeric() == False:
        while del_item.isnumeric() ==False:
            print('Digite apenas numeros!')
            del_item = input('Deseja deletar algum item da lista?\
        [1] - Sim ou [2] - Não.')      
        
    del_item = int(del_item)

    #Condição para manter o usuário entre 1 ou 2
    if del_item <1 or del_item > 2:
            while del_item <1 or del_item > 2:
                print('Digite apenas numeros!') 
                del_item = input('Deseja deletar algum item da lista?\
                [1] - Sim ou [2] - Não.')
                while del_item.isnumeric() == False:
                        print('Digite apenas numeros!')
                        del_item = input('Deseja deletar algum item da lista?\
                    [1] - Sim ou [2] - Não.')
                        del_item = int(del_item)

    

    if del_item == 1:
        #Numerando a lista para o usuário visualizar o item desejado
        for indice, nome in enumerate(lista_de_compras):
            print(f'{indice} - {nome} ')
        
        #Solicitando o numero do item para exclusão e printando o resultado pós deletado
        del_item = input('Qual item deseja excluir?')

        #Condição para receber somente numeros
        if del_item.isnumeric() == False:
            while del_item.isnumeric() ==False:
                print('Digite apenas numeros!')
                del_item = input('Qual item deseja excluir?')

        del_item = int(del_item)

        #Condição para conter o 'out of range' 
        if del_item > indice or del_item < indice: 
            while del_item > indice:   
                print('Item não encontrado na lista. Favor inserir um numero valido.')
                del_item = input('Qual item deseja excluir?')
                #Laço para não inserir texto
                while del_item.isnumeric() == False:
                    print('Digite apenas numeros!')
                    del_item = input('Qual item deseja excluir?')

                del_item = int(del_item)

        lista_de_compras.pop(del_item)


   #Condição para digitar somente numeros
    visu = input('Deseja visualizar sua lista? [1] - SIM [2] - NÃO: ')
    if visu.isnumeric() == False:
        while visu.isnumeric() == False:
            print('Digite apenas numeros!')
            visu = input('Deseja visualizar sua lista? [1] - SIM [2] - NÃO: ')
    
    visu = int(visu)
    
    #Condição para manter o usuário entre 1 ou 2
    """ if visu <1 or visu > 2:
        while visu <1 or visu > 2:
            print('Digite apenas numeros!') 
            visu = input('Deseja visualizar sua lista? [1] - SIM [2] - NÃO: ')  
            visu = int(visu) """

    #Condição para visualizar a lista
    if visu == 1:
        for indice, nome in enumerate(lista_de_compras):
            print(f'{indice} - {nome} ')

        
    else:
        continue

    
    
       
    
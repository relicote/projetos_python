"""
Faça uma lista de compras com listas
o usuário deve ter a possibilidade de 
inserir, apagar e listar os valores da sua lista
Não permita que  o programa quebre com erros de indices inexistentes na lsita  
"""

lista_de_compras = []

while True:
    # Solicitando o item para o usuário
    item = input('Digite um item para adicionar a lista: ')

    # Adicionando o item a lista de compras (repetidor)
    lista_de_compras.append(item)
    print(lista_de_compras)


    # Condição para excluir item da lista
    del_item = input('Deseja deletar algum item da lista?\
        [1] - Sim ou [2] - Não.')
    del_item = int(del_item)

    if del_item == 1:
        #Numerando a lista para o usuário visualizar o item desejado
        for indice, nome in enumerate(lista_de_compras):
            print(f'{indice} - {nome} ')
        
        #Solicitando o numero do item para exclusão e printando o resultado pós deletado
        del_item = input('Qual item deseja excluir?')
        del_item = int(del_item)
        lista_de_compras.pop(del_item)

        #Evitando erro 'out of range'
    # if del_item > indice:       
    #     print('Item não encontrado na lista. Favor inserir um numero valido.')
    #     break
    visu = input('Deseja visualizar sua lista?')
    
    if visu == 's':
        for indice, nome in enumerate(lista_de_compras):
            print(f'{indice} - {nome} ')

        
    else:
        continue

    
    
       
    
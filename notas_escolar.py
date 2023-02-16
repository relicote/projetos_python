import os
lnotas = []
soma = 0
i = 0

#criando o laço para armazenar 4 notas
while i <= 3:
    
    nota = input('Insira uma nota: ')

#validando se o o valor digitado é numerico
    if nota.isnumeric() == False:
        while nota.isnumeric() == False:
            print('Digite apenas numeros!')
            break
        continue

#validando se a nota é menor que 0 ou maior que 10
    elif  int(nota) <0 or int(nota) >10:
            while int(nota) <0 or int(nota) >10:
                print('Digite uma nota valida!')
                break
            continue

#convertendo nota para int, adicionando a nota em uma lista e armazenando para soma
    else:
        nota = int(nota)
        lnotas.append(nota)
        soma = soma + nota   

        print(f'A nota inserida foi:{nota} ')
        del(nota)
        i+=1

#Printando a media final pelo divisor de 4

os.system('cls') #limpando o terminal para imprimir o resultado

mf = soma / 4
print('*************************')
print(f'A média final é de: {mf}')
print('*************************')

#Validando e printando se a nota é suficiente para aprovação

if mf >= 7:
    print('Aluno aprovado.')

else:
    print("Aluno reprovado.")

#Printando a maior e menor nota
print(f'A maior nota foi: {max(lnotas)}')
print(f'A menor nota foi: {min(lnotas)}')

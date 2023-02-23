u=10
soma = int()
lista_res = []


#Recebe o CPF fornecido pelo usuário
cpf = input('Digite seu CPF: ')

# repetição de multiplicador
for i in cpf: 
    i = int(i)
    r = u * i
    lista_res.append(r)
    # print(lista_res)
    u-=1

# somando os valores do resultado
u=0
for i in lista_res:
    soma = soma + lista_res[u]
    # print(soma)
    u+=1

# Multiplicando a soma por 10  
soma = soma * 10

# print(soma)

soma = soma % 11

if soma > 9:
    soma = 0
    print(f'O primeiro digito do seu CPF é: {soma}')

elif soma < 9:
    print(f'O primeiro digito do seu CPF é: {soma}')


############Encontrando o segundo digito##################

# repetição de multiplicador 
u=11
i=0
lista_res.clear()

#concatenaçao
cpf = str(cpf)
soma = str(soma)
cpf = cpf + soma
# print(cpf)


for i in cpf: 
    i = int(i)
    r = u * i
    lista_res.append(r)
    # print(lista_res)
    u-=1

# somando os valores do resultado 2
u=0
soma=0
for i in lista_res:
    soma = int(soma)
    soma = soma + lista_res[u]
    # print(soma)
    u+=1

# Multiplicando a soma por 10  
soma = soma * 10
soma = soma % 11


if soma > 9:
    soma = 0
    print(f'O segundo digito do seu CPF é: {soma}')

elif soma <= 9:
    print(f'O segundo digito do seu CPF é: {soma}')
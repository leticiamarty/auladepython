# name = "meu nome e lele"

# print(name)

# #  imprimir as coisas no arquivo oque estao dentro de print

# birth_year = input('qual ano vc nasceu?')
# year = 2002
# # perguntar e ja responder la no arquivo 


# print(year - int(birth_year))
# fazer conta com idade

# peso_lbs = input('descubra quanto vale em kg')
# peso_kg =(peso_lbs) * 0.45

# descobrir pesso com conta

# name = "leticia"
# color = input ("qual a sua cor favorita?")

# print("A" + name + " gosta da cor "  +  color)
#  perguntar ao usuario sua cor  e dps fazer uma frase

# name = "leticia"

# print(name[1:5])
# print (len (name))
# print (name.find('i'))
# print(name.replace('leticia','martins'))

# course = 'estacao hack do facebook'
# print('hack' in course )
 
# #  condicao
# summer = True   # letra maiscula sempre
# winter = False 

# if summer:
#     print ('use oculos de sol')
#     print('use filtro solar')
# elif winter:
#     print('nao esquece o casado filho')
# else :
#      print('nao use oculos')


# while  isso é repetitivo ate chegar no numero maximo 

# secret_number = 2
# i = 0

# while i < 5: 
#     print(i)
#     i = i + 1
# print('acabou')

#  atividade com a compra do  celular 
# secret_number = 7
# i = 0 
# while i < 3: 
#     chute = int(input('qual o seu numero  secreto ?'))          #int serve pra converter um numero inteiro 
#     i = i + 1
#     if chute == secret_number:    # se o numero que o usuario colocou for igual o numero secreto chega a notificacao que ele acertou 
#         print('vc acertou miseravi')
#         break  #"i = 3" breack serve pra perguntar e se vc acertar ja nn pergunta mais dps
#     else:
#         print('errouuu')


# # listas
# name = ['ana','leticia','lucas','ju']
# print(name[1:3])

# lista com numeros 
numbers = [1,4,6,8,345,21,101]
# numbers.append(20)        #append é como se fosse adicionar em ultimo lugar 
# numbers.append(21)        #append é como se fosse adicionar em ultimo lugar 
# numbers.insert(0, 99)     #insert é pra vc escolher a posicao e adicionar um numero na posicao escolhida (com a posicao na frente e o numero )
# #numbers.clear()          #cuidado com esse metodo ele apaga tudo 
# numbers.pop()             #exclui so o ultimo add
# print(numbers)
#$print.remove()              #remove so o numero que vc quer 

# print(numbers.index(345)) # index retorna a posicao do numero 
 
# lista2 = numbers.copy()  # isso serve pra ter uma copia do arquivo se caso apagar algo 
# print(lista2)  # vai mostrar tudo que tinha na lista original 


# copiar a lista e remover tal numero  de uma vez so 
# lista2 = numbers.copy()
# lista2.remove(6)
# print(numbers)
# print(lista2)

# nova_lista = []   #vc cria uma lista nova coloca valores  que a nova nn tinha ainda

# for number in numbers:
#     if number not in nova_lista:
#         nova_lista.append(number)
# print(nova_lista)


# #tupla ou tuple
# cursos = ('matematica','ingles','programacao')

#lista vc pode editar,acrecentar, apagar <<<,ja com a tupla nao da pra mudar nada, apenas  da pra ver a ordem que esta esta cada coisa 


#dicionarios

# pessoa = {
#     'name': 'hayane',
#     'age':22,
#     'endereco':'area de preservacao florestal',
#     'coisas': ['python','c','cobol','pascal','pearl','birlll']
# }

# print(pessoa['name'])
# print(pessoa['endereco'])

lista = [1, 2, 5, 10, 64]

print (max(lista)) # max serve pra pergar o maior numero que tem na lista 



faltas = input("quantas faltas vc teve?")
nota = 10

if faltas > 3:
    print("vc faltou demais")
elif faltas < 2 :
    print("passou")

if notas >  6:
    print ("passou com nota azul")
elif  notas < 6:
    print ("nao passou, melhore sua nota da proxima vez ")




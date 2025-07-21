###criando uma lista
##ivan,  Gustavo,
#  Tarso, gabriel
# victor, Rafael
# Fabricio

#qual seria o print e
#  input para impedir os nomes?

print("*** Lista de nomes ***\n")

nomes= input("Digite os nomes separados por vírgula:"). split

#nomes = [nome.strip() for nome in nomes]

print(nomes)

print("\n Quais operações você quer fazer:") 
print("1 -Adicionar um nome")
print("2 -Remover um nome")
print("3 - Listar nomes")
print("4 - Sair")

#faça um loop para pedir a opçaõ do usuário

while True:
    opcao = input("Digite a opção desejada(1-4):")

    if opcao == "1":
        #novo_nome = input("Digite o nome a ser adicionado:")
        #nomes.append(novo_nome)
        #print(f"{novo_nome} foi adicionado a lista.")
        print(f" foi adicionado a lista.")

elif opcao == "2":
#nome_remover = input("Digite o nome a ser removido:")
#if nome_remover in nomes:
#    nomes.remove(nome_remover)
#    print(f"{nome_remover} foi removido da lista.")
#else:
#    print(f"{nome_remover} não está na lista.")
print(f" não está na lista.")

elif opcao == "3":
print("\nLista de Nomes:")
for nome in nomes:
#   print(nome)
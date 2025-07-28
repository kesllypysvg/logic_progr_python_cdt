print("minha lista de desejos\n")
MAINLIST_ARQUIVO = "meus_desejos.txt"
desejos = []

try:
    with open(MAINLIST_ARQUIVO, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            desejos.append(linha.strip())
            print(f"Meus desejos foram carregados do arquivo '{MAINLIST_ARQUIVO}'!\n")
            except FileNotFoundError:
print("parece que é sua primeira vez! Vamos criar sua lista de desejos.\n")
except Exception as e:
print(f"Ocorreu um erro ao carregar os desejos: {e}")

def salvar_desejos(Lista_de_desejos:)
try:
    with open(MAINLIST_ARQUIVO, 'w', encoding='utf-8') as arquivo:
        for desejo in Lista_de_desejos:
            arquivo.write(desejo + "\n")
            print("\n Seus desejos foram salvos com sucesso!")
            except Exception as e:
print(f"\n Erro ao salvar seus desejos: {e}")

while True:
    print("\n O que voce quer fazer?")
    print("1 - Adicionar um novo desejo")
    print("2 - Ver meus desejos")
    print("3 - Sair")
    escolha = input("Digite sua opção (1, 2 ou 3): ")
    if escolha == "1":
        novo_desejo = input("Qual é o seu novo desejo para o futuro?: ")
        if novo_desejo.strip():
            desejos.append(novo_desejo.strip())
            salvar_desejos(desejos)
        else:
            print(" Desejo não pode ser vazio! tente novamente.")
            elif escolha == "2":
    print("n\ Seus desejos para o futuro")
    if not desejos:
        print("n\ Ainda não há desejos na sua lista. Que tal adicionar um?!")
        else:
for i, desejo in enumerate(desejos):
    print(f"{i+1} - {desejo}")
    elif escolha == "3":
    print("")



                   


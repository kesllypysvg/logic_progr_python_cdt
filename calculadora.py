##MVC
#Model
### vai conter a lógica de cálculo
# da cálculadora.

#View
### vai exibir o resultado na tela.

#controller
### vai receber as entradas do
#  usuário e interagir com o modelo.

 def mostrar_menu()
 print("\n---Calculadora---")
 print("1. Adição")
print("2. Subtração")
print("5. Sair")
print(--------------------)

def obter_numeros():
 while True:
  try:
   num1= float(input("Digite o primeiro número: "))
   num2= float(input("Digite o segundo número: "))
   return num1, num2
  except ValueError:
   print
  
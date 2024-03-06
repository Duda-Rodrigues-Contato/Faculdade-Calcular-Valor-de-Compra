#Atividade para usar o if...elif...else. Nessa atividade, iremos fazer um programa que ao colocarmos o valor, dá se temos desconto ou não
#Devemos, nessa atividade, fazer um caso para evitar se alguém colocar um valor negativo ou R$0
valordacompra = float(input("Insira aqui o valor de sua compra:"))
if valordacompra >= 100.0: #Lembrar de colocar ponto quando for tratar de dinheiro, por exemplo (coisas reais)
    print("Você é elegível para um desconto!")
elif valordacompra <= 0:
    print("Esse valor não é aplicável.") 
else:
    print("Valor total de compra insuficiente para um desconto.")
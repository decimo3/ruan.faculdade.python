# Imprimir algo na tela, pegar a entrada do usuário e Imprimir para ele
print("Olá mundo!")
print("Esse não é o meu primeiro código Python, porém estarei reaprendendo novamente.")
print("Qual é o seu nome?")
nome = input()
print(f"Olá {nome}")


# Entrar em um loop e sair dele após uma séries de condições
a = 10
b = 5
while a > b:
    print("Oi")
    b = b + 1

# para usar o comando 'for' é necessário informar um objeto de lista (arrays, texto, ou array de números com o método 'range()')
# usando 'for' para iterar em uma lista de números através da função 'range()'
lista = range(5) # A função 'range()' cria uma lista de números 0 a 5 e o for faz a iteração nessa lista de números.
for l in lista:
    print(l)
# usando 'for' para iterar em um texto:
for x in nome:
    print(x)

# Estrutura de decisão
codigo_compra = 5111
if codigo_compra == 5222:
    print("Compra à vista.")
elif codigo_compra == 5333:
    print("Compra à prazo no boleto.")
elif codigo_compra == 5444:
    print("Compra à prazo no cartão.")
else:
    print("Código não cadastrado")

# Conversão implícita
qtde_faltas = int(input("Digite a quantidade de faltas: "))
media_final = float(input("Digite a média final: "))

if qtde_faltas <= 5 and media_final >= 7:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!") 

"""
As aspas triplas possibilitam quebrar a linha do texto.
As aspas triplas também podem ser usadas para criar comentários de várias linhas em Python.
"""

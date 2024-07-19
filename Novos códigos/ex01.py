# Algoritmo que calcula a média de três números e trabalha com strings

# Declaração de variáveis
numero1 = 0
numero2 = 0
numero3 = 0
media = 0.0
frase = ""
lista_palavras = []

# Função para ler um número inteiro do usuário
def ler_numero(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            return numero
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

# Função para ler uma string do usuário
def ler_string(mensagem):
    return input(mensagem)

# Leitura dos três números
numero1 = ler_numero("Digite o primeiro número: ")
numero2 = ler_numero("Digite o segundo número: ")
numero3 = ler_numero("Digite o terceiro número: ")

# Cálculo da média
lista_numeros = [numero1, numero2, numero3]
media = sum(lista_numeros) / len(lista_numeros)

# Leitura de uma frase do usuário
frase = ler_string("Digite uma frase: ")

# Leitura de várias palavras do usuário (usando um loop)
num_palavras = int(input("Quantas palavras deseja inserir? "))
for i in range(num_palavras):
    palavra = ler_string(f"Digite a palavra {i+1}: ")
    lista_palavras.append(palavra)

# Exibição dos resultados
print(f"\nA média dos números {lista_numeros} é {media:.2f}")
print(f"A frase digitada foi: {frase}")
print(f"As palavras digitadas foram: {lista_palavras}")

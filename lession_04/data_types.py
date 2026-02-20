# String data type

# literal assignment
import math
first = "Breno"
last = "Cavalcante"

# Tipo String ---------------------------------------------------------------------

# print(type(first))
# print(type(first) == str)  # True
# print(isinstance(first, str))  # True, é uma instancia da classe string

# Construcor function str() -------------------------------------------------------

# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatenando strings -------------------------------------------------------------

# fullname = first + " " + last
# print(fullname)

# fullname += "!"
# print(fullname)

# Casting de um numero para string -------------------------------------------------

# decade = str(1980)

# print(type(decade))
# print(decade)

# statement = "I like rock music from the " + decade + "s."
# print(statement)

# Multipas Linhas -----------------------------------------------------------
# multiline = '''
# # Hey, how are you?

# # I was just checking in..
# #                             All good?

# # '''
# print(multiline)

# Caractere especial de escape
# frase = 'I\'m back at work!\t Hey!\n\nWhere\'s this at\\located?'
# print(frase)

# String methods ---------------------------------------------------------

# print(first)
# print(first.lower())
# print(first.upper())
# print(first)

# print(multiline.title()) # deixa a primeira letra da palavara Maiúscula
# print(multiline.replace("good", "ok")) # substitui a palavra fornecida
# print(multiline)

# texto_com_espaco = "     hello world!     "

# print(len(texto_com_espaco)) # exibe o tamanho total da string incluindo os espaços
# print(len(texto_com_espaco.strip())) # remove os espaços em branco
# print(len(texto_com_espaco.lstrip())) # remove os espaços do lado esquerdo
# print(len(texto_com_espaco.rstrip())) # remove os espaços do lado direito

# Construindo um menu ------------------------------------------------------------

# titulo = "menu".upper()  # deixa todos caracteres maiusculos
# print(titulo.center(20, "="))  # centralisa a variavel e preenche com simbolo
# print("Café".ljust(16, ".") + "1$".rjust(4))

# justifica esquerda ljust(), justifica direita rjust()
# print("Pão de Queijo".ljust(16, ".") + "1.2$".rjust(4))

# justifica esquerda ljust(), justifica direita rjust()
# print("Misto Quente".ljust(16, ".") + "2.5$".rjust(4))

# Índice de String --------------------------------------------------------------

# print(first[1:-1])  # exibe o segundo e o antepenúltimo
# print(first[0:])  # percorre e exibe do inicio até o fim da string

# Métodos que retornam boleano
# a string começa com a letra "B" (sensitive case)
# print(first.startswith("B"))
# a string termina com a letra "a" (sensitive case)
# print(first.endswith("a"))

# Tipos de dados boleano -------------------------------------------------------
valor = True
x = bool(False)  # função construtora

print("É uma instância: ", isinstance(valor, bool))
print(type(valor), type(x))
print(valor, x)

# tipo int ---------------------------------------------------------------------
preco = 100
melhor_preco = int(80)
print(type(preco))
print(isinstance(melhor_preco, int))

# tipo float ---------------------------------------------------------------------
gpa = 3.28
y = float(1.14)
print(type(gpa))
print(isinstance(y, float))

# tipo complex -------------------------------------------------------------------
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)  # valor real
print(comp_value.imag)  # valor imaginario

# Built-in functions for numbers --------------------------------------------------
print("\n" + 100 * "=")
print(abs(gpa))  # função para obter um valor absoluto de um numero
print(round(gpa))  # função que arredonda o valor para o inteiro mais proximo
print(round(gpa, 1))  # podemos passar o numero de casas por parâmetro

# Modulo math ---------------------------------------------------------------------
print("\n" + 100 * "=")
print(math.pi)
print(math.sqrt(64))
print(math.pow(3, 3))

# Casting de string para inteiro ---------------------------------------------------
print("\n" + 100 * "=")
CEP_STRING = "10001"
CEP_INT = int(CEP_STRING)
print(CEP_INT, type(CEP_INT))

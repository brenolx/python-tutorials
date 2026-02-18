# String data type

# literal assignment
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
multiline = '''
# Hey, how are you?

# I was just checking in..
#                             All good?

# '''
# print(multiline)

# Caractere especial de escape
#frase = 'I\'m back at work!\t Hey!\n\nWhere\'s this at\\located?'
#print(frase)

# String methods ---------------------------------------------------------

# print(first)
# print(first.lower())
# print(first.upper())
# print(first)

#print(multiline.title()) # deixa a primeira letra da palavara Maiúscula
#print(multiline.replace("good", "ok")) # substitui a palavra fornecida
#print(multiline)

#texto_com_espaco = "     hello world!     "

#print(len(texto_com_espaco))
#print(len(texto_com_espaco.strip())) # remove os espaços em branco
#print(len(texto_com_espaco.lstrip())) # remove os espaços do lado esquerdo
#print(len(texto_com_espaco.rstrip())) # remove os espaços do lado direito

# Construindo um menu ------------------------------------------------------------

titulo = "menu".upper() # deixa todos caracteres maiusculos
print(titulo.center(20, "=")) # centralisa a variavel e preenche com simbolo
print("Café".ljust(16, ".") + "1$".rjust(4))
print("Pão de Queijo".ljust(16, ".") + "1.2$".rjust(4)) # justifica esquerda ljust(), justifica direita rjust()
print("Misto Quente".ljust(16, ".") + "2.5$".rjust(4))  # justifica esquerda ljust(), justifica direita rjust()

# Índice de String 
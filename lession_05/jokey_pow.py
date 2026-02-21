import sys
import random
from enum import Enum


class PPT(Enum):
    PEDRA = 1
    PAPEL = 2
    TESOURA = 3


escolha_usu = int(
    input('\nDigte... \n[1]Pedra, \n[2]Papel, \n[3]Tesoura: \n\n->'))

if escolha_usu < 1 or escolha_usu > 3:
    sys.exit("Opção Inválida. Escolha entre 1, 2 ou 3!")

escolha_cpu = int(random.choice("123"))

print('')
print('Escolha Jogador: ' + str(PPT(escolha_usu).name.title()))
print('Escolha CPU: ' + str(PPT(escolha_cpu).name.title()))
print('')


if escolha_usu == 1 and escolha_cpu == 3:
    print("🎉 VOCE VENCEU!")
elif escolha_usu == 2 and escolha_cpu == 1:
    print("🎉 VOCE VENCEU!")
elif escolha_usu == 3 and escolha_cpu == 2:
    print("🎉 VOCE VENCEU!")
elif escolha_usu == escolha_cpu:
    print("🤝 O Jogo Empatou!")
else:
    print("🤖 CPU VENCEU!")

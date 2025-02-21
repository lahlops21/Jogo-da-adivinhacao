print('Estou pensando em um número entre 0 e 15... ')
print('Quero ver se consegue adivinhar qual foi...')
print('='* 40)
print('')
from random import randint
computador = randint(0,100)

palpite = 0
acertou = False

while acertou == False:
  jogador = int(input('Escolha um número entre 0 e 100: '))
  palpite += 1
  if jogador == computador:
    acertou = True
  else:
    if jogador > computador:
      print('O número é menor... Tente outra vez!')
    elif jogador < computador:
      print('O número é maior... Tente outra vez!')
print(f'Acertou com {palpite} tentativas!')




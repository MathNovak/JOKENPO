import random
import time

jokenpô = ['pedra', 'papel', 'tesoura']
escolha_computador = random.choice(jokenpô).capitalize()


escolha_usuário_numero = str(input('[1]Pedra - [2]Papel - [3]Tesoura: ').strip().capitalize())
if escolha_usuário_numero == '1':
    escolha_usuário = 'Pedra'
elif escolha_usuário_numero == '2':
    escolha_usuário = 'Papel'
elif escolha_usuário_numero == '3':
    escolha_usuário = 'Tesoura'


print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO')

if escolha_usuário == 'Pedra' and escolha_computador == 'Pedra':
    resultado = 'EMPATE!'
elif escolha_usuário == 'Pedra' and escolha_computador == 'Papel':
    resultado = 'Você perdeu!'
elif escolha_usuário == 'Pedra' and escolha_computador == 'Tesoura':
    resultado = 'Você ganhou!'
elif escolha_usuário == 'Papel' and escolha_computador == 'Pedra':
    resultado = 'Você ganhou!'
elif escolha_usuário == 'Papel' and escolha_computador == 'Papel':
    resultado = 'EMPATE!'
elif escolha_usuário == 'Papel' and escolha_computador == 'Tesoura':
    resultado = 'Você perdeu!'
elif escolha_usuário == 'Tesoura' and escolha_computador == 'Tesoura':
    resultado = 'EMPATE!'
elif escolha_usuário == 'Tesoura' and escolha_computador == 'Pedra':
    resultado = 'Você perdeu!'
elif escolha_usuário == 'Tesoura' and escolha_computador == 'Papel':
    resultado = 'Você ganhou!'
print('-=-'*10)
print(f'Computador escolheu: {escolha_computador}')
print(f'Você escolheu: {escolha_usuário}')
print(resultado)
print('-=-'*10)
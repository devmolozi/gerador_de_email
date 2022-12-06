import random
import time


def gera_email(nome: str, sobrenome: str):
    print('')
    numero = random.randint(1, 9999)
    print('')
    ponto = '.'
    if numero > 9999:
        return None
    if len(nome) > 0 and len(sobrenome) > 0:
        print('Aguarde, estamos gerando seu e-mail...')
        print('')
        time.sleep(4)
        print('----------------------------------------------------------')
        return f"E-mail gerado com sucesso! | {nome.lower()+sobrenome.lower()+f'{ponto}{numero}@gmail.com |'}"
    else:
        return 'Erro! Você não preencheu os dois campos acima :/'

while True:
    print('')
    print('Abrindo sessão...')
    time.sleep(3)
    print('')
    nome = str(input('Digite seu primeiro nome: '))
    print('')
    sobrenome = str(input('Digite seu segundo nome: '))
    print(gera_email(sobrenome, nome))

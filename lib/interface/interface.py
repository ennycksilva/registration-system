from .colors import COLORS

def read_int(message):
    while True:
        try:
            number = int(input(message))
        except ValueError:
            print(f'{COLORS["red"]}ERRO! Digite um número inteiro válido.{COLORS["reset"]}')
        except KeyboardInterrupt:
            print(f'{COLORS["red"]}\nERRO! O usuário preferiu encerrar o programa.{COLORS["reset"]}')
            return None
        else:
            return number

def line(size, color='reset'):
    try:
        print(f'{COLORS[color]}{"—" * size}{COLORS["reset"]}')
    except KeyError:
        print(f'{COLORS["red"]}ERRO! A cor inserida é inválida.{COLORS["reset"]}')

def header(message):
    line(42, 'blue')
    print(f'{message}'.center(42))
    line(42, 'blue')

def menu(options):
    header('MENU PRINCIPAL')
    for position, item in enumerate(options, start=1):
        print(f'{COLORS["yellow"]}{position} - {COLORS["reset"]}{COLORS["green"]}{item}{COLORS["reset"]}')
    while True:
        option = read_int('Sua opção: ')
        if option is None:
            return None
        if option < 1 or option > len(options):
            print(f'{COLORS["red"]}ERRO! A opção escolhida não existe.{COLORS["reset"]}')
        else:
            return option


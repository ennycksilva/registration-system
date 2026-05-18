def read_int(message):
    while True:
        try:
            number = int(input(message))
        except ValueError:
            print('ERRO! Digite um número inteiro válido.')
        except KeyboardInterrupt:
            print('\nERRO! O usuário preferiu encerrar o programa.')
            return None
        else:
            return number

def line(size):
    print('—' * size)

def header(message):
    line(42)
    print(f'{message}'.center(42))
    line(42)

def menu(list):
    header('MENU PRINCIPAL')
    for position, item in enumerate(list, start=1):
        print(f'{position} - {item}')
    option = read_int('Sua opção: ')
    return option



# -*- coding: utf-8 -*-


def protected(func):

    def wrapper(password):

        if password == 'platzi':
            return func()
        else:
            print('La contraseña es incorrecta')

    return wrapper


def protected_func():
    print('Tu contraseña es correcta.')


if __name__ == '__main__':
    password = str(raw_input('Ingresa tu contraseña: '))
    wrapper = protected(protected_func)
    wrapper(password)
    protected_func(password)

while True:
    par = int(input('informe o numero par do buraco:'))
    tacadas = int(input('informe o numero de tacadas:'))
    birdie = par - 1
    eagle = par -2
    deagle = par -3
    bogey = par + 1
    resp = ''
    if tacadas == 1:
        print('FOI UM HOLE-IN-ONE!!!')
    elif par == tacadas:
        print('FOI UM PAR !!!')
    elif tacadas == birdie:
        print("foi um birdie!!")
    elif tacadas == eagle:
        print("foi um eagle!!")
    elif tacadas == deagle:
        print("foi um double eagle!!")
    elif tacadas == bogey:
        print('foi um bogey!')
    elif tacadas > bogey:
        print('foi um double bogey ;_;')
    else:
        print('double eagle')
    resp = input('deseja sair?(s/n)')
    if resp == 's' or 'sim':
        break
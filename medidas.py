def entrada():
    while True:
        e = input('_')
        if  e.isalpha():
            print('Comando invalido. Utiliza somente números')
            continue
        elif e.isspace():
            print('Comando invalido. Utiliza somente números em espaços')
        if e.isnumeric():
            e = int(e)
            return e
        elif not e.isdigit():
            e = float(e)
            return e

def continuar():
    while True:
        e = input('Deseja continuar ? [S] [N]')
        if e.isnumeric():
            print('Comando invalido.')
            continue
        if not e =='s' and not  e == 'n':
            print('Comando invalido.')
        elif e == 's':
            return e
        else:
            return e

def polegadas():
    print('\n')
    print(' █▀█ █▀█ █░░ █▀▀ █▀▀ ▄▀█ █▀▄ ▄▀█ █▀\n'
          ' █▀▀ █▄█ █▄▄ ██▄ █▄█ █▀█ █▄▀ █▀█ ▄█')
    print('\n')
    divicao()
    while True:
        print('[1] Polegadas → Milímetros\n'
              '[2] Polegadas → Centímetros\n'
              '[3] Polegadas → Metros\n'
              '[4] Sair')
        e = entrada()
        if e < 5:
            if e == 1:
                p_milimetros()
                break
            elif e == 2:
                p_centimetros()
                break
            elif e == 3:
                p_m()
                break
            else:
                menu()
        else:
            print('Comando Inválido')
            continue
def p_milimetros():
    print('Quantas Polegadas você quer converter em Milímetros ?')
    p = entrada()
    if p == int(p):
        mi = p * 25.4
        print(f'{p} Polegadas é equivalente a {mi:.2f} Milímetros')
    else:
        mi = p * 254
        print(f'{p} Polegadas é equivalente a {mi:.2f} Milímetros')
    if continuar() == 's' :
        p_milimetros()
    else:
        polegadas()
def p_centimetros():
    print("Quantas Polegadas você quer converter em Centímetros ?")
    p =entrada()
    if p == int(p):
        c = p * 2.54
        print(f'{p} Polegadas é equivalente a {c:.2f} Centímetros')
    else:
        c = p * 25.4
        print(f'{p} Polegadas é equivalente a {c} Centímetros')
    if continuar() == 's' :
        p_centimetros()
    else:
        polegadas()
def p_m():
    print('Quantas Polegadas você quer converter em Metros ?')
    p = entrada()
    if p == int(p):
        m = p / 39.37
        print(f'{p} Polegadas é equivalente a {m:.2f} Metros.')
    else:
        m = p / 3.937
        print(f'{p} Polegadas é equivalente a {m:.2f} Metros.')
    if continuar() =='s':
        p_m()
    else:
        polegadas()

def milimetros():
    print('\n')
    print(' █▀▄▀█ █ █░░ █ █▀▄▀█ █▀▀ ▀█▀ █▀█ █▀█ █▀\n'
          ' █░▀░█ █ █▄▄ █ █░▀░█ ██▄ ░█░ █▀▄ █▄█ ▄█')
    print('\n')
    divicao()
    while True:
        print('[1] Milímetros → Polegadas\n'
              '[2] Milímetros → Centímetros\n'
              '[3] Milímetros → Metros\n'
              '[4] Sair')
        e = entrada()
        if e < 5:
            if e == 1:
                milimetros_p()
                break
            elif e == 2:
                milimetros_centimetros()
                break
            elif e == 3:
                milimetros_m()
                break
            else:
                menu()
        else:
            print('Comando Inválido')
            continue
def milimetros_p():
    print('Quantos Milímetros você quer converter em Polegadas ?')
    mi = entrada()
    if mi == int(mi):
        p = mi / 25.4
        print(f'{mi} Milímetros é equivalente a {p:.0f} Polegadas')
    else:
        p = mi / 2.54
        print(f'{mi} Milímetros é equivalente a {p:.2f} Polegadas')
    if continuar() =='s':
        milimetros_p()
    else:
        milimetros()
def milimetros_centimetros():
    print('Quantos Milimetros você quer converter em Centímetros ?')
    mi = entrada()
    if mi == int(mi):
        c = mi / 10
        print(f'{mi} Milímetros é equivalente a {c:.2f} Centímetros')
    else:
        c = mi * 1
        print(f'{mi} Milímetros é equivalente a {c:.2f} Centímetros.')
    if continuar() =='s':
        milimetros_centimetros()
    else:
        milimetros()
def milimetros_m():
    print('Quantos milimetros Você quer converter em metros ?')
    mi = entrada()
    if mi == int(mi):
        m = mi / 1000
        print(f'{mi} Milímetros é equivalente a {m:.2f} Metros')
    else:
        m = mi / 100
        print(f'{mi} Milímetros é equivalente a {m:.2f} Metros')
    if continuar() == 's':
        milimetros_m()
    else:
        milimetros()

def centimetros():
    print('\n')
    print(' █▀▀ █▀▀ █▄░█ ▀█▀ █ █▀▄▀█ █▀▀ ▀█▀ █▀█ █▀█ █▀\n'
          ' █▄▄ ██▄ █░▀█ ░█░ █ █░▀░█ ██▄ ░█░ █▀▄ █▄█ ▄█')
    print('\n')
    divicao()
    while True:
        print('[1] Centimetros → Polegadas\n'
              '[2] Centimetros → Milímetros\n'
              '[3] Centimetros → Metros\n'
              '[4] Centimetros → Quilometros\n'
              '[5] Sair')
        e = entrada()
        if e < 6:
            if e == 1:
                centimetros_p()
                break
            elif e == 2:
                centimetros_milimetros()
                break
            elif e == 3:
                centimetros_m()
                break
            elif e == 4:
                centimetros_k()
                break
            else:
                menu()
        else:
            print('Comando Inválido')
            continue
def centimetros_p():
    print('Quantos Centímetros você quer converter em Polegadas.')
    c = entrada()
    if c == int(c):
        p = c / 2.54
        print(f'{c} Centímetros é equivalente a {p:.2f} Polegadas.')
    else:
        p = c * 3.937
        print(f'{c} Centímetros é equivalente a {p} Polegadas')
    if continuar() == 's':
        centimetros_p()
    else:
        centimetros()
def centimetros_milimetros():
    print("Quantos Centímetros você quer converter em Milímetros ?")
    c = entrada()
    if c == int(c):
        mi = c * 10
        print(f'{c} Centímetros é equivalente a {mi:.0f} Milímetros')
    else:
        mi = c *100
        print(f'{c} Centímetro é equivalente a {mi:.0f} Milímetros')
    if continuar() =='s':
        centimetros_milimetros()
    else:
        centimetros()
def centimetros_m():
    print("Quantos Centímetros você quer converter em Metros ?")
    c = entrada()
    if c == int(c):
        m = c / 100
        print(f'{c} Centimetros é equivalente a {m:.1f} Metros')
    else:
        m = c / 10
        print(f'{c} Centimetos é equivalente a {m:.2f} Metros')
    if continuar() == 's':
        centimetros_m()
    else:
        centimetros()
def centimetros_k():
    print('Quantos Centímetos você quer converter em Quilometros ?')
    c = entrada()
    k = c /100000
    print(f'{c} Centímetros é equivalente a {k} Quilometros.')
    if continuar() == 's':
        centimetros_k()
    else:
        centimetros()

def metros():
        print('\n')
        print(' █▀▄▀█ █▀▀ ▀█▀ █▀█ █▀█ █▀\n'
              ' █░▀░█ ██▄ ░█░ █▀▄ █▄█ ▄█')
        print('\n')
        divicao()
        while True:
            print('[1] Metros → Polegadas\n'
                  '[2] Metros → Milímetros\n'
                  '[3] Metros → Centimetros'
                  '[4] Metros → Quilometros\n'
                  '[5] Metros → Milhas\n'
                  '[6] Metros → Milhas Náuticas\n' 
                  '[7] Sair')
            e = entrada()
            if e < 8:
                if e == 1:
                    m_p()
                    break
                elif e == 2:
                    m_milimetros()
                    break
                elif e == 3:
                    m_centimetros()
                    break
                elif e == 4:
                    m_k()
                    break
                elif e == 5:
                    m_milhas()
                    break
                elif e == 6 :
                    metros_milhas_nauticas()
                else:
                    menu()
            else:
                print('Comando Inválido')
                continue
def m_p():
    print('Quantos Metros você quer converter em Polegadas ?')
    m = entrada()
    if m == int(m):
        p = m * 39.37
        print(f'{m} Metros é equivalente a {p:.2f} Polegadas')
    else:
        p = m * 394
        print(f'{m} Metros é equivalente a {p:.2f} Polegadas')
    if continuar() =='s':
        m_p()
    else:
        metros()
def m_milimetros():
    print('Quantos Metros você quer converter em Milímetros ?')
    m = entrada()
    if m == int(m):
        mi = m * 1000
        print(f'{m} Metros é equivalente a {mi:.0f} Milímetros.')
    else:
        mi = m * 10000
        print(f'{m} Metros é equivalente a {mi:.0f} Milímetros')
    if continuar() =='s':
        m_milimetros()
    else:
        metros()
def m_centimetros():
    print('Quantos Metro você quer converter em Centimetro?')
    m = entrada()
    if m == int(m):
        c = m * 100
        print(f'{m} Metros é equivalente a {c:.1f} Centimetros')
    else:
        c = m * 1000
        print(f'{m} Metros é equivalente a {c:.2f} Centímetros')
    if continuar() == 's':
        m_centimetros()
    else:
        metros()
def m_k():
    print('Quantos Metro você quer converter em Quilometros ?')
    m = entrada()
    if m == int(m):
        k = m / 1000
        print(f'{m} Metros é equivalente a {k} Quilometros')
    else:
        k = m / 990
        print(f'{m} Metros é equivalente a {k:.3f} Quilometros')
    if continuar() == 's':
        m_k()
    else:
        metros()
def m_milhas():
    print('Quantos Metro você quer converter em Milhas ?')
    m = entrada()
    if m == int(m):
        milhas = m / 1690
        print(f'{m} Metros é equivalente a {milhas:.2f} Milhas')
    else:
        milhas = m / 169
        print(f'{m} Metros é equivalente a {milhas:.3f} Milhas')
    if continuar() == 's':
        m_milhas()
    else:
        metros()
def metros_milhas_nauticas():
    print('Quantos Metro você quer converter em Milhas Náuticas ?')
    m = entrada()
    if m == int(m):
        milhas = m / 1852
        print(f'{m} Metros é equivalente a {milhas:.2f} Milhas Nauticas')
    else:
        milhas = m / 185
        print(f'{m} Metros é equivalente a {milhas:.3f} Milhas Náuticas')
    if continuar() == 's':
        metros_milhas_nauticas()
    else:
        metros()

def quilometros():
        print('\n')
        print('█▀█ █░█ █ █░░ █▀█ █▀▄▀█ █▀▀ ▀█▀ █▀█ █▀█ █▀\n'
              '▀▀█ █▄█ █ █▄▄ █▄█ █░▀░█ ██▄ ░█░ █▀▄ █▄█ ▄█')



        print('\n')
        divicao()
        while True:
            print('[1] Quilometros → Metros\n'
                  '[2] Quilometros → Milhas\n'
                  '[3] Quilometros → Milhas Náuticas\n'
                  '[4] Sair')
            e = entrada()
            if e < 5:
                if e == 1:
                    k_m()
                    break
                elif e == 2:
                    k_milhas()
                    break
                elif e == 3:
                    k_milhas_nauticas()
                    break
                else:
                    menu()
            else:
                print('Comando Inválido')
                continue
def k_m():
    print('Quantos Quilometros você quer converter em Metros ?')
    k = entrada()
    if k == int(k):
        m = k * 1000
        print(f'{k} Quilometros é equivalente a {m} Metros')
    else:
        m = k * 990
        print(f'{k} Quilometros é equivalente a {m:.1f} Metros')
    if continuar() == 's':
        k_m()
    else:
        pass
def k_milhas():
    print('Quantos Quilometros você quer converter em Milhas')
    k = entrada()
    if k == int(k):
        milha = k / 1.609
        print(f'{k} Quilometos é equivalente a {milha:.2f} Milhas.')
    else:
        milha = k * 6.214
        print(f'{k} Quilometros é equivalente a {milha:.2f} Milhas')
    if continuar() == 's':
        k_milhas()
    else:
        pass
def k_milhas_nauticas():
    print('Quantos Quilometros você quer converter em Milhas Náuticas ?')
    k = entrada()
    if k == int(k):
        milhas = k / 1.852
        print(f'{k} Quilometros é equivalente a {milhas:.2f} Milhas Nauticas')
    else:
        milhas = k * 5.4
        print(f'{k} Quilometros é equivalente a {milhas:.2f} Milhas Náuticas')
    if continuar() == 's':
        k_milhas_nauticas()
    else:
        pass

def Milhas():
    print('\n')
    print('█▀▄▀█ █ █░░ █░█ ▄▀█ █▀\n'
          '█░▀░█ █ █▄▄ █▀█ █▀█ ▄█')
    print('\n')
    divicao()
    while True:
        print('[1] Milhas → Metros\n'
              '[2] Milhas → Quilometros\n'
              '[3] Milhas → Milhas Náuticas\n'
              '[4] Sair')
        e = entrada()
        if e < 5:
            if e == 1:
                milhas_m()
            elif e == 2:
                milhas_k()
            elif e == 3:
                milhas_milhas_nauticas()
            else:
                menu()
        else:
            print('Comando Inválido')
            continue
def milhas_m():
    print('Quantas Milhas você quer converter em Metros ?\nUtiliza somente uma casa decimal')
    milhas = entrada()
    if milhas == int(milhas):
        m = milhas * 1609
        print(f'{milhas} Milhas é equivalente a {m:.2f} Metros')
    else:
        m = milhas * 16093
        print(f'{milhas} Milhas é equivalente a {m:.1f} Metros')
    if continuar() == 's':
        milhas_m()
    else:
        Milhas()
def milhas_k():
    print('Quantas Milhas você quer converter em Quilometros ?')
    m = entrada()
    if m == int(m):
        k = m * 1.609
        print(f'{m} Milhas é equivalente a {k:.2f} Quilometros')
    else:
        k = m * 16.093
        print(f'{m} Milhas é equivalente a {k:.2f} Quilometros')
    if continuar() == 's':
        milhas_k()
    else:
        Milhas()
def milhas_milhas_nauticas():
    print('Quantas Milhas você quer converter em Milhas Náuticas ?')
    m = entrada()
    if m == int(m):
        milha = m / 1.151
        print(f'{m} Milhas é equivalente a {milha:.2f} Minhas Náuticas')
    else:
        milhas = m * 8.69
        print(f'{m} Milhas é equivalente a {milhas:.2f} Milhas Náuticas')
    if continuar() == 's':
        milhas_milhas_nauticas()
    else:
        Milhas()

def Milhas_nauticas():
    print('\n')
    print('█▀▄▀█ █ █░░ █░█ ▄▀█ █▀   █▄░█ ▄▀█ █░█ ▀█▀ █ █▀▀ ▄▀█ █▀\n'
          '█░▀░█ █ █▄▄ █▀█ █▀█ ▄█   █░▀█ █▀█ █▄█ ░█░ █ █▄▄ █▀█ ▄█')
    print('\n')
    divicao()
    while True:
        print('[1] Milhas Nauticas → Metros\n'
              '[2] Sair')
        e = entrada()
        if e < 3:
            if e == 1:
                milhas_nauticas_metros()
                break
            else:
                menu()
        else:
            print('Comando Inválido')
            continue
def milhas_nauticas_metros():
    print('Quantas Milhas Náuticas você quer converter em Metros ?\nUtiliza somente uma casa decimal')
    milhas = entrada()
    if milhas == int(milhas):
        m = milhas * 1852
        print(f'{milhas} Milhas Nauticas é equivalente a {m:.2f} Metros')
    else:
        m = milhas * 18520
        print(f'{milhas} Milhas Nauticas é equivalente a {m:.1f} Metros')
    if continuar() == 's':
        milhas_nauticas_metros()
    else:
        pass

def divicao():
    print('#' * 75)
    print('#' * 75)
def menu():
    print('█▀▀ █▀█ █▄░█ █░█ █▀▀ █▀█ █▀ █▀█ █▀█   █▀▄ █▀▀   █▀▄▀█ █▀▀ █▀▄ █ █▀▄ ▄▀█ █▀')
    print('█▄▄ █▄█ █░▀█ ▀▄▀ ██▄ █▀▄ ▄█ █▄█ █▀▄   █▄▀ ██▄   █░▀░█ ██▄ █▄▀ █ █▄▀ █▀█ ▄█')
    print('\n')
    divicao()
    while True:
        print('[1] Polegadas\n'
              '[2] Milímetros\n'
              '[3] Centímetros\n'
              '[4] Metros\n'
              '[5] Quilometros\n'
              '[6] Milhas\n'
              '[7] Milhas Náuticas\n'
              '[8] Sair')
        e = entrada()
        if e < 9:
            if e == 1 :
               polegadas()
               break
            elif e == 2:
                milimetros()
            elif e == 3 :
                centimetros()
            elif e == 4 :
                metros()
            elif e == 5 :
                quilometros()
            elif e == 6 :
                Milhas()
            elif e == 7 :
                Milhas_nauticas()
            else:
                break
        else:
            print('comando invalido')


menu()
#menu geral

def menu():
    print('[1] Precificação por porcentagem\n'
          '[2] Porcentagem sobre produto\n'
          '[3] Aplicação de desconto\n'
          '[4] Sair')
    e = input('____ ')
    print('______')
    if e.isdigit():
        e = int(e)
        while e <=4:
            if e == 4:
                print('Obrigado')
                exit()
                break
            if e == 1:
                porcentagem()
            if e == 2 :
                porcentagem_lucro()
                menu()
            if e == 3:
                desconto()
                menu()

        else:
            print('comando invalido')
            menu()
    else:
        print('comando invalido')
        menu()


# Precificação sobre a compra do produto
def porcentagem():
    print('[1] 15%\n'
          '[2] 30%\n'
          '[3] 50%\n'
          '[4] 70%\n'
          '[5] Voltar')
    e = input('escolha')
    if e.isdigit():
        e = int(e)
        while e <=5:
            if e == 1 :
                p15()
            elif e == 2 :
                p30()
            elif e == 3 :
                p50()
            elif e == 4 :
                p70()
            else:
                menu()
        else:
            print('comando invalido')
    else:
        print('comando invalido')
def p15():
    v = input('Valor do produtor\n'
              '_____________    ')
    if not v.isdigit():
        v =  float(v)
        p = (v*15)/100
        print(f'15 % do produto {v} é : {p}\n'
              f'Com o valor de venda de {v+p}')
        print('='*30)
        e = input('Deseja continuar? [s] [n]')
        while e == 's' or e == 'n':
            if e == 's':
                p15()
            else:
                porcentagem()
        else:
            print('comando invalido')
    else:
        print('comando invalido')
def p30():
    v = input('valor')
    if v.isdigit():
        v =  float(v)
        p = (v*30)/100
        print(f'30 % de {v} é : {p}')
        print('='*30)
        e = input('Deseja continuar? [s] [n]')
        while e == 's' or e == 'n':
            if e == 's':
                p30()
            else:
                porcentagem()
        else:
            print('comando invalido')
    else:
        print('comando invalido')
def p50():
    v = input('valor')
    if v.isdigit():
        v =  float(v)
        p = (v*50)/100
        print(f'50 % de {v} é : {p}')
        print('='*30)
        e = input('Deseja continuar? [s] [n]')
        while e == 's' or e == 'n':
            if e == 's':
                p50()
            else:
                porcentagem()
        else:
            print('comando invalido')
    else:
        print('comando invalido')
def p70():
    v = input('valor')
    if v.isdigit():
        v =  float(v)
        p = (v*70)/100
        print(f'70 % de {v} é : {p}')
        print('='*30)
        e = input('Deseja continuar? [s] [n]')
        while e == 's' or e == 'n':
            if e == 's':
                p50()
            else:
                porcentagem()
        else:
            print('comando invalido')
    else:
        print('comando invalido')

# Lucro sobre a venda do produto
def porcentagem_lucro():
    p = input('Qual o valor de compra do produto ? ')
    v = input('Qual o valor de venda do produto ?')
    if not p.isnumeric() and not v.isnumeric():
        p = float(p)
        v = float(v)
        l = (v-p)*100/p
        print(f'o valor do produto é {p} você vende por {v} e tem {l:.2f}% de lucro')
        e = input('Deseja continuar? [s] [n]')
        while e == 's' or e == 'n':
            if e == 's':
                porcentagem_lucro()
            else:
                menu()
        else:
            print('comando invalido')
    else:
        print('valor invalido, coloque os centravos ou .00')
        porcentagem_lucro()
# Gerador de desconto.
def desconto():
    p = input('Qual o valor de Atual de venda ? ')
    v = input('Qual porcentagem deseja aplicar ?\n'
              'Coloque .00\n'
              '____')
    if not p.isnumeric() and not v.isdigit():
        p = float(p)
        v = float(v)
        d = p*(v/100)
        pf = p-d
        print(f'O Desconto será de {d}')
        print(f'Com o valor final de {pf}')
        e = input('Deseja continuar? [s] [n]')
        while e == 's' or e == 'n':
            if e == 's':
                desconto()
            else:
                menu()
        else:
            print('comando invalido')
    else:
        print('valor invalido, coloque os centravos ou .00')
        desconto()

menu()
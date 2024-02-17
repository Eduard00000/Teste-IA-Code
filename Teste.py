def ler_numero(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Por favor, insira um número válido.")

def mostrar_menu():
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Dividir
    [5] Exponenciar
    [6] Outros Números
    [7] Mostrar Histórico
    [8] Sair do programa''')

def adicionar_historico(historico, operacao, resultado):
    historico.append(f"{operacao} = {resultado}")

p1 = ler_numero('Primeiro Valor: ')
p2 = ler_numero('Segundo Valor: ')
opcao = 0
historico = []

while opcao != 8:
    mostrar_menu()
    opcao = int(ler_numero('Qual a sua opção?: '))
    
    if opcao == 1:
        resultado = p1 + p2
        print(f'A soma entre os números {p1} e {p2} é {resultado}')
        adicionar_historico(historico, f"{p1} + {p2}", resultado)
    elif opcao == 2:
        resultado = p1 * p2
        print(f'A multiplicação entre os números {p1} e {p2} é {resultado}')
        adicionar_historico(historico, f"{p1} * {p2}", resultado)
    elif opcao == 3:
        maior = p1 if p1 > p2 else p2
        print(f'Entre os números {p1} e {p2} o maior é {maior}')
        adicionar_historico(historico, f"Maior entre {p1} e {p2}", maior)
    elif opcao == 4:
        if p2 == 0:
            print("Divisão por zero não é permitida.")
        else:
            resultado = p1 / p2
            print(f'A divisão entre os números {p1} e {p2} é {resultado}')
            adicionar_historico(historico, f"{p1} / {p2}", resultado)
    elif opcao == 5:
        resultado = p1 ** p2
        print(f'{p1} elevado a {p2} é {resultado}')
        adicionar_historico(historico, f"{p1} ^ {p2}", resultado)
    elif opcao == 6:
        p1 = ler_numero('Primeiro Valor: ')
        p2 = ler_numero('Segundo Valor: ')
    elif opcao == 7:
        if historico:
            for operacao in historico:
                print(operacao)
        else:
            print("Nenhuma operação foi realizada ainda.")
    elif opcao == 8:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')

print('Fim do programa! Até mais!')
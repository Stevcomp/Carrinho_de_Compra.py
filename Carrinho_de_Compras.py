
# Parâmetros de desconto
valor_minimo_de_desconto = 100.0
taxa_desconto = 0.10


def exibir_menu_carrinho():
    print('\n--- Calculadora de carrinho de compras ---')
    print('1. Adicionar Preço de Produto')
    print('2. Ver carrinho e Calcular Total')
    print('3. Esvaziar Carrinho')
    print('4. Sair')


def adicionar_preco(carrinho):
    try:
        preco_str = input('Digite o preço do produto (ex: 15.60): ')
        preco = float(preco_str)

        if preco > 0:
            carrinho.append(preco)
            print(f'Produto de R$ {preco:.2f} adicionado.')
        else:
            print('O preço deve ser um valor positivo.')
    except ValueError:
        print('Erro, valor inválido. Digite um valor numérico.')


def ver_carrinho_e_total(carrinho):
    if not carrinho:
        print("O carrinho está vazio.")
        return
    print('\n--- Itens no carrinho ---')
    subtotal = 0.0

    for preco in carrinho:
        print(f'R$ {preco:.2f}')
        subtotal += preco

    print(f'\nSubtotal: R$ {subtotal:.2f}')

    if subtotal > valor_minimo_de_desconto:
        desconto = subtotal * taxa_desconto
        total_a_pagar = subtotal - desconto
        print(f'Desconto (10%): R$ {desconto:.2f}')
    else:
        desconto = 0.0
        total_a_pagar = subtotal
        print('Nenhum desconto aplicado (compre acima de R$ 100,00).')

    print(f'Total a pagar (com desconto aplicado): R$ {total_a_pagar:.2f}')


def esvaziar_carrinho(carrinho):
    carrinho.clear()
    print('Carrinho esvaziado com sucesso.')


def main_carrinho():
    carrinho_de_compras = []

    while True:
        exibir_menu_carrinho()
        opcao = input('Escolha uma opção (1-4): ')

        if opcao == '1':
            adicionar_preco(carrinho_de_compras)
        elif opcao == '2':
            ver_carrinho_e_total(carrinho_de_compras)
        elif opcao == '3':
            esvaziar_carrinho(carrinho_de_compras)
        elif opcao == '4':
            print('Saindo... Obrigado por usar a calculadora de carrinho!')
            break
        else:
            print('Opção inválida. Tente novamente.')


main_carrinho()

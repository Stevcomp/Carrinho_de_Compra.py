🛒 Calculadora de Carrinho de Compras com Desconto
Este projeto é um sistema de terminal em Python que simula o funcionamento de um carrinho de compras. Ele permite gerenciar produtos e aplica automaticamente um desconto progressivo baseado no valor total da compra.

✨ Funcionalidades
Adição de itens: Permite inserir múltiplos preços de produtos com validação de entrada (apenas valores positivos).
Visualização detalhada: Lista todos os itens presentes no carrinho.
Cálculo de Total: Soma os valores e calcula o desconto se os critérios forem atingidos.
Gestão de Carrinho: Opção para esvaziar a lista e recomeçar o processo.
Tratamento de Erros: Evita que o programa feche caso o usuário digite letras ou caracteres inválidos.

💰 Regra de Negócio
O sistema aplica a seguinte lógica de desconto:
Valor mínimo: R$ 100,00
Taxa de desconto: 10%
Se o subtotal for superior a R$ 100,00, o desconto é exibido e subtraído do valor final.

🛠️ Tecnologias
Python 3.x

💻 Como executar
Clone o repositório ou copie o código para um arquivo .py.
Execute o comando:
Bash
python nome_do_arquivo.py
Navegue pelo menu interativo digitando os números correspondentes às opções.

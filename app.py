#importa as classes
from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

#Cria a lanchonte
restaurante_lanchonete = Restaurante('Lanchonete da Lu', 'lanchonete')

#Cria o os itens da lanchonete
bebida_suco = Bebida('Suco de Melancia', 7.0,'500ml')
prato_paozinho = Prato('Paozinho',3.00,'O melhor pão da cidade')
sobremesa_sorvete = Sobremesa('Sorvete', 10.00, 'Chocolate')
prato_bolo = Prato('Bolo', 15.00, 'Bolo caseiro de fubá')
bebida_refri = Bebida('Coca-cola', 5.00, '250ml')
bebida_cafe = Bebida('Café', 3.00, '200ml')
prato_salgado = Prato('Coxinha', 6.00, 'Caxinha de frango com cutupiry')
 
#Cria a  pizzaria
restaurante_pizza = Restaurante('Pizzaria Bom Sabor', 'Pizzaria')

#Cria os itens da pizzaria
prato_calabresa = Prato('Pizza de calabresa', 48.00, 'A melhor pizza de calabresa' )
prato_calabresa.aplicar_desconto()
prato_frango = Prato('Pizza de frando', 55.00, 'Pizza de frando com bastante recheio')
prato_frango.aplicar_desconto()

#restaurantes recebem avaliações
restaurante_lanchonete.receber_avaliacao('Laura', 5)
restaurante_lanchonete.receber_avaliacao('Cláudio', 3)
restaurante_lanchonete.receber_avaliacao('Marcos', 5)

restaurante_pizza.receber_avaliacao('Felipe', 5)
restaurante_pizza.receber_avaliacao('Marcelo', 4)
restaurante_pizza.receber_avaliacao('Isadora', 5)

#Adiciona os itens ao cardápio dos restaurantes
restaurante_lanchonete.adicionar_no_cardapio(bebida_suco)
restaurante_lanchonete.adicionar_no_cardapio(prato_paozinho)
restaurante_lanchonete.adicionar_no_cardapio(sobremesa_sorvete)
restaurante_lanchonete.adicionar_no_cardapio(prato_bolo)
restaurante_lanchonete.adicionar_no_cardapio(bebida_refri)
restaurante_lanchonete.adicionar_no_cardapio(prato_salgado)

restaurante_pizza.adicionar_no_cardapio(prato_calabresa)
restaurante_pizza.adicionar_no_cardapio(prato_frango)
restaurante_pizza.adicionar_no_cardapio(bebida_refri)

restaurante_lanchonete.alternar_estado()

Restaurante.listar_restaurantes()

def main():
    restaurante_lanchonete.exibir_cardapio
    print('')
    restaurante_pizza.exibir_cardapio

if __name__ == '__main__':
    main()

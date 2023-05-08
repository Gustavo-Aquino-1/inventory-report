# from inventory_report.inventory.product import Product
from inventory_report.inventory.product import Product


def test_cria_produto():
    new_product = Product(
        1,
        "Camisa básica",
        "nike",
        "2023-05-05",
        "2029-05-05",
        155587,
        "na sombra",
    )
    assert new_product.id == 1
    assert new_product.nome_do_produto == 'Camisa básica'
    assert new_product.nome_da_empresa == 'nike'
    assert new_product.data_de_fabricacao == "2023-05-05"
    assert new_product.data_de_validade == "2029-05-05"
    assert new_product.numero_de_serie == 155587
    assert new_product.instrucoes_de_armazenamento == "na sombra"

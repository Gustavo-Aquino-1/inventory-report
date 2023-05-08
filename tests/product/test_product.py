# from inventory_report.inventory.product import Product
from inventory_report.inventory.product import Product


def test_cria_produto():
    new_product = Product(
        1,
        "Camisa básica",
        "nike",
        "25/02/2023",
        "25/02/2029",
        155587,
        "na sombra",
    )
    assert isinstance(new_product, Product)

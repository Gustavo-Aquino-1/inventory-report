from inventory_report.inventory.product import Product


def test_relatorio_produto():
    new_product = Product(
        1, "Camisa", "nike", "02-02-2023", "02-04-2029", 11234, "na sombra"
    )
    assert (
        new_product.__repr__()
        == "O produto Camisa fabricado em 02-02-2023 por nike com " +
        "validade até 02-04-2029 precisa ser armazenado na sombra."
    )

from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, arr):
        simple_report = super().generate(arr)
        companies = {x["nome_da_empresa"]: 0 for x in arr}
        for cp in arr:
            companies[cp["nome_da_empresa"]] += 1

        result = "\n".join(
            [f"- {name}: {qtd}" for name, qtd in companies.items()]
        )

        return (
            f"""{simple_report}
Produtos estocados por empresa:
{result}\n"""
        )

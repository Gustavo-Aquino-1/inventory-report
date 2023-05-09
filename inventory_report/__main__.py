import sys
from inventory_report.inventory.inventory_refactor import (
    InventoryRefactor,
    JSON,
    CSV,
    XML,
)


def main():
    args = sys.argv
    args = [x for x in args if x != '']
    if len(args) < 3:
        sys.stderr.write('Verifique os argumentos' + '\n')
        return

    _, path, report_type = args
    extension = path[path.rindex(".") + 1:]
    importers = {"json": JSON, "csv": CSV, "xml": XML}
    inventory = InventoryRefactor(importers[extension])
    inventory.import_data(path, report_type)
    relatory = list(inventory.data[0])
    # print(relatory)
    while relatory[-1] == '\n':
        del relatory[-1]
    # print(relatory)
    if report_type == 'simples':
        print("".join(relatory), end="")
    else:
        print("".join(relatory))


# main()

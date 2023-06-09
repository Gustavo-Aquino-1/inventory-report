from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(path, rp=None):
        if "json" in path or "xml" in path:
            raise ValueError('Arquivo inválido')
        with open(path, mode="r", encoding="utf8") as file:
            data = csv.DictReader(file, delimiter=",", quotechar='"')
            return list(data)

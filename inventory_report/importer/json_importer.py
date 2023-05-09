from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(path, rp=None):
        if 'csv' in path or 'xml' in path:
            raise ValueError('Arquivo inválido')
        with open(path, mode="r", encoding="utf8") as file:
            data = json.load(file)
            return list(data)

from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @staticmethod
    def import_data(path, rp=None):
        if "csv" in path or "json" in path:
            raise ValueError("Arquivo inválido")
        with open(path, mode="r", encoding="utf8") as file:
            data = xmltodict.parse(file.read())
            return data["dataset"]["record"]

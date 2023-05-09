from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json

# import xml.etree.ElementTree as ET
import xmltodict
from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator


class CSV:
    @staticmethod
    def import_data(path, report_type):
        type_gr = SimpleReport if report_type == "simples" else CompleteReport
        with open(path, mode="r", encoding="utf8") as file:
            data = csv.DictReader(file, delimiter=",", quotechar='"')
            return type_gr.generate(list(data))


class JSON:
    @staticmethod
    def import_data(path, report_type):
        type_gr = SimpleReport if report_type == "simples" else CompleteReport
        with open(path, mode="r", encoding="utf8") as file:
            data = json.load(file)
            return type_gr.generate(list(data))


class XML:
    @staticmethod
    def import_data(path, report_type):
        type_gr = SimpleReport if report_type == "simples" else CompleteReport
        with open(path, mode="r", encoding="utf8") as file:
            data = xmltodict.parse(file.read())
            return type_gr.generate(data["dataset"]["record"])


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path, report_type):
        print(path, report_type)
        data = self.importer.import_data(path=path, report_type=report_type)
        self.data += data

    def __iter__(self):
        return InventoryIterator(self.data)


# inventory = InventoryRefactor(CSV)
# inventory.import_data("inventory_report/data/inventory.csv", "simples")
# print(inventory.data)

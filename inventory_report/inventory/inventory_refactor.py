import csv
import json
# import xml.etree.ElementTree as ET
import xmltodict
from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator


class CSV:
    @staticmethod
    def import_data(path):
        with open(path, mode="r", encoding="utf8") as file:
            data = csv.DictReader(file, delimiter=",", quotechar='"')
            return list(data)


class JSON:
    @staticmethod
    def import_data(path):
        with open(path, mode="r", encoding="utf8") as file:
            data = json.load(file)
            return list(data)


class XML:
    @staticmethod
    def import_data(path):
        with open(path, mode="r", encoding="utf8") as file:
            data = xmltodict.parse(file.read())
            return data["dataset"]["record"]


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path, report_type):
        data = self.importer.import_data(path)
        self.data.extend(data)

    def __iter__(self):
        return InventoryIterator(self.data)

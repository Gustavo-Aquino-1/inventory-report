from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator
import csv
import json

# import xml.etree.ElementTree as ET
import xmltodict


class CSV:
    @staticmethod
    def import_data(path, report_type=None):
        type_gr = SimpleReport if report_type == "simples" else CompleteReport
        with open(path, mode="r", encoding="utf8") as file:
            data = csv.DictReader(file, delimiter=",", quotechar='"')
            return type_gr.generate(list(data))


class JSON:
    @staticmethod
    def import_data(path, report_type=None):
        type_gr = SimpleReport if report_type == "simples" else CompleteReport
        with open(path, mode="r", encoding="utf8") as file:
            data = json.load(file)
            return type_gr.generate(list(data))


class XML:
    @staticmethod
    def import_data(path, report_type=None):
        type_gr = SimpleReport if report_type == "simples" else CompleteReport
        with open(path, mode="r", encoding="utf8") as file:
            data = xmltodict.parse(file.read())
            return type_gr.generate(data['dataset']['record'])


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path, report_type):
        data = self.importer.import_data(path, report_type)
        if isinstance(data, str):
            self.data.append(data)
        else:
            self.data.extend(data)

    def __iter__(self):
        return InventoryIterator(self.data)

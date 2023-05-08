from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json

# import xml.etree.ElementTree as ET
import xmltodict


class CSV:
    @classmethod
    def import_data(cls, path, report_type):
        type_gr = SimpleReport if report_type == "simples" else CompleteReport
        with open(path, mode="r", encoding="utf8") as file:
            data = csv.DictReader(file, delimiter=",", quotechar='"')
            return type_gr.generate(list(data))


class JSON:
    @classmethod
    def import_data(cls, path, report_type):
        type_gr = SimpleReport if report_type == "simples" else CompleteReport
        with open(path, mode="r", encoding="utf8") as file:
            data = json.load(file)
            return type_gr.generate(list(data))


class XML:
    @classmethod
    def import_data(cls, path, report_type):
        type_gr = SimpleReport if report_type == "simples" else CompleteReport
        with open(path, mode="r", encoding="utf8") as file:
            data = xmltodict.parse(file.read())
            return type_gr.generate(data['dataset']['record'])


class Inventory:
    @classmethod
    def import_data(cls, path, report_type: str):
        redirect = {"csv": CSV, "json": JSON, "xml": XML}
        ind = path.rindex(".")
        type_arq = path[ind + 1:]
        return redirect[type_arq].import_data(path, report_type)

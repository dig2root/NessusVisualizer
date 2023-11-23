from src.controller.parser.NessusXMLParser import NessusXMLParser
import sys

class Controller:

    INSTANCE = None

    def __init__(self):
        self.nessus_parser = NessusXMLParser.get_instance()

    @staticmethod
    def get_instance():
        if Controller.INSTANCE is None:
            Controller.INSTANCE = Controller()
        return Controller.INSTANCE

    def get_nodes_from_xml(self):
        filepath = "data/uploads/2d74a074-858d-11ee-8c27-5354c2051836/report.nessus"
        filepath = "data/uploads/ebf370e6-862f-11ee-b14f-5ebbf69eeefa/report.nessus"
        with open(filepath, "r") as f:
            xml_content = f.read().encode("utf-8")
        sys.stdout.write("Parsing XML file...\n")
        data = self.nessus_parser.get_vulnerabilities_from_xml(xml_content)
        nodes = [vulner_id for vulner_id in data]

        sys.stdout.write(str(nodes)+ "\n")
        return nodes
from lxml import etree

class NessusXMLParser:

    INSTANCE = None

    def __init__(self):
        pass

    @staticmethod
    def get_instance():
        if NessusXMLParser.INSTANCE is None:
            NessusXMLParser.INSTANCE = NessusXMLParser()
        return NessusXMLParser.INSTANCE

    def get_vulnerabilities_from_xml(self, xml_content: str):
        vulnerabilities = dict()
        single_params = ["agent", "cvss3_base_score", "cvss3_temporal_score", "cvss3_temporal_vector", "cvss3_vector",
                        "cvss_base_score", "cvss_temporal_score", "cvss_temporal_vector", "cvss_vector", "description",
                        "exploit_available", "exploitability_ease", "exploited_by_nessus", "fname", "in_the_news",
                        "patch_publication_date", "plugin_modification_date", "plugin_name", "plugin_publication_date",
                        "plugin_type", "script_version", "see_also", "solution", "synopsis", "vuln_publication_date",
                        "compliance",
                        "{http://www.nessus.org/cm}compliance-check-id",
                        "{http://www.nessus.org/cm}compliance-check-name",
                        "{http://www.nessus.org/cm}audit-file",
                        "{http://www.nessus.org/cm}compliance-info",
                        "{http://www.nessus.org/cm}compliance-result",
                        "{http://www.nessus.org/cm}compliance-see-also"]
        p = etree.XMLParser(huge_tree=True)
        root = etree.fromstring(text=xml_content, parser=p)
        for block in root:
            if block.tag == "Report":
                for report_host in block:
                    host_properties_dict = dict()
                    for report_item in report_host:
                        if report_item.tag == "HostProperties":
                            for host_properties in report_item:
                                host_properties_dict[host_properties.attrib['name']] = host_properties.text
                    for report_item in report_host:
                        if 'pluginName' in report_item.attrib:
                            vulner_struct = dict()
                            vulner_struct['port'] = report_item.attrib['port']
                            vulner_struct['pluginName'] = report_item.attrib['pluginName']
                            vulner_struct['pluginFamily'] = report_item.attrib['pluginFamily']
                            vulner_struct['pluginID'] = report_item.attrib['pluginID']
                            vulner_struct['svc_name'] = report_item.attrib['svc_name']
                            vulner_struct['protocol'] = report_item.attrib['protocol']
                            vulner_struct['severity'] = report_item.attrib['severity']
                            for param in report_item:
                                if param.tag == "risk_factor":
                                    risk_factor = param.text
                                    vulner_struct['host'] = report_host.attrib['name']
                                    vulner_struct['riskFactor'] = risk_factor
                                elif param.tag == "plugin_output":
                                    if not "plugin_output" in vulner_struct:
                                        vulner_struct["plugin_output"] = list()
                                    if not param.text in vulner_struct["plugin_output"]:
                                        vulner_struct["plugin_output"].append(param.text)
                                else:
                                    if not param.tag in single_params:
                                        if not param.tag in vulner_struct:
                                            vulner_struct[param.tag] = list()
                                        if not isinstance(vulner_struct[param.tag], list):
                                            vulner_struct[param.tag] = [vulner_struct[param.tag]]
                                        if not param.text in vulner_struct[param.tag]:
                                            vulner_struct[param.tag].append(param.text)
                                    else:
                                        vulner_struct[param.tag] = param.text
                            for param in host_properties_dict:
                                vulner_struct[param] = host_properties_dict[param]
                            compliance_check_id = ""
                            if 'compliance' in vulner_struct:
                                if vulner_struct['compliance'] == 'true':
                                    compliance_check_id = vulner_struct['{http://www.nessus.org/cm}compliance-check-id']
                            if compliance_check_id == "":
                                vulner_id = vulner_struct['host'] + "|" + vulner_struct['port'] + "|" + \
                                            vulner_struct['protocol'] + "|" + vulner_struct['pluginID']
                            else:
                                vulner_id = vulner_struct['host'] + "|" + vulner_struct['port'] + "|" + \
                                            vulner_struct['protocol'] + "|" + vulner_struct['pluginID'] + "|" + \
                                            compliance_check_id
                            if not vulner_id in vulnerabilities:
                                vulnerabilities[vulner_id] = vulner_struct
        return(vulnerabilities)
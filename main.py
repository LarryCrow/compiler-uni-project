from doh_lexer import *
from doh_parser import *
import sys
import argparse

import xml.etree.ElementTree as etree
from xml.dom import minidom

from os import listdir, path, getcwd
from os.path import isfile, join, abspath, dirname, splitext


def create_params_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-parameters')
    parser.add_argument('-xml')

    return parser


def convert_to_xml(root):
    main_scope = etree.Element('SCOPE')

    def convert_node(node, prev):
        if hasattr(node, 'type'):
            node_xml = etree.SubElement(prev, node.type)
            for part in node.parts:
                convert_node(part, node_xml)
        else:
            prev.text = node

    for elem in root.parts:
        convert_node(elem, main_scope)
    return main_scope


def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = etree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")


pr = create_params_parser()
namespace = pr.parse_args(sys.argv[1:])
lexer = lex.lex()
file_name = namespace.parameters
is_xml = bool(namespace.xml)
with open(file_name, 'r', encoding="UTF-8") as r:
    data = r.read()
    lexer.start_row_pos = 0
    lexer.input(data)
    import sys
    from errors import subscribe_errors, find_semantic_errors, errors_reported
    parser = create_doh_parser()
    with subscribe_errors(lambda msg: sys.stdout.write(msg+"\n")):
        program = parser.parse()
        if errors_reported() == 0:
            find_semantic_errors(program)
            if errors_reported() == 0:
                if is_xml:
                    res = convert_to_xml(program)
                    xml_file = open('program.xml', 'w')
                    xml_file.write(prettify(res))
                else:
                    with open('result.txt', 'w') as w:
                        w.write(str(program))

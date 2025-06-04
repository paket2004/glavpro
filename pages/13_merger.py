from docxcompose.composer import Composer
from docx import Document as Document_compose
from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import streamlit as st

def add_page_break(doc):
    """Inserts a page break into the document."""
    paragraph = doc.add_paragraph()
    run = paragraph.add_run()
    br = OxmlElement('w:br')
    br.set(qn('w:type'), 'page')
    run._r.append(br)

def combine_all_docx(filename_master, files_list, output_path):
    """Merging specified docx documents"""
    number_of_sections = len(files_list)
    master = Document_compose(filename_master)
    composer = Composer(master)
    for i in range(0, number_of_sections):
        doc_temp = Document_compose(files_list[i])
        composer.append(doc_temp)
    composer.save(output_path)


def merge_izav_info():
    """merging izav folder"""
    return combine_all_docx(\
        filename_master= "inventarization_description/izav_info/description.docx",
        files_list=["inventarization_description/izav_info/part2_without_intro.docx"],
        output_path="inventarization_description/izav_info/razdel2.docx")

def merge_san_zone():
    """merging sanitary zone folder"""
    return combine_all_docx(
        filename_master="object_property/sanitary_zone/description.docx",
        files_list=["object_property/dust_and_gas/dust_and_gus_info.docx", "object_property/previous_inventarization/prev_inv_info.docx"],
        output_path="object_property\sanitary_zone\sanitary_zone.docx"
    )

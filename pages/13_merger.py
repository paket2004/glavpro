from docxcompose.composer import Composer
from docx import Document as Document_compose
from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import streamlit as st
import os

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

def merge_all_documents():
    """Главная функция для объединения всех документов"""
    results = []
    
    with st.status("Объединение документов...", expanded=True) as status:
        st.write("Объединяем раздел 'izav_info'...")
        results.append(merge_izav_info())
        
        st.write("Объединяем раздел 'sanitary_zone'...")
        results.append(merge_san_zone())
        
        
        if all(results):
            status.update(label="Все документы успешно объединены!", state="complete")
            return True
        else:
            status.update(label="Объединение завершено с ошибками", state="error")
            return False

st.title("📄 Система объединения документов")

if st.button("Объединить все документы", type="primary"):
    if merge_all_documents():
        # Создаем список объединенных файлов для скачивания
        merged_files = [
            "inventarization_description/izav_info/razdel2.docx",
            "object_property/sanitary_zone/sanitary_zone.docx"
        ]
        
        # Показываем кнопки для скачивания каждого файла
        for file_path in merged_files:
            if os.path.exists(file_path):
                with open(file_path, "rb") as f:
                    st.download_button(
                        label=f"⬇️ Скачать {os.path.basename(file_path)}",
                        data=f,
                        file_name=os.path.basename(file_path),
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )
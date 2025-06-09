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
    """Merging specified docx documents with error handling"""
    try:
        # Проверка существования файлов
        missing_files = []
        if not os.path.exists(filename_master):
            missing_files.append(filename_master)
        
        for file in files_list:
            if not os.path.exists(file):
                missing_files.append(file)
        
        if missing_files:
            raise FileNotFoundError(f"Отсутствуют файлы: {', '.join(missing_files)}")

        # Создание папки для результата, если её нет
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Процесс объединения
        master = Document_compose(filename_master)
        composer = Composer(master)
        
        for file in files_list:
            doc_temp = Document_compose(file)
            composer.append(doc_temp)
        
        composer.save(output_path)
        return True
    except Exception as e:
        st.error(f"Ошибка при объединении в {output_path}: {str(e)}")
        return False

def merge_izav_info():
    """merging izav folder"""
    try:
        st.write("Попытка объединения izav_info...")
        result = combine_all_docx(
            filename_master="inventarization_description/izav_info/description.docx",
            files_list=["inventarization_description/izav_info/part2_without_intro.docx"],
            output_path="inventarization_description/izav_info/razdel2.docx"
        )
        if result:
            st.success("Успешно!")
        return result
    except Exception as e:
        st.error(f"Ошибка в merge_izav_info: {str(e)}")
        return False

def merge_san_zone():
    """merging sanitary zone"""
    try:
        st.write("Попытка объединения sanitary_zone...")
        result = combine_all_docx(
            filename_master="object_property/sanitary_zone/description.docx",
            files_list=[
                "object_property/dust_and_gas/dust_and_gus_info.docx",
                "object_property/previous_inventarization/prev_inv_info.docx"
            ],
            output_path="object_property/sanitary_zone/sanitary_zone.docx"
        )
        if result:
            st.success("Успешно!")
        return result
    except Exception as e:
        st.error(f"Ошибка в merge_san_zone: {str(e)}")
        return False

def merge_all_documents():
    results = []
    
    with st.status("Объединение документов...", expanded=True) as status:
        required_files = [
            "inventarization_description/izav_info/description.docx",
            "inventarization_description/izav_info/part2_without_intro.docx",
            "object_property/sanitary_zone/description.docx",
            "object_property/dust_and_gas/dust_and_gus_info.docx",
            "object_property/previous_inventarization/prev_inv_info.docx"
        ]
        
        missing_files = [f for f in required_files if not os.path.exists(f)]
        if missing_files:
            st.error(f"Отсутствуют файлы: {', '.join(missing_files)}")
            status.update(label="Объединение невозможно: отсутствуют файлы", state="error")
            return False
        
        st.write("Начинаем объединение...")
        results.append(merge_izav_info())
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
        merged_files = [
            "inventarization_description/izav_info/razdel2.docx",
            "object_property/sanitary_zone/sanitary_zone.docx"
        ]
        
        for file_path in merged_files:
            if os.path.exists(file_path):
                with open(file_path, "rb") as f:
                    st.download_button(
                        label=f"⬇Скачать {os.path.basename(file_path)}",
                        data=f,
                        file_name=os.path.basename(file_path),
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )
            else:
                st.warning(f"Файл {file_path} не был создан")
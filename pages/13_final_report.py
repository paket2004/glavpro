import streamlit as st
from pathlib import Path
from io import BytesIO

from report_combiner_docx import combine_all_docx, create_page_break_doc

def main():
    st.title("Сборка итогового отчёта")
    st.write("Нажмите кнопку ниже, чтобы объединить все разделы в один итоговый документ.")

    if st.button("Сформировать итоговый отчёт"):
        with st.spinner("Объединяем документы..."):
            try:
                filename_master = "content/Содержание_отчета.docx"
                files_to_merge = [
                    "mount/src/glavpro/termins_and_short/dictionary_table.docx",
                    "introduction/introduction.docx",
                    "inventarization_description/punkt1/organization_sources_info.docx",
                    "object_property/sanitary_zone/sanitary_zone.docx",
                    "inventarization_description/izav_info/razdel2.docx",
                    "calculations/tables/razdel3/razdel3.docx"
                ]

                combine_all_docx(filename_master, files_to_merge)

                output_path = Path("combined_file.docx")
                if output_path.exists():
                    with open(output_path, "rb") as f:
                        data = f.read()
                    st.success("Отчёт успешно сформирован!")
                    st.download_button(
                        label="📥 Скачать итоговый отчёт",
                        data=data,
                        file_name="Итоговый_отчет.docx",
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )
                else:
                    st.error("Не удалось найти файл 'combined_file.docx'")
            except Exception as e:
                st.error(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()

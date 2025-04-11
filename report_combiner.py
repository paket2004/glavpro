from docx import Document
from docx.enum.section import WD_SECTION

def merge_docx(files, output_file):
    if not files:
        print("No files to merge!")
        return

    merged_document = Document(files[0])  # Начинаем с первого документа

    for file in files[1:]:  # Обрабатываем остальные документы
        # Добавляем разрыв страницы перед следующим документом
        merged_document.add_page_break()
        
        doc = Document(file)
        for element in doc.element.body:
            merged_document.element.body.append(element)

    merged_document.save(output_file)
    print(f"Документы успешно объединены в {output_file}")

# Пример использования
files_to_merge = [
    "content/Содержание_отчета.docx",
    "termins_and_short/dictionary_table.docx",
    "introduction/introduction.docx"
]
merge_docx(files_to_merge, "REPORT.docx")
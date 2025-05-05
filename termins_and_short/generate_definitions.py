import openai
from openai import OpenAI
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os
from docx.shared import Pt, RGBColor
from docx import Document

import re

from generate_short import shorcuts_list
openai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

def add_shortcuts_to_doc(doc, shortcuts_cur, shorcuts_list):
    style = doc.styles['Normal']
    style.font.name = 'Times New Roman'
    heading = doc.add_heading(level=1)
    heading.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = heading.add_run('''
    Принятые в отчете по инвентаризации стационарных источников и выбросов вредных (загрязняющих) веществ в атмосферный воздух сокращения:''')
    run = heading.runs[0]
    run.font.color.rgb = RGBColor(0, 0, 0)  # Black color
    run.font.name = 'Times New Roman'
    run.font.size = Pt(8)
    run.bold = True
    for shorcut in shortcuts_cur:
        if shorcut in shorcuts_list.keys():
            p = doc.add_paragraph()
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.0
            
            run = p.add_run(f"{shorcut} – {shorcuts_list[shorcut]}")
            run.font.name = 'Times New Roman'
            run.font.size = Pt(6)
        else:
            print("Нет такого сокращения")
    


def generate_response(termins: str, shortcuts: dict):
    # ТУТ БЫ В БУДУЩЕМ ПРОВЕРКУ ОТ ЛЛМКИ НА ОПЕЧАТКУ И РЕГЕКСПЫ НА ТО, ЧТО НАПИСАНО ЧТО-ТО АДЕКВАТНОЕ
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant and your aim is to write a inventarization report for the company. Do not write abstract text, it should be very human written text."},
            {
                "role": "user",
                "content": f"""provide definitions on Russian language for stated words. Do this for these termins: {termins}.
                Examples: 
                
                input: история
                answer:  наука, научная (академическая) дисциплина, предметом изучения которой является человеческое прошлое; историческая наука использует исторические источники, включая различные нарративы, письменные документы, устные сообщения, материальные артефакты, лингвистические данные, а также экологические маркеры, для описания и исследования человеческого прошлого и причинно-следственных связей исторических событий и фактов, конкретные проявления и закономерности исторического процесса, развитие социума и любую человеческую деятельность.
                
                input: магнат
                answer: дворянин или человек, занимающий высокое социальное положение, по рождению (происхождению), богатству или другим качествам.

                input: раздел

                answer: рубрикационная часть произведения или издания. В произведении раздел объединяет несколько глав. Несколько разделов, в свою очередь, могут образовать часть или книгу. В издании в раздел могут быть объединены несколько произведений.
                    """
            }
        ]
    )
    answers = completion.choices[0].message


    # Use regex to extract term-answer pairs
    pattern = r"input: (.*?)\s*answer: (.*?)(?=\ninput: |\Z)"
    matches = re.findall(pattern, answers.content, re.DOTALL)

    # Store the results in a dictionary
    results = {term.strip(): answer.strip() for term, answer in matches}
    print(results.keys())


    doc = Document()
    style = doc.styles['Normal']
    style.font.name = 'Times New Roman'
    heading = doc.add_heading(level=1)
    heading.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = heading.add_run('Основные термины, используемые в проекте')
    run = heading.runs[0]
    run.font.color.rgb = RGBColor(0, 0, 0)  # Black color
    run.font.name = 'Times New Roman'
    run.font.size = Pt(8)
    table = doc.add_table(rows=len(results), cols=2)
    table.style = 'Table Grid'
    # Populate the table with dictionary keys and values
    for i, (key, value) in enumerate(results.items()):
        # Add key to the first column
        table.cell(i, 0).text = str(key)
        # Add value to the second column
        table.cell(i, 1).text = str(value)

    for row in table.rows:
        for cell in row.cells:
            for paragraph in cell.paragraphs:
                for run in paragraph.runs:
                    run.font.size = Pt(6)

    # Добавляем сокращения в документ
    if shortcuts:
        add_shortcuts_to_doc(doc, shortcuts, shorcuts_list)
    doc.save('termins_and_short/dictionary_table.docx')
    


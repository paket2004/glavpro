#!/usr/bin/python
# -*- coding: utf-8 -*-
from pypdf import PdfReader
import re
# Загрузка PDF-файла
reader = PdfReader("downloads/ul-1025602832474-20250128144643.pdf")

# Извлечение текста с первой страницы
page = reader.pages[0]
text = page.extract_text()
text = text.replace("\n", " ")
plain_text = ""

for page in reader.pages:
    text = page.extract_text()
    text = text.replace("\n", " ")
    plain_text += text


data_to_extract = ["Полное наименование на русском языке","Сокращенное наименование на русском языке", "Адрес юридического лица","ИНН", "ОГРН","КПП", "ОКВЭД"]


# Функция для поиска значений по ключевому слову
def extract_value(pattern, text):
    match = re.search(pattern, text)
    return match.group(1).strip() if match else None


import openai
from openai import OpenAI

import os
openai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()


def generate_response(text: str, data_to_extract: str):
    # ТУТ БЫ В БУДУЩЕМ ПРОВЕРКУ ОТ ЛЛМКИ НА ОПЕЧАТКУ И РЕГЕКСПЫ НА ТО, ЧТО НАПИСАНО ЧТО-ТО АДЕКВАТНОЕ
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a information extractor from the extract from the Unified State Register of Legal Entities. Your aim is to extract a information that is asked in the prompt. Do not write abstract text, it should be very human written text."},
            {
                "role": "user",
                "content": f"""please, extract the text for the information on Russian language that I provide to you. Do this for these termins: {data_to_extract}. Please, pay special attention to the ОКВЭД. It may be not only main, but also additional.
                Text {plain_text}.
                answer: 
                Полное наименование на русском языке:
                Сокращенное наименование на русском языке:
                Адрес юридического лица:
                Адреса осуществления деятельности:
                Фактический адрес площадки:
                ИНН:
                ОГРН:
                КПП:
                ОКВЭД:
                Директор:  
                    """
            }
        ]
    )
    answers = completion.choices[0].message
    import re
    # print(answers.content)
    text = answers.content.replace("\n", " ")
    text = re.sub(r'\s+', ' ', text)
    
    print(text)
    # Регулярные выражения для поиска данных
    data = {
    "Полное наименование": extract_value(r'Полное наименование на русском языке:\s*(.+?)\s*Сокращенное наименование', text),
    "Сокращенное наименование": extract_value(r'Сокращенное наименование на русском языке:\s*(.+?)\s*Адрес', text),
    "Адрес": extract_value(r'Адрес юридического лица:\s*(.+?)\s*ИНН', text),
    "ИНН": extract_value(r'ИНН:\s*(\d+)', text),
    "ОГРН": extract_value(r'ОГРН:\s*(\d+)', text),
    "КПП": extract_value(r'КПП:\s*(\d+)', text),
    "ОКВЭД_основной": extract_value(r'ОКВЭД:\s*Основной\s*-\s*(\S+)', text),
    "ОКВЭД_дополнительный": extract_value(r'Дополнительный\s*-\s*(\S+)', text),
    "Директор": extract_value(r'Директор:\s*(.+)', text),
}

    # Вывод результата
    for key, value in data.items():
        print(f"{key}: {value}")

    
        

generate_response(plain_text, data_to_extract)

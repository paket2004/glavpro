import streamlit as st
import requests
import json
import os
import datetime
import traceback
from time import sleep
from urllib.parse import urlencode
from io import BytesIO

# inn = "5639004992"
# inn = st.text_input("Введите ИНН вашей компании")
def get_report(inn: str):
    s = requests.Session()

    # Получаем CSRF-токен
    try:
        r = s.get("https://egrul.nalog.ru/index.html",
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
                "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
            }
        )
        r.raise_for_status()

    except Exception as e:
        print(f"Ошибка при получении страницы: {e}")
        exit()

    # Отправляем запрос с ИНН
    try:
        form_data = {
            'vyp3CaptchaToken': '',
            'page': '',
            'query': inn,
            'region': '',
            'PreventChromeAutocomplete': ''
        }
        
        r = s.post(
            'https://egrul.nalog.ru/',
            data=urlencode(form_data),
            headers={
                "Host": "egrul.nalog.ru",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
                "Referer": "https://egrul.nalog.ru/index.html",
                "Content-Type": "application/x-www-form-urlencoded",
                "X-Requested-With": "XMLHttpRequest"
            }
        )
        r.raise_for_status()
        t = r.json()['t']
    except Exception as e:
        print(f"Ошибка при отправке ИНН: {e}")
        exit()

    # Получаем результаты поиска
    try:
        sleep(0.5)
        r = s.get(f"https://egrul.nalog.ru/search-result/{t}",
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
                "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
                "Referer": "https://egrul.nalog.ru/index.html"
            }
        )
        r.raise_for_status()
        jsn = r.json()
    except Exception as e:
        print(f"Ошибка при получении результатов: {e}")
        exit()

    # Обработка результатов
    try:
        if jsn.get('status') == 'wait':
            while True:
                sleep(0.5)
                r = s.get(f"https://egrul.nalog.ru/search-result/{t}")
                jsn = r.json()
                if jsn.get('status') != 'wait':
                    break

        if not jsn.get('rows'):
            print("Не найдено записей по данному ИНН")
            exit()

        item = jsn['rows'][0]
        if str(item.get('tot', '0')) == '0':
            print("Нет данных для скачивания")
            exit()

        name = inn
        dir_name = os.getcwd()
        os.makedirs(dir_name, exist_ok=True)
        with open(f"{dir_name}/{name}.txt", 'w', encoding='utf-8') as f:
            f.write(f"по состоянию на {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(json.dumps(item, ensure_ascii=False, indent=2))

        # 5. Запрос и скачивание выписки
        t = item['t']
        try:
            r = s.get(f"https://egrul.nalog.ru/vyp-request/{t}")
            r.raise_for_status()

            # Ожидание готовности выписки
            while True:
                sleep(0.5)
                r = s.get(f"https://egrul.nalog.ru/vyp-status/{t}")
                status = r.json().get('status')
                if status == 'ready':
                    break
                elif status == 'error':
                    raise Exception("Ошибка формирования выписки")

            # Скачивание PDF
            r = s.get(f"https://egrul.nalog.ru/vyp-download/{t}")
            r.raise_for_status()

            with open(f"{dir_name}/{name}выписка.pdf", 'wb') as f:
                f.write(r.content)

            print(f"Выписка успешно сохранена в папке: {dir_name}")

        except Exception as e:
            print(f"Ошибка при получении выписки: {e}")

    except Exception as e:
        print(f"Ошибка обработки результатов: {e}")
        traceback.print_exc()

    return r.content
st.set_page_config("Выписка ЕГРЮЛ", layout="centered")
st.title("Получить выписку из ЕГРЮЛ")
inn = st.text_input("Введите ИНН вашей компании (10 цифр)")

if st.button("Сформировать выписку"):
    if not inn or not inn.isdigit() or len(inn) != 10:
        st.error("Пожалуйста, введите корректный 10-значный ИНН.")
    else:
        with st.spinner("Обрабатываем запрос..."):
            try:
                pdf_content = get_report(inn)
                st.success("Выписка успешно получена!")
                filename = f"{inn}выписка.pdf"
                print(filename)
                st.download_button(
                    label="📥 Скачать выписку (PDF)",
                    data=BytesIO(pdf_content),
                    file_name=filename,
                    mime="application/pdf"
                )
            except Exception as e:
                st.error(f"Ошибка: {str(e)}")
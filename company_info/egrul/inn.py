import streamlit as st
from egrul_getter import egrul_info
import re
def is_valid_inn(inn):
    """Check if the INN is a 10-digit number."""
    return bool(re.match(r'^\d{10}$', inn))

st.title("Получение выписки ЕГРЮЛ")
inn = st.text_input("Введите ИНН вашей компании (10 цифр)")


if st.button("Получить выписку"):
    if is_valid_inn(inn):
        egrul_info.get_statement(inn)
    else:
        st.error("Некорректный ИНН. Введите 10 цифр.")

import streamlit as st
from docx import Document

doc = Document()
st.title("Характеристика пылегазоочистного оборудования и оценка его эффективности")

pgoy = st.text_input("Введите ПГОУ, установленное на вашем предприятии. Если такого нет, оставьте пустую строку")

if st.button("Отправить"):
    if pgoy:
        print("sth")
    else:
        doc.add_paragraph("Пылегазоочистное оборудование (ПГОУ) на объекте негативного воздействия отсутствуют.")
        doc.save("dust_and_gas/dust.docx")
        print("saved succesfully")
        st.success("Документ сохранён")
import streamlit as st
from docx import Document


doc = Document()
st.title("Сведения о проведённых инвентаризациях")

history = st.text_input("Введите информацию о проведённх инвентаризацияз (если их не было оставьте поле пустым)")

if st.button("Отправить"):
    if history:
        print("laslalal")
    else:
        doc.add_paragraph("Ранее инвентаризации стационарных источников и выбросов вредных веществ в атмосферный воздух для  НАЗВАНИЕ ОРГАНИЗАЦИИ не проводилась. ")
        doc.save("previous_inventarization/prev_inv.docx")
        st.success("Документ сохранён")
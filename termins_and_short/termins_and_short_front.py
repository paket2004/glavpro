import streamlit as st
from generate_definitions import generate_response
from io import BytesIO


def main():
    st.title("Генерация определений по терминам")

     # User input for terms (one term per line)
    st.write("Введите термины, используемые в проекте (один термин на строку):")
    termins_input = st.text_area("Термины", height=150)
    # Split the input into a list of terms (one per line)
    termins = [term.strip() for term in termins_input.split("\n") if term.strip()]

    st.write("Введите сокращения (одно на строку):")
    shortcuts_input = st.text_area("Сокращения", height=150)
    shortcuts = [shortcut.strip() for shortcut in shortcuts_input.split("\n") if shortcut.strip()]

    # Button to generate the document
    if st.button("Сгенерировать DOCX"):
        if termins or shortcuts:
            with st.spinner("Генерация определений и создание документа..."):
                # Call the generate_response function
                generate_response(termins, shortcuts)

                # Provide a download link for the generated DOCX
                with open("termins_and_short\dictionary_table.docx", "rb") as file:
                    doc_bytes = file.read()

                st.success("Документ успешно сгенерирован!")
                st.download_button(
                    label="Скачать DOCX",
                    data=doc_bytes,
                    file_name="основные_термины.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                )
        else:
            st.error("Пожалуйста, введите хотя бы один термин или сокращение")


# Run the app
if __name__ == "__main__":
    main()
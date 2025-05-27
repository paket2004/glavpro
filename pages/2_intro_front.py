import streamlit as st

from introduction.intro import generate_introduction 

def main():
    st.title("Генерация Введения")

    st.write("Введите название вашей организации:")
    orgnization_name = st.text_area("Название организации", height=150)

    if st.button("Сгенерировать введение"):
        if generate_introduction(orgnization_name) == 0:
            st.success("Документ успешно сгенерирован!")
if __name__ == "__main__":
    main()

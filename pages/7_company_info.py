import streamlit as st
import pandas as pd

def init_session_state():
    if 'company_init' not in st.session_state:
        rows = [
            "Адреса осуществления деятельности", 
            "Фактический адрес площадки",
            "ИНН", "ОГРН", "КПП", "ОКФС", "ОКОПФ", "ОКОГУ", "ОКТМО", "ОКПО",
            "Коды, присвоенные при постановке на государственный учет ОНВ", 
            "Директор",
            "Должностные лица, ответственные за проведение инвентаризации выбросов", 
            "Краткая характеристика местности",
            "Размеры и границы санитарно-защитной зоны"
        ]
        
        st.session_state.company_df = pd.DataFrame({
            "Наименование данных": rows,
            "На момент разработки отчета инвентаризации": [""] * len(rows)
        })
        st.session_state.company_init = True

init_session_state()

# 2. Основной интерфейс
st.title("Информация о компании")

# 3. Редактируемая таблица
st.write("Введите данные в таблицу:")
edited_df = st.data_editor(
    st.session_state.company_df,
    num_rows="dynamic",
    key="company_data_editor"
)

# 4. Сохранение изменений
st.session_state.company_df1 = edited_df

# 5. Кнопка для вывода данных
if st.button("Показать введённые данные", key="company_show_data"):
    st.write(st.session_state.company_df1)

# 6. Создание новой таблицы
if st.button("Создать новую таблицу", key="company_create_table"):
    try:
        # Создаем преобразованную таблицу
        new_data = {
            "Категория": st.session_state.company_df1["Наименование данных"],
            "Значение": st.session_state.company_df1["На момент разработки отчета инвентаризации"]
        }
        new_df = pd.DataFrame(new_data)
        
        st.write("Новая таблица:")
        st.write(new_df)
        
        # Экспорт в Excel
        new_df.to_excel("company_data.xlsx", index=False)
        with open("company_data.xlsx", "rb") as f:
            st.download_button(
                "Скачать данные компании",
                data=f,
                file_name="company_data.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
    except Exception as e:
        st.error(f"Ошибка при создании таблицы: {str(e)}")
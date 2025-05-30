import streamlit as st
import pandas as pd

st.title("Информация о компании")

columns_name = ["Наименование данных", "На момент разработки отчета инвентаризации"]

if 'df' not in st.session_state:
    rows = [
        "Адреса осуществления деятельности", 
        "Фактический адрес площадки", 
        "ИНН", "ОГРН", "КПП", "ОКФС", "ОКОПФ", "ОКОГУ", "ОКТМО", "ОКПО",
        "Коды, присвоенные при постановке на государственный учет ОНВ", 
        "Директор",
        "Должностные лица, ответственные за проведение инвентаризации выбросов МБОУ «Мирошкинская СОШ»", 
        "Краткая характеристика местности, прилегающей к объекту ОНВ",
        "Размеры и границы санитарно-защитной зоны"
    ]
    
    data = {
        "Наименование данных": rows,
        "На момент разработки отчета инвентаризации": [""] * len(rows),
    }
    st.session_state.df = pd.DataFrame(data)

# Отображаем редактируемую таблицу
st.write("Введите данные в таблицу:")
edited_df = st.data_editor(st.session_state.df, num_rows="dynamic")  # Фиксированное количество строк

# Сохраняем изменения в session_state
st.session_state.df = edited_df

# Кнопка для вывода данных
if st.button("Показать введённые данные"):
    st.write("Введённые данные:")
    st.write(st.session_state.df)

# Создание новой таблицы на основе введённых данных
if st.button("Создать новую таблицу"):
    # Извлекаем данные из session_state
    df = st.session_state.df
    
    # Создаем новую таблицу
    new_data = {
        "Категория": [
            "Полное наименование предприятия",
            "Сокращенное наименование предприятия",
            "Адрес юридического лица",
            "Адреса осуществления деятельности",
            "Фактический адрес площадки", 
            "ОКВЭД",
            "ИНН",
            "ОГРН",
            "КПП",
            "ОКОПФ", 
            "ОКФС", 
            "ОКОГУ", 
            "ОКТМО", 
            "ОКПО",
            "Коды, присвоенные при постановке на государственный учет ОНВ", 
            "Директор",
            "Должностные лица, ответственные за проведение инвентаризации выбросов МБОУ «Мирошкинская СОШ»",
            "Краткая характеристика местности, прилегающей к объекту ОНВ",
            "Размеры и границы санитарно-защитной зоны"

        ],
        "Значение": [
            df[df["Наименование данных"] == "Полное наименование предприятия"]["На момент разработки отчета инвентаризации"].values[0],
            df[df["Наименование данных"] == "Сокращенное наименование предприятия"]["На момент разработки отчета инвентаризации"].values[0],
            df[df["Наименование данных"] == "Адрес юридического лица"]["На момент разработки отчета инвентаризации"].values[0],
            df[df["Наименование данных"] == "Адреса осуществления деятельности"]["На момент разработки отчета инвентаризации"].values[0],
            df[df["Наименование данных"] == "Фактический адрес площадки"]["На момент разработки отчета инвентаризации"].values[0],
            df[df["Наименование данных"] == "ОКВЭД"]["На момент разработки отчета инвентаризации"].values[0],
            df[df["Наименование данных"] == "ИНН"]["На момент разработки отчета инвентаризации"].values[0],
            df[df["Наименование данных"] == "ОГРН"]["На момент разработки отчета инвентаризации"].values[0],
            df[df["Наименование данных"] == "КПП"]["На момент разработки отчета инвентаризации"].values[0],
            df[df["Наименование данных"] == "ОКОПФ"]["На момент разработки отчета инвентаризации"].values[0],
            df[df["Наименование данных"] == "ОКФС"]["На момент разработки отчета инвентаризации"].values[0],
            df[df["Наименование данных"] == "ОКОГУ"]["На момент разработки отчета инвентаризации"].values[0],
            df[df["Наименование данных"] == "ОКТМО"]["На момент разработки отчета инвентаризации"].values[0],
            df[df["Наименование данных"] == "ОКПО"]["На момент разработки отчета инвентаризации"].values[0],
            df[df["Наименование данных"] == "Коды, присвоенные при постановке на государственный учет ОНВ"]["На момент разработки отчета инвентаризации"].values[0],
            df[df["Наименование данных"] == "Директор"]["На момент разработки отчета инвентаризации"].values[0],
            df[df["Наименование данных"] == "Должностные лица, ответственные за проведение инвентаризации выбросов МБОУ «Мирошкинская СОШ»"]["На момент разработки отчета инвентаризации"].values[0],
            df[df["Наименование данных"] == "Краткая характеристика местности, прилегающей к объекту ОНВ"]["На момент разработки отчета инвентаризации"].values[0],
            df[df["Наименование данных"] == "Размеры и границы санитарно-защитной зоны"]["На момент разработки отчета инвентаризации"].values[0],
            
        ]
    }
    
    # Создаем DataFrame для новой таблицы
    new_df = pd.DataFrame(new_data)
    
    # Отображаем новую таблицу
    st.write("Новая таблица:")
    st.write(new_df)
    
    # Экспорт новой таблицы в CSV
    # csv = new_df.to_csv(index=False, encoding='utf-8-sig').encode('utf-8')
    new_df.to_excel("новая_таблица.xlsx", index=False)
    # Скачиваем Excel-файл
    with open("новая_таблица.xlsx", "rb") as file:
        st.download_button(
            label="Скачать новую таблицу как Excel",
            data=file,
            file_name='новая_таблица.xlsx',
            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        )
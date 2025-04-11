import streamlit as st

number_of_boilers = st.slider("Выберите кол-во котельных:", min_value=1, max_value=10, value=5)

boiler = st.text_input("Марка, тип котла (если есть паспорт)/: ")

boiler_power = st.text_input("Мощность котла:")

num_of_boilers_in_work = st.text_input("Количество котлов в работе/резерве:")

fuel = st.text_input("Введите вид топлива")
fuel_usage = st.text_input("Введите расход топлива")

in_work_days = st.text_input("Количество дней работы котла в год (дн/год)")
in_work_hours = st.text_input("Количество часов работы котла в сутки (ч/сут)")
height = st.text_input("Высота дымовой трубы (от земли), м")
diameter = st.text_input("Диаметр дымовой трубы, м")

if st.button("Отправить"):
    st.session_state["number_of_boilers"] = number_of_boilers
    st.session_state["boiler"] = boiler
    st.session_state["boiler_power"] = boiler_power
    st.session_state["num_of_boilers_in_work"] = num_of_boilers_in_work
    st.session_state["fuel"] = fuel
    st.session_state["fuel_usage"] = fuel_usage
    st.success("Data saved! Navigate to the Output Page to view it.")
# st.write("Характеристики котла:")

# st.write("Марка, тип котла:", boiler)


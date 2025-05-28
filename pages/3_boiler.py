import os
import sys
sys.path.append(os.getcwd())
import streamlit as st
from calculations.fill_document import generate_docx
st.title("Информация о первом источнике загрязнения")
st.text("Нам необходимо знать данные о передвижном источнике загрязнения для выполнения расчётов. Пожалуйста, предоставьте их нам.")

car_types = ["Автобусы карбюраторные особо малые габаритной длиной до 5.5 м (СНГ)", "","Легковые автомобилями выпуска до 01.01.94 г."]
car = st.selectbox("Выберите тип машины", car_types)
car_amount =st.number_input("Введите кол-во таких автомобилей!", value=1)
fuel_type = ["А-92; А-76 ", "АИ-93"]
speed = st.number_input("Введите скорость движения ИЗАВ по объекту ОНВ, (км/ч)", value=10)
fuel = st.selectbox("Выберите тип топлива, который используется автомобилем", fuel_type)
Dp = st.number_input("Введите кол-во дней, которые автомобиль находится в работе", value=181)
Nk = st.number_input("общее количество автомобилей данной группына территории или в помещении стоянки", value=1)
Nkv = st.number_input("среднее количество автомобилей данной группы, выходящих со стоянки в сутки", value=1)
Nkk = st.number_input("Наибольшее количество автомобилей данной группы, выезжающих со стоянки (въезжающих на стоянку) в течении периода времени Tr",value=1)
num_of_days_in_work_car = st.number_input("Введите кол-во дней автомобиля в работе", value=181)
num_of_hours_in_day_in_work_car = st.number_input("Введите кол-во часов автомобиля в работе в день", value=1.5)
L1_warmup = st.number_input("L1 - пробег автомобиля по территории стоянки, км ПРИ ПРОГРЕВЕ", value=0.01)
L2_warmup = st.number_input("L2 - пробег автомобиля по территории стоянки, км ПРИ ПРОГРЕВЕ", value=0.01)
tnp = st.number_input("Введите время прогрева двигателя, мин", value=4)
txx1 = st.number_input("время работы двигателя на холостом ходу при выезде , мин", value=1)
txx2 = st.number_input("время работы двигателя на холостом ходу при возврате, мин", value=1)
L1_warm = st.number_input("L1 - пробег автомобиля по территории стоянки, км ПОСЛЕ ПРОГРЕВА при выезде", value=0.1)
L2_warm = st.number_input("L2 - пробег автомобиля по территории стоянки, км ПОСЛЕ ПРОГРЕВА при возвращении", value=0.1)
Tr = st.number_input("Период максимальной интенсивности выезда техники со стоянки, мин", value=20)
num_of_boilers = st.number_input("Введите кол-во котлов в работе", value=2)
fuel_type = st.text_input("Введите тип топлива", value="газ")
num_of_days_in_work = st.number_input("Введите кол-во дней в работе", value=181)
num_of_hours_in_day_in_work = st.number_input("Введите кол-во часов в день в работе", value=24)
fuel_consumption_year = st.number_input("Введите расход газа вашим котлом (тыс м3 / год)", value=30.05)
throughpout = st.number_input("Введите пропускную способность клапана (ПЕРЕНЕСТИ НА ДРУГУЮ СТРАНИЦУ)", value=20)

num_of_days_in_work_parking = st.number_input("Введите кол-во дней, которые открытая стоянка работает", value=181)
num_of_hours_in_day_in_work_parking = st.number_input("Введите кол-во часов в день работы парковки", value=24)
num_of_parkings = st.number_input("Введите кол-во открытых стоянок!", value=1)

num_of_days_in_work_candle = st.number_input("Введите кол-во дней, которые продувочная свеча работает", value=1)
num_of_hours_in_day_in_work_candle = st.number_input("Введите кол-во часов в день работы продувочной часы", value=1.5)
num_of_candles = st.number_input("Введите кол-во продувочных свечей!", value=1)

if st.button("Отправить"):
    ab = Nkv/Nk
    generate_docx(num_of_boilers, fuel_type, num_of_days_in_work, num_of_hours_in_day_in_work, 
                  fuel_consumption_year, throughpout, tnp, txx1, txx2, L2_warmup, L1_warmup, 
                  ab, Nk, Dp, Tr, L1_warm, L2_warm, Nkv, Nkk, car, speed, num_of_days_in_work_car, num_of_hours_in_day_in_work_car, num_of_days_in_work_parking, 
                  num_of_hours_in_day_in_work_parking, num_of_parkings, num_of_days_in_work_candle, num_of_hours_in_day_in_work_candle, num_of_candles, car_amount)
    st.success("Данные успешно переданы")

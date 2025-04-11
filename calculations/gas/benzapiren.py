import os
import sys
sys.path.append(os.getcwd())

# from calculations.gas.fuel_comsumption import fuel_consumption, fuel_consumption_sec
from calculations.gas.dry import Va
import math
import decimal

Q = 33.66
Vt = 3
# a = 1.08
a = 1.05
kr = 1
kd = 1.5
kst = 2.1
e = 2.71


     
def calculate_amount_of_benzapiren_year(fuel_consumption_year, num_of_days_in_work):
    
    q = fuel_consumption_year * 1000 / (60 * 60 * 24 * num_of_days_in_work) * Q * 1000/ Vt
    Cbp =  0.001 * (0.059 + 0.079 * 0.001 * q) / math.exp(3.8 * (a - 1))* kd * kr * kst

    mbp_year = Cbp * Va  * fuel_consumption_year / 1000000 # т/год
    rounded_year = round(mbp_year,7)
    return rounded_year

def calculate_amount_of_benzapiren_sec(fuel_consumption_sec):
    q = fuel_consumption_sec * Q * 1000/ Vt
    Cbp =  0.001 * (0.059 + 0.079 * 0.001 * q) / math.exp(3.8 * (a - 1))* kd * kr * kst
    mbp = Cbp * Va  * fuel_consumption_sec / 1000 # г/сек
    rounded_sec = round(mbp,9)
    return rounded_sec

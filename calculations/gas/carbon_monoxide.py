# from gas.fuel_comsumption import fuel_consumption_year, fuel_consumption_sec
q3 = 0.2
R = 0.5 # поскольку газ
Q = 33.66
q4 = 0

def calculate_MCO_sec(fuel_consumption_sec):
    MCO_sec = fuel_consumption_sec * q3 * R * Q * (1- q4 / 100)
    MCO_sec = round(MCO_sec, 4)
    return MCO_sec

def calculate_MCO_year(fuel_consumption_year):
    MCO_year = fuel_consumption_year * q3 * 0.001 * R * Q * (1- q4 / 100) * 0.001
    MCO_year = round(MCO_year, 4)
    return MCO_year

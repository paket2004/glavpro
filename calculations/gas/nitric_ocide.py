# from calculations.gas.fuel_comsumption import fuel_consumption_sec, fuel_consumption_year
br = 1
b4 = 0
b3 = 0
b2 = 1.225
t = 22 # ????
b1 = 1 + 0.002 * (t - 30)
Q = 33.66



def calculate_MNO2_g(fuel_consumption_sec):
    Qt = fuel_consumption_sec * Q 
    KNO = 0.013 * Qt **0.5 + 0.03
    MNOx_g = fuel_consumption_sec * Q * KNO * b1 * br * b2 * (1-b3) * (1-b4) * 1 # kn = 1 - г/с
    MNO2_g = 0.8 * MNOx_g
    MNO2_g = round(MNO2_g,4)
    return MNO2_g

def calculate_Mno2_t(fuel_consumption_year, fuel_consumption_sec):
    Qt = fuel_consumption_sec * Q 
    KNO = 0.013 * Qt **0.5 + 0.03
    MNOx_t = fuel_consumption_year * Q * KNO * b1 * br * b2 * (1-b3) * (1-b4) * 0.001 # kn = 1 - г/с
    MNO2_t = 0.8 * MNOx_t
    MNO2_t = round(MNO2_t,6)
    return MNO2_t


def calculate_MNO_g(fuel_consumption_sec):
    Qt = fuel_consumption_sec * Q 
    KNO = 0.013 * Qt **0.5 + 0.03
    MNOx_g = fuel_consumption_sec * Q * KNO * b1 * br * b2 * (1-b3) * (1-b4) * 1 # kn = 1 - г/с
    MNO_g = 0.13 * MNOx_g
    MNO_g = round(MNO_g,6)
    return MNO_g


def calculate_MNO_t(fuel_consumption_year, fuel_consumption_sec):

    Qt = fuel_consumption_sec * Q 
    KNO = 0.013 * Qt **0.5 + 0.03
    MNOx_t = fuel_consumption_year * Q * KNO * b1 * br * b2 * (1-b3) * (1-b4) * 0.001 # kn = 1 - г/с
    MNO_t = 0.13 * MNOx_t
    MNO_t = round(MNO_t,6)
    return MNO_t

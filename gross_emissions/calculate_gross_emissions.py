from gross_emissions.CO import calculate_CO
from gross_emissions.nitric_ocide import calcualte_nitric_ocide
from gross_emissions.sulfur import calculate_SO
from gross_emissions.petrol import calculate_petrol

def calculate_gross_emissions(tnp, txx1, txx2, L2_warmup, L1_warmup, ab, Nk, Dp, Tr, L1_warm, L2_warm, Nkv, Nkk):
    COgik_warmup, COgik_warm, CO_mik_warm, CO_mik_warmup = calculate_CO(L1_warmup, L2_warmup, L1_warm, L2_warm, Dp, Nk, Nkv, Nkk)
    Gno2_warm, Gno2_warm_up, Gno_warm, Gno_warm_up, Mno2_warm, Mno_warm, Mno_warm_up, Mno2_warm_up = calcualte_nitric_ocide(tnp, txx1, txx2, L2_warmup, L1_warmup, ab, Nk, Dp, Tr, L1_warm, L2_warm)
    SOgik, SO_gik_warm, SO_mik, SO_mik_warm = calculate_SO(tnp, txx1, txx2, L2_warmup, L1_warmup, L2_warm, L1_warm, ab, Nk, Dp, Tr)
    petrol_gik_warm, petrol_gik_warmup, petrol_mik_warm, petrol_mik_warmup = calculate_petrol(tnp, txx1, txx2, L2_warm, L2_warmup, L1_warm, L1_warmup, ab, Nk, Dp, Tr)
    COgik_warmup = round(COgik_warmup, 5)
    COgik_warm = round(COgik_warm,6)
    CO_mik_warm = round(CO_mik_warm,6)
    CO_mik_warmup = round(CO_mik_warmup,6 )
    Gno2_warm = round(Gno2_warm,7)
    Gno2_warm_up = round(Gno2_warm_up, 6)
    Gno_warm = round(Gno_warm,7)
    Gno_warm_up = round(Gno_warm_up, 6)
    Mno2_warm = round(Mno2_warm,7)
    Mno_warm = round(Mno_warm,7)
    Mno_warm_up = round(Mno_warm_up,6)
    Mno2_warm_up = round(Mno2_warm_up,6)
    SOgik = round(SOgik,8)
    SO_gik_warm = round(SO_gik_warm,8)
    SO_mik = round(SO_mik,8)
    SO_mik_warm = round(SO_mik_warm,8)
    petrol_gik_warm = round(petrol_gik_warm,7)
    petrol_gik_warmup = round(petrol_gik_warmup,6)
    petrol_mik_warm = round(petrol_mik_warm,7)
    petrol_mik_warmup = round(petrol_mik_warmup,6)
    return COgik_warmup, COgik_warm, CO_mik_warm, CO_mik_warmup, Gno2_warm, Gno2_warm_up, Gno_warm, Gno_warm_up, Mno2_warm, Mno_warm, Mno_warm_up, Mno2_warm_up, SOgik, SO_gik_warm, SO_mik, SO_mik_warm, petrol_gik_warm, petrol_gik_warmup, petrol_mik_warm, petrol_mik_warmup

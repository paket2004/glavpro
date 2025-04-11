# from gross_emissions.nitric_ocide import tnp, txx1, txx2, L2_warm, L2_warmup, L1_warm, L1_warmup, ab, Nk, Dp, Tr
mnpik = 1 * 0.9 # первая 
mLik = 3.15 # стр 15
mxxik = 0.4 # таблица 2.3

def calculate_petrol(tnp, txx1, txx2, L2_warm, L2_warmup, L1_warm, L1_warmup, ab, Nk, Dp, Tr):
    m1ik_warmup = mnpik * tnp + mLik * L1_warmup + mxxik * txx1   

    m2ik_warmup = mLik * L2_warmup + mxxik * txx2

    petrol_mik_warmup = ab * (m1ik_warmup + m2ik_warmup) * Nk * Dp * 1e-6

    petrol_gik_warmup = (mnpik * tnp + mLik * L1_warmup + mxxik * txx1) * Nk / Tr / 60

    m1ik_warm = mLik * L1_warm

    petrol_mik_warm = ab * m1ik_warm * Nk * Dp * 1e-6

    M2ik_warm = mLik * L2_warm

    petrol_gik_warm = M2ik_warm * Nk /Tr / 60
    return petrol_gik_warm, petrol_gik_warmup, petrol_mik_warm, petrol_mik_warmup
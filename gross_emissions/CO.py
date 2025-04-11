# ЭТО ВСЁ ПАРАМЕТРЫ И ИХ НАДО ПОДДТЯГИВАТЬ ОТКУДА-ТО
mnpik = 9.1 * 0.9 #
mxxik = 4.5 #
mLik = 28.5 * 0.9 # cтраница 15
txx1 = 1 # minuta
txx2 = 1 # minuta
tnp = 4 # min
Tr = 20 # min Период максимальной интенсивности выезда техники со стоянки,

def calculate_CO(L1_warmup, L2_warmup, L1_warm, L2_warm, Dp, Nk, Nkv, Nkk):
    ab = Nkv / Nk
    m1ik_warmup = mnpik * tnp + mLik * L1_warmup + mxxik * txx1   

    m2ik_warmup = mLik * L2_warmup + mxxik * txx2

    CO_mik_warmup = ab * (m1ik_warmup + m2ik_warmup) * Nk * Dp * 1e-6

    COgik_warmup = (mnpik * tnp + mLik * L1_warmup + mxxik * txx1) * Nk / Tr / 60

    m1ik_warm = mLik * L1_warm
    CO_mik_warm = ab * m1ik_warm * Nk * Dp * 1e-6
    M2ik_warm = mLik * L2_warm 
    COgik_warm = M2ik_warm * Nkk / Tr / 60
    print(COgik_warm, CO_mik_warm)
    return COgik_warmup, COgik_warm, CO_mik_warm, CO_mik_warmup
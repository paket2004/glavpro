# from gross_emissions.CO import tnp, txx1, txx2, L2_warmup, L1_warmup, ab, Nk, Dp, Tr, L1_warm, L2_warm

mnpik = 0.07

mLik = 0.6

mxxik =  0.05

Kno2 = 0.8
Kno = 0.13

def calcualte_nitric_ocide(tnp, txx1, txx2, L2_warmup, L1_warmup, ab, Nk, Dp, Tr, L1_warm, L2_warm):


    m1ik_warmup = mnpik * tnp + mLik * L1_warmup + mxxik * txx1   

    m2ik_warmup = mLik * L2_warmup + mxxik * txx2

    mik_warmup = ab * (m1ik_warmup + m2ik_warmup) * Nk * Dp * 1e-6

    gik_warmup = (mnpik * tnp + mLik * L1_warmup + mxxik * txx1) * Nk / Tr / 60

    Mno2_warm_up = Kno2 * mik_warmup
    Gno2_warm_up = Kno2 * gik_warmup

    Mno_warm_up = Kno * mik_warmup
    Gno_warm_up = Kno * gik_warmup


    m1ik_warm = mLik * L1_warm

    mik_warm = ab * m1ik_warm * Nk * Dp * 1e-6

    M2ik_warm = mLik * L2_warm

    gik_warm = M2ik_warm * Nk /Tr / 60

    Mno2_warm = Kno2 * mik_warm
    Gno2_warm = Kno2 * gik_warm

    Mno_warm = Kno * mik_warm
    Gno_warm = Kno * gik_warm
    return Gno2_warm, Gno2_warm_up, Gno_warm, Gno_warm_up, Mno2_warm, Mno_warm, Mno_warm_up, Mno2_warm_up
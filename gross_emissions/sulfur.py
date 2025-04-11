mnpik = 0.016 * 0.9
mxxik = 0.012
mLik = 0.11 * 0.9

def calculate_SO(tnp, txx1, txx2, L2_warmup, L1_warmup, L2_warm, L1_warm, ab, Nk, Dp, Tr):
    m1ik = mnpik * tnp + mLik * L1_warmup + mxxik * txx1   

    m2ik = mLik * L2_warmup + mxxik * txx2

    SO_mik = ab * (m1ik + m2ik) * Nk * Dp * 1e-6

    SOgik = (mnpik * tnp + mLik * L1_warmup + mxxik * txx1) * Nk / Tr / 60

    m1ik_warm = mLik * L1_warm

    SO_mik_warm = ab * m1ik_warm * Nk * Dp * 1e-6

    M2ik_warm = mLik * L2_warm

    SO_gik_warm = M2ik_warm * Nk /Tr / 60
    return SOgik, SO_gik_warm, SO_mik, SO_mik_warm
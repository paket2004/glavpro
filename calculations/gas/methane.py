# Введите пропускную способность
t = 600
def calculate_methane(throughpout: int):
    Q_hour = 0.0005 * throughpout
    Q_sec = Q_hour * 0.684 * 1000 / 3600
    methane_g_s = Q_sec * t / 1200
    methane_g_y = Q_sec * t * 12 # видимо время работы в месяц и кол-во месяцев
    methane_t_y = methane_g_y / 1000000
    methane_g_y = round(methane_g_y, 6)
    methane_t_y= round(methane_t_y, 6)
    return methane_g_s, methane_t_y

def calculate_ethanethiol(throughpout: int):
    Q_hour = 0.0005 * throughpout
    Q_sec = Q_hour * 0.684 * 1000 / 3600
    Q = Q_sec * 16  / 3600 / 1000
    ethanethiol_g_s = Q * t / 1200
    ethanethiol_g_y = Q * t * 12
    ethanethiol_t_y = ethanethiol_g_y / 1000000
    ethanethiol_g_s = round(ethanethiol_g_s, 10)
    ethanethiol_t_y = round(ethanethiol_t_y, 12)
    return ethanethiol_g_s, ethanethiol_t_y
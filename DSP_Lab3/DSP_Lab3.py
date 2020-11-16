import math
import numpy as np
import matplotlib.pyplot as ppl
import csv

ampl = 0.1
snr_db = 1

def calc_ratio(snr_db):
    return ampl / (10 ** (snr_db / 20))

def visualize(t, sn, title):
    ppl.xlabel('t, с')
    ppl.ylabel('sn, В')
    ppl.title(title)
    ppl.xticks(np.linspace(t[0], t[-1], 5))
    ppl.plot(t, sn, 'C0')
    ppl.show()

snr = calc_ratio(snr_db)
print('Амплитудный коэффициент для шумовых отсчетов:', snr)

with open('..\\DSP_Lab1\\1_signal.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    filtered = list(filter(lambda row: len(row) != 0, reader))[1:]
    t = list(map(lambda row: float(row[0]), filtered))
    sig = list(map(lambda row: float(row[1]), filtered))

with open('..\\DSP_Lab2\\1_noise.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    filtered = list(filter(lambda row: len(row) != 0, reader))[1:]
    noise = list(map(lambda row: float(row[1]), filtered))

sn = list(map(lambda t: (t[0], t[1] + t[2] * snr), zip(t, sig, noise)))

with open('1_sn.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    rows = [('t', 'sn')] + sn
    writer.writerows(rows)

fragm_len = len(t) // 100 + 1
t_fragment = t[:fragm_len]
sn_fragment = sn[:fragm_len]

visualize(t_fragment, sn_fragment, 'Сигнал + шум')


# по смеси (или сигналу, шуму) посчитать угол между сигналом и шумом (по скалярному произведению), сделать вывод

from functools import reduce

def calc_norm(s):
    return math.sqrt(
        reduce(lambda x1, x2: x1 + x2, 
               map(lambda x: x**2, s)))

sc_prod = reduce(lambda x1, x2: x1 + x2, 
                 map(lambda x, y: x * y, sig, noise))

cos_phi = sc_prod / (calc_norm(sig) * calc_norm(noise))
phi = math.degrees(math.acos(cos_phi))
print(phi)

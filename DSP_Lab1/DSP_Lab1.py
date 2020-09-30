import math
import numpy as np
import matplotlib.pyplot as ppl
import csv

ampl = 0.1
offset = 0
freq = 12207.03125
phase = 0
samp_freq = 100 * 1000
duration = 100 / 1000

def calc(ampl, offset, freq, phase, samp_freq, duration):
    samp_count = math.floor(samp_freq * duration) + 1
    model_freq = freq / samp_freq
    phase_rad = math.pi * (phase / 180)
    return samp_count, model_freq, phase_rad

def signal(t):
    return np.cos(2 * math.pi * freq * t + phase_rad) * ampl + offset

def visualize(t, title):
    s = signal(t)
    ppl.xlabel('t, с')
    ppl.ylabel('s(t), В')
    ppl.title(title)
    ppl.plot(t, s)
    ppl.show()

samp_count, model_freq, phase_rad = calc(
    ampl,
    offset,
    freq,
    phase,
    samp_freq,
    duration)

print('Количество отчетов для моделирования:', samp_count)
print('Частота сигнала в модели:', model_freq)
print('Начальная фаза в радианах:', phase_rad)

t = np.round(np.linspace(0, duration, samp_count), 7)
visualize(t, 'Сигнал')

t_fragment = np.round(np.linspace(0, duration / 10, int((samp_count - 1) / 10 + 1)), 7)
visualize(t_fragment, 'Сигнал (укрупненный фрагмент)')

with open('1_signal.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    rows = [('t', 's(t)')] + list(zip(t, signal(t)))
    writer.writerows(rows)
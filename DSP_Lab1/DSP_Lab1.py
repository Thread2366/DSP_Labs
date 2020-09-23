import math
import numpy as np
import matplotlib.pyplot as ppl
import json

ampl = 0.1
offset = 0
freq = 12207.03125
phase = 0
samp_freq = 100 * 1000
duration = 100 / 1000

def calc(ampl, offset, freq, phase, samp_freq, duration):
    samp_count = math.floor(samp_freq * duration) + 1
    model_freq = freq
    phase_rad = math.pi * (phase / 180)
    return samp_count, model_freq, phase_rad

def visualize(start, end, samp_count, ampl, offset, model_freq, phase_rad):
    t = np.linspace(start, end, samp_count)
    s = np.cos(2 * math.pi * model_freq * t + phase_rad) * ampl + offset
    ppl.plot(t, s)
    ppl.show()

samp_count, model_freq, phase_rad = calc(
    ampl,
    offset,
    freq,
    phase,
    samp_freq,
    duration)

print("Количество отчетов для моделирования:", samp_count)
print("Частота сигнала в модели:", model_freq)
print("Начальная фаза в радианах:", phase_rad)

visualize(0, duration, samp_count, ampl, offset, model_freq, phase_rad)
visualize(0, duration / 10, (samp_count - 1) / 10 + 1, ampl, offset, model_freq, phase_rad)
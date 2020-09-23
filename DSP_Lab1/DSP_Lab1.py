import math
import numpy as np
import matplotlib.pyplot as ppl
import json

def calc(ampl, offset, freq, phase, samp_freq, duration):
    samp_count = math.floor(samp_freq * duration) + 1
    model_freq = 0
    phase_rad = math.pi * (phase / 180)
    return samp_count, model_freq, phase_rad

def visualize():
    pass


with open("input.json", "r") as file:
    json_text = file.read()
inp = json.loads(json_text)

samp_count, model_freq, phase_rad = calc(
    inp["amplitude"],
    inp["offset"],
    inp["frequency"],
    inp["phase"],
    inp["samplingFrequency"],
    inp["duration"])

print("Количество отчетов для моделирования:", samp_count)
print("Частота сигнала в модели:", model_freq)
print("Начальная фаза в радианах:", phase_rad)


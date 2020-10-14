import math
import numpy as np
import matplotlib.pyplot as ppl
import csv
import random as rnd

def noise(t):
    size = len(t)
    return np.random.uniform(-1, 1, size)

def visualize(t, ns, title):
    ppl.xlabel('t, с')
    ppl.ylabel('noise, В')
    ppl.title(title)
    ppl.xticks(np.linspace(t[0], t[-1], 5))
    ppl.plot(t, ns)
    ppl.show()

with open('..\\DSP_Lab1\\1_signal.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    filtered = list(filter(lambda row: len(row) != 0, reader))[1:]
    t = list(map(lambda row: float(row[0]), filtered))

ns = noise(t)

with open('1_noise.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    rows = [('t', 'noise')] + list(zip(t, ns))
    writer.writerows(rows)

print(round(np.mean(ns), 2))
print(round(np.std(ns) ** 2, 2))

fragm_len = len(t) // 100 + 1
t_fragment = t[:fragm_len]
ns_fragment = ns[:fragm_len]

visualize(t_fragment, ns_fragment, 'Шум')
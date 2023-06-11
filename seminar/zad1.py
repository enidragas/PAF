import matplotlib.pyplot as plt
import numpy as np
import kosi_hitac as kh

p1 = kh.Particle(10, 45, 0, 20, 200, 0.01)
p1.putanja()
p1.maksimalna_visina()
p1.domet()
p1.maksimalna_brzina()
p1.meta(10, 10, 5)
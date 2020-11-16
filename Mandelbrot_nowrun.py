import numpy as np
import matplotlib.pyplot as plt
import statistics
import math
import lhsmdu
import time

from PIL import Image, ImageDraw


def amount_iter(compl, max_steps, threshold_inf: int = 10):
    c = compl
    z = 0
    i = 0
    while (z*z.conjugate()).real < threshold_inf and i < max_steps:
        z = z**2 + c
        i += 1
    return i

def xy_LHS(x):
    l = lhsmdu.sample(2,x)
    x,y = (l[0][0]), (l[1][0])
    x = x.tolist()
    x = x[0]
    for xind in range(len(x)):
        x[xind] = 3*x[xind]-2
    y = y.tolist()
    y = y[0]
    for yind in range(len(y)):
        y[yind] = 2*y[yind]-1
    return x,y


## Approximation by LHS

start = time.time()

samples = [100, 200, 500, 1000]
listLHS = [[],[],[],[]]
max_steps = 1000 # this is equal to i
maxmax_steps = 1000

for value in range(len(samples)):
    print("Amount of samples: " + str(samples[value]))
    for max_steps in range(maxmax_steps):
        t = 0
        x_LHS,y_LHS = xy_LHS(samples[value])
        if max_steps%100 == 0:
            print("Percentage: "+ str(max_steps/maxmax_steps * 100) + "%")
        for index in range(len(x_LHS)):
#             print(index)
            x, y = x_LHS[index], y_LHS[index]
            m = amount_iter(complex(x,y), max_steps)
            if m == max_steps:
                t += 1
    #     print(t/it*6)
        listLHS[value].append(t/samples[value]*6)


for i in range(len(samples)):
    print(statistics.mean(listLHS[i]))
    print(statistics.stdev(listLHS[i]))
    print(listLHS[i][-1])

end = time.time()
print("Running time: " + str(end - start))

data = np.array(listLHS)
np.savez("Myfile", data)

import matplotlib.pyplot as plt
import numpy as np



labels1 = [i for i in range(1000,6000,1000)]
labels2 = [i for i in range(6000,11000,1000)]

pc = [
      0.9892232418060303,
            10.598870515823364,
            34.88852858543396,
            109.62109637260437,
            179.50116634368896,
            364.8732559680939,
            544.3221867084503,
            1255.395488500595,
            1325.6269969940186,
            2095.555953979492]



colab = [
    1.146564245223999,
                13.85277771949768,
                53.977993965148926,
                249.89103150367737,
                293.59917187690735,
                612.5278112888336,
                828.314866065979,
                2533.58340215683,
                1985.1021757125854,
                4371.168046712875]



plt.figure(1)
x = np.arange(len(labels1))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, pc[:5], width, label='PC')
rects2 = ax.bar(x + width/2, colab[:5], width, label='Colab')

ax.set_ylabel('Time, sec')
ax.set_xlabel('Matrix size, MxM')
ax.set_title('Matrix calculation time with numpy')
ax.set_xticks(x)
ax.set_xticklabels(labels1)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=16)

fig.tight_layout()
plt.savefig('plot_000.jpeg',dpi=300)

x = np.arange(len(labels2))  # the label locations
plt.figure(2)
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, pc[5:], width, label='PC')
rects2 = ax.bar(x + width/2, colab[5:], width, label='Colab')

ax.set_ylabel('Time, sec')
ax.set_xlabel('Matrix size, MxM')
ax.set_title('Matrix calculation time with numpy')
ax.set_xticks(x)
ax.set_xticklabels(labels2)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()
plt.savefig('plot_111.jpeg',dpi=300)


#plt.show()
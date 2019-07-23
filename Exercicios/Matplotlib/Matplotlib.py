import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,100); print(x)
y = 2 * x
z = x ** 2

# Exercicio 1

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])

ax.plot(x, y)
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_title('y= 2x')

## plt.show()

# Exercicio 2

fig = plt.figure()
ax1 = fig.add_axes([0, 0, 1, 1])
ax2 = fig.add_axes([0.2, 0.5, .2, .2])

ax1.plot(x, y)
ax2.plot(x, y)
ax1.set_xlabel('Eixo X')
ax1.set_ylabel('Eixo Y')
ax1.set_title('y= 2x')

## plt.show()

# Exercicio 3

fig = plt.figure()
ax1 = fig.add_axes([0, 0, 1, 1])
ax2 = fig.add_axes([0.2, 0.5, .4, .4])

ax1.set_xlabel('Eixo X')
ax1.set_ylabel('Eixo Z')
ax1.set_title('y = x^2')

ax2.set_xlabel('Eixo X')
ax2.set_ylabel('Eixo Z')
ax2.set_title('y = x^2')

ax1.plot(x, z)
ax2.plot(x, y)

ax2.set_xlim(20, 22)
ax2.set_ylim(30, 50)
ax1.set_xlim(0, 100)
ax1.set_ylim(0, 10000)

ax1.plot(x, z)
ax2.plot(x, y)
## plt.show()

# Exercicio 4

fig, ax = plt.subplots(ncols = 2, nrows = 1, figsize = (7, 7))
print(ax)

ax[0].plot(x, y, 'b-')
# ax[0].plot(x, y, color = 'blue', lw = 3, ls = '--')
ax[0].set_xlabel('Eixo X')
ax[0].set_ylabel('Eixo Z')
ax[0].set_title('y = x^2')

ax[1].plot(x, z, 'r')
# ax[0].plot(x, y, color = 'red', lw = 3, ls = '-')
ax[1].set_xlabel('Eixo X')
ax[1].set_ylabel('Eixo Z')
ax[1].set_title('y = x^2')

plt.show()

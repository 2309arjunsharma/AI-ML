import numpy
import matplotlib.pyplot as plt

y = numpy.random.normal(5, 1, 25000)

plt.hist(y, 100)
plt.show()

x = numpy.random.uniform(0, 5, 25000)

print(x)

a = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
v = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(a, v)
plt.show()
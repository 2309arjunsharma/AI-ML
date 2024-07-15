import numpy
from scipy import stats
num = [1,2,3,4,5,6,7,8,9,10,10,2,3,4,5,6,7,8,9,10,11,11,12,13,12,14]
x = numpy.mean(num)
y = numpy.median(num)
z = stats.mode(num)
a = numpy.std(num)
b = numpy.var(num)
c = numpy.percentile(num, 75)
print("Mean is",x,",median is",y,",mode is",z," and standard deviation is",a)
print("Variance is",b,", percentile is",c)

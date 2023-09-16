import random
import math

from pyspark import SparkContext

sc = SparkContext(appName="EstimatePi")

def inside(p):

    a, b = random.uniform(-1.0,1.0), random.uniform(-1.0,1.0)
    return a*a + b*b < 1

n_total = 1000000

count = sc.parallelize(range(0, n_total)).filter(inside).count()

print("Accuracy : ", 100.0*math.fabs((float(4.0 * count / n_total) - math.pi)), "per cent")
print("Pi is roughly", float(4.0 * count / n_total))

sc.stop()
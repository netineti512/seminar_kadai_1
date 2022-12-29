import numpy as np
import matplotlib.pyplot as plt

X = [1452, 1796, 1894, 2584, 2735, 3447]
Y = [3231, 3747, 3726, 5853, 8855, 10913]

annotations=["2014","2015","2016","2017","2018","2019"]

plt.figure(figsize=(8,6))
plt.scatter(X,Y,s=100)
plt.xlabel("オープンキャンパス参加者人数(人)",fontname="MS Gothic",fontsize=15)
plt.ylabel("志願者数(人)",fontname="MS Gothic",fontsize=15)
plt.title("散布図",fontname="MS Gothic",fontsize=15)
for i, label in enumerate(annotations):
    plt.annotate(label, (X[i], Y[i]))

plt.show()
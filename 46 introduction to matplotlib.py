#matplotlib
from matplotlib import pyplot as plt
plt.title("title")
x1=[1,2,3]
y1=[5,7,9]
x2=[7,8,1]
y2=[3,2,4]
plt.plot(x1,y1,color='g',label="today's sale",linewidth=2)
plt.plot(x2,y2,color='y',label="yesterday's sale",linewidth=2)
plt.xlabel("day")
plt.ylabel("sales")
plt.legend()
plt.grid(True,color="c")
plt.show()

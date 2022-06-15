import numpy as np
import matplotlib.pyplot as plt
x = np.arange(1,20)  #用numpy生成x坐标点
print(x)
y = x*x              #生成y坐标的值
print(y.shape)
plt.title("juzicode")#设置标题
plt.plot(x,y,'*--g') #绘图
plt.show()         #显示图片
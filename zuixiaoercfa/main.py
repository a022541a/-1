import numpy as np
import random
import time
import matplotlib.pyplot as plt

l=[]
def shengcheng_seed(x1,x2): #以当前时间为seed生成随机坐标,需要传入范围
    a=time.time()
    random.seed(a)
    for i in range(100):
        c=[random.randint(x1,x2),random.randint(x1,x2)]
        if c not in l:
            l.append(c)

    return l
def zuixiao(dian):    #最小二乘法计算，需传入list的坐标点
    A=[]
    B=[]
    for i in dian:
        A.append([i[0]**0,i[0]**1])
        B.append([i[1]])

    A_J=np.matrix(A)
    B_J=np.matrix(B)
    X=((A_J.T*A_J).I)*A_J.T*B_J
    return X                    #返回2*1的矩阵，依次是x0与x1








if __name__ == '__main__':

    a=shengcheng_seed(0,1000)
    b1=zuixiao(a)
    x1=b1[1,0]
    x0=b1[0,0]

    #print(b[1,0])

    # 样本点
    Xi=[]
    Yi=[]
    for i in a:
        Xi.append(i[0])
        Yi.append(i[1])

    plt.figure(figsize=(8, 6))  ##指定图像比例
    plt.scatter(Xi, Yi, color="green", label="example", linewidth=1) #样本点绿色

    # 拟合直线
    x = np.linspace(0, 1000, 100)  ##在0-15直接画100个连续点
    y = x1 * x + x0 ##函数式
    plt.plot(x, y, color="red", label="zhixian", linewidth=2) #拟合直线红色
    plt.legend(loc='lower right')  # 绘制图例
    plt.show()






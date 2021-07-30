import random
import numpy as np
import math


# sigmoid函数
def sigmoid(x):
    return 1/(1 + np.exp(-x))


# softmax函数
def softmax(x):
    return np.exp(x - np.max(x)) / np.sum(np.exp(x - np.max(x)))


# sigmoid归一化并存储
def save_sigmoid():
    sig = list(sigmoid(data_n))
    print(sig)
    with open(r'sigmoid.txt', 'w+') as f1:
        e = ''
        for i in range(len(data)):
            e = e + data[i][0] + ' ' + data[i][1] + ' ' + str(sig[i])
            f1.write(e.strip(' '))
            f1.write('\n')
            e = ''


# sigmoid归一化并存储
def save_softmax():
    soft = softmax(np.array(data_n))
    print(soft)
    with open(r'softmax.txt', 'w+') as f1:
        e = ''
        for i in range(len(data)):
            e = e + data[i][0] + ' ' + data[i][1] + ' ' + str(soft[i])
            f1.write(e.strip(' '))
            f1.write('\n')
            e = ''


# 保存知识图谱三元组，用户-关系-用户，这里关系均为1
def save_kg(filename):
    with open(filename, 'w+') as f2:
        e = ''
        for i in range(len(data)):
            # e = e + data[i][0] + ' ' + str(1) + ' ' + data[i][1]
            e = e + data[i][0] + ' ' + str(1) + ' ' + data[i][1]
            f2.write(e.strip(' '))
            f2.write('\n')
            e = ''
        for i in range(len(data)):
            e = e + data[i][1] + ' ' + str(1) + ' ' + data[i][0]
            f2.write(e.strip(' '))
            f2.write('\n')
            e = ''


def save_n(filename):
    with open(filename, 'w+') as f3:
        e = ''
        for i in range(len(data)):
            e = e + data[i][0] + ' ' + data[i][1] + ' ' + str(1)
            f3.write(e.strip(' '))
            f3.write('\n')
            e = ''
        for i in range(len(data)):
            e = e + data[i][1] + ' ' + data[i][0] + ' ' + str(1)
            f3.write(e.strip(' '))
            f3.write('\n')
            e = ''


with open(r'C:\Users\86138\Desktop\PinSAGE_lastfm_top_k\k2\PinSAGE_lastfm_top_2.txt', 'r') as f:
    data = []
    data_n = []
    for line in f:
        a = line.split()
        data.append(a[:-1])
        b = a[-1]
        data_n.append(float(b))
data_n = np.array(data_n)

# save_softmax()
# save_sigmoid()
save_kg(r'C:\Users\86138\Desktop\PinSAGE_lastfm_top_k\k2\lastfm_trusts_kg.txt')
save_n(r'C:\Users\86138\Desktop\PinSAGE_lastfm_top_k\k2\lastfm_trusts_n.txt')

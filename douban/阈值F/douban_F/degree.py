import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tqdm import tqdm


def addtrustdata(path):
    print('向用户字典添加信任数据')
    with open(path, 'r') as f1:
        trust_data = []
        for line in f1:
            a = line.split()
            trust_data.append(a)
    for i in tqdm(range(len(trust_data))):
        ind = trust_data[i][0]
        ind_1 = trust_data[i][1]
        user[str(ind)]['nei'].append(trust_data[i][1])
        user[str(ind_1)]['nei'].append(trust_data[i][0])
        user[str(ind)]['nei'] = list(set(user[str(ind)]['nei']))
        user[str(ind_1)]['nei'] = list(set(user[str(ind_1)]['nei']))


def readratingdata(path):
    print('正在读取评分数据')
    user_set = set()
    item_set = set()
    with open(path, 'r') as f:
        for line in tqdm(f):
            a = line.split()
            user_set.add(int(a[0]))
            item_set.add(int(a[1]))
    return list(user_set), list(item_set)


def iniuserdic(user_id):
    print('正在初始化用户字典')
    user = {}
    for i in tqdm(user_id):
        user[str(i)] = {}
        user[str(i)]['nei'] = []
        user[str(i)]['item'] = {}
    return user


def additemdata(path):
    print('向用户字典中添加项目数据')
    with open(path, 'r') as f:
        ratings_data = []  # 初始数据集
        for line in f:
            a = line.split()
            ratings_data.append(a)
    for i in tqdm(range(len(ratings_data))):
        user[str(ratings_data[i][0])]['item'][str(ratings_data[i][1])] = int(ratings_data[i][2])


def save_degree(filename):
    degree = []
    for i in range(len(user)):
        degree.append(len(user[str(user_id[i])]['nei']))
    print(degree)
    with open(filename, 'w+') as f2:
        f2.write(str(degree)[1:-1])


if __name__ == '__main__':
    rating_path = 'ratings.txt'  # 评分数据路径
    trust_path = r'C:\Users\86138\Desktop\douban_data\0.09\douban_user_nei.txt'  # 信任数据路径
    user_id, item_id = readratingdata(rating_path)
    user = iniuserdic(user_id)  # 初始化用户字典
    addtrustdata(trust_path)  # 添加信任数据
    additemdata(rating_path)  # 添加项目数据
    save_degree(r'C:\Users\86138\Desktop\douban_data\0.09\douban_degree.txt')



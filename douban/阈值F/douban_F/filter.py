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


def sim_stru_f():
    print('正在计算结构相似度')
    sim_stru = []
    for i in tqdm(user_id):
        # print(i)
        sim_stru_m = []
        for j in user:
            # print(j)
            if len(set(user[str(i)]['nei']).union(set(user[str(j)]['nei']))) != 0:
                sim_stru_m.append(len(set(user[str(i)]['nei']).intersection(set(user[str(j)]['nei']))) /
                                  len(set(user[str(i)]['nei']).union(set(user[str(j)]['nei']))))
            else:
                sim_stru_m.append(0)
        sim_stru.append(sim_stru_m)
    sim_stru = np.array(sim_stru)
    return sim_stru


def sim_pre_f():
    print('正在计算偏好相似度')
    item_tal = []
    for i in tqdm(user_id):
        item_tal.append(user[str(i)]['item'])
    dict_vectorizer = DictVectorizer(dtype=np.int32, sparse=False)
    result = dict_vectorizer.fit_transform(item_tal)  # 返回矩阵
    items = dict_vectorizer.get_feature_names()  # 项目标号
    sim_pref = cosine_similarity(result)
    return sim_pref


def sim_final_f():
    print('正在计算总相似度')
    sim_final = []
    w1 = 0.5  # 结构相似度权重
    w2 = 1 - w1  # 偏好相似度权重
    for i in tqdm(range(len(user_id))):
        sim_final_m = []
        for j in range(len(user_id)):
            sim_final_m.append(w1 * float(sim_s[i][j]) + w2 * float(sim_p[i][j]))
        sim_final.append(sim_final_m)
    sim_final = np.array(sim_final)
    return sim_final


def filter_f():
    print('正在过滤相似度低的邻居')
    threshold = 0.1
    for i in tqdm(range(len(user_id))):
        for j in range(len(user_id)):
            if sim_f[i][j] < threshold:
                if str(user_id[j]) in user[str(user_id[i])]['nei']:
                    user[str(user_id[i])]['nei'].remove(str(user_id[j]))


def addnei():
    print('正在根据偏好相似度给没有邻居的用户添加邻居')
    for i in tqdm(range(len(user_id))):
        nei_n = []
        if len(user[str(user_id[i])]['nei']) == 0:
            # print(i)
            for j in range(len(user_id)):
                if sim_p[i][j] == 1 or i == j:
                    sim_p[i][j] = 0
                nei_n.append(sim_p[i][j])
            k = list(sim_p[i]).index(max(nei_n))
            user[str(user_id[i])]['nei'].append(str(user_id[k]))
            user[str(user_id[k])]['nei'].append(str(user_id[i]))
            # print(user[str(user_id[i])]['nei'])


# 存储当前相似度
def save_sim_f():
    np.savetxt(r'C:\Users\86138\Desktop\douban_data\0.1\douban_sim_final.txt', sim_f)


def save_f():
    print('正在存储过滤后的信任数据')
    q = ''
    with open(r'C:\Users\86138\Desktop\douban_data\0.1\douban_user_nei.txt', 'w+') as w:
        for i in tqdm(range(len(user_id))):
            if len(user[str(user_id[i])]['nei']) != 0:
                for j in range(len(user[str(user_id[i])]['nei'])):
                    if user_id[i] != user[str(user_id[i])]['nei'][j]:
                        # print(i, user[str(i)]['nei'][j])
                        n = int(user[str(user_id[i])]['nei'][j])
                        n1 = user_id.index(n)
                        q = str(user_id[i]) + ' ' + user[str(user_id[i])]['nei'][j] + ' ' + '1' + ' ' + str(sim_f[i][n1])
                        w.write(q.strip(' '))
                        w.write('\n')
                        q = ''


if __name__ == '__main__':
    rating_path = 'ratings.txt'  # 评分数据路径
    trust_path = 'trusts.txt'  # 信任数据路径
    user_id, item_id = readratingdata(rating_path)
    user = iniuserdic(user_id)  # 初始化用户字典
    addtrustdata(trust_path)  # 添加信任数据
    additemdata(rating_path)  # 添加项目数据
    sim_s = sim_stru_f()  # 计算结构相似度
    sim_p = sim_pre_f()  # 计算偏好相似度
    sim_f = sim_final_f()  # 计算最终相似度
    save_sim_f()  # 保存当前相似度
    print(sim_s)
    print(sim_p)
    print(sim_f)
    filter_f()  # 过滤
    addnei()  # 给没有邻居的用户添加邻居
    save_f()  # 保存过滤后的信任数据

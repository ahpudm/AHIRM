import numpy as np
import pandas as pd


# txt转csv
def txt_to_csv(filename, savename):
    txt = np.loadtxt(filename)
    txtDF = pd.DataFrame(txt)
    txtDF.to_csv(savename, index=False)


# txt转tsv
def txt_to_tsv(txt, tsv):
    with open(tsv, 'w+', encoding="utf8")as t:
        with open(txt, 'r', encoding='utf8')as f:
            # print(f.readlines())
            for line in f.readlines():
                # print(line)
                line_list = line.strip('\n').split()  # 去掉str左右端的空格并以空格分割成list
                # print(line_list)
                hbaseRowID_list = line_list[0:3]  # 取前三个list中的元素
                hbaseRowID = " ".join(hbaseRowID_list)  # 连接list
                line_list[2] = hbaseRowID
                tsv_list = line_list[2:]
                tsv_list = '\t'.join(tsv_list)
                print(tsv_list)
                t.write(tsv_list + '\n')


if __name__ == '__main__':
    # txt_to_tsv('douban_ratings.txt', 'douban_ratings.tsv')
    txt_to_tsv(r'C:\Users\86138\Desktop\PinSAGE_douban_w1\bine\douban_trusts_kg.txt', r'C:\Users\86138\Desktop\PinSAGE_douban_w1\bine\douban_trusts_kg.tsv')
    txt_to_tsv(r'C:\Users\86138\Desktop\PinSAGE_douban_w1\bine\douban_trusts_n.txt', r'C:\Users\86138\Desktop\PinSAGE_douban_w1\bine\douban_trusts_n.tsv')

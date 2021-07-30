#
# import matplotlib.pyplot as plt
#
# name_list = ['Global 6', 'Global 7', 'Global 8', 'Global 9','Global 10']
# # num_list = [4, 4, 4, 4, 4]
# # num_list = [4.5,4.5,4.5,4.5,4.5]
# # num_list2 = [4,4,4,4,4]
# # num_list3 = [4.5,4.5,4.5,4.5,4.5]
# # num_list4 = [5,5,5,5,5]
# num_list = [4.5,4.5,4,3.75,3.75]
# num_list2 = [4,4,3.5,3.5,3.5]
# num_list3 = [4.5,4.5,4,4,3.75]
# num_list4 =[5,5,4.5,4.5,4.5]
# x = list(range(len(num_list)))
# total_width, n = 0.8, 6
# width = total_width / n
# plt.figure(figsize=(10, 6))
# plt.xlabel("Global ID")
# plt.ylabel("Score")
# plt.ylim(2, 5.1)
# # plt.bar(x, num_list, width=width, label='Initial', tick_label=name_list, fc='y')
# for i in range(len(x)):
#     x[i] = x[i] + width
# plt.bar(x, num_list, width=width, label='Season', tick_label=name_list, fc='white',hatch="/",edgecolor='k')
# for i in range(len(x)):
#     x[i] = x[i] + width
# plt.bar(x, num_list2, width=width, label='Longitude', tick_label=name_list, fc='white',hatch="x",edgecolor='k')
# for i in range(len(x)):
#     x[i] = x[i] + width
# plt.bar(x, num_list3, width=width, label='Latitude', tick_label=name_list, fc='white',hatch="\\",edgecolor='k')
# for i in range(len(x)):
#     x[i] = x[i] + width
# plt.bar(x, num_list4, width=width, label='Lab status', tick_label=name_list, fc='white',hatch="+",edgecolor='k')
# plt.legend(['Season','Longitude','Latitude','Lab status'],labelspacing=-0.1)
# plt.show()
# import pandas as pd
# from rom collections import Counter
# import matplotlib.pyplot as plt
#
#  microwave = pd.read_csv(r'C:\Users\24543\Desktop\Problem_C_Data\microwave.tsv', header=0, sep='\t',
#                          usecols=[7], engine="python", encoding='UTF-8')
#  microwave.mean()
#  counts = Counter(microwave.star_rating)
#  print(counts)
#
#  counts = [2069, 14, 2342, 15]
#  plt.figure(figsize=(12, 7))
#  plt.subplot(121)
#  x = range(1, 5)
#  y = [2069, 14, 2342, 15]
#  labels = ['Negative ID', 'Positive ID', 'Unverified', 'Unprocessed']
#  plt.bar(x, y, label='counts', color='coral', hatch='\\', edgecolor='k')
#  for xx, yy in zip(x, y):
#      plt.text(xx, yy + 0.1, str(yy), ha='center', fontsize=12)
#  plt.xticks(x, labels,fontsize=12)
#  plt.xticks(fontsize=12)
#  plt.xlabel('type', fontsize=15)
#  plt.ylabel('counts', fontsize=15)
#  plt.legend(loc='best')
#
#  plt.subplot(122)
#  colors = ['r', 'orange', 'gold', 'deepskyblue']
#  rate = [counts[0] / 4440, counts[1] / 4440, counts[2] / 4440, counts[3] / 4440]
#  # patches, l_texts, p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本
#  patches, l_text, p_text = plt.pie(rate, colors=colors, autopct='%3.1f%%', startangle=65, shadow=False,
#                                    labels=['Negative ID', 'Positive ID', 'Unverified', 'Unprocessed'])
#  pie_wedge_collection = plt.pie(rate, colors=colors, startangle=65, shadow=False)
#
#  # 设置边框线
#  for pie_wedge in pie_wedge_collection[0]:
#      pie_wedge.set_edgecolor('black')
#
#  # 修改字体大小
#  for t in l_text:
#      t.set_size(15)
#  for t in p_text:
#      t.set_size(15)
#
#  plt.legend(loc='best')
#  plt.show()
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
#
# # microwave = pd.read_csv(r'C:\Users\24543\Desktop\Problem_C_Data\microwave.tsv', header=0, sep='\t',
# #                         usecols=[7], engine="python", encoding='UTF-8')
# # microwave.mean()
# # counts = Counter(microwave.star_rating)
# # print(counts)
#
# counts = [2069, 14, 2342, 15]
# plt.figure(figsize=(12, 7))
# plt.subplot(121)
# x = range(1, 5)
# y = [2069, 14, 2342, 15]
# labels = ['Negative ID', 'Positive ID', 'Unverified', 'Unprocessed']
# plt.bar(x, y, label='counts', color='white', hatch='\\', edgecolor='k')
# for xx, yy in zip(x, y):
#     plt.text(xx, yy + 0.1, str(yy), ha='center', fontsize=12)
# plt.xticks(x, labels,fontsize=12)
# plt.xticks(fontsize=12)
# plt.xlabel('type', fontsize=15)
# plt.ylabel('counts', fontsize=15)
# plt.legend(loc='best')
#
# plt.subplot(122)
# colors = ['white']
# rate = [counts[0] / 4440, counts[1] / 4440, counts[2] / 4440, counts[3] / 4440]
# # patches, l_texts, p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本
# patches, l_text, p_text = plt.pie(rate, colors=colors, autopct='%3.1f%%', startangle=65, shadow=False,
#                                   labels=['Negative ID', 'Positive ID', 'Unverified', 'Unprocessed'])
# pie_wedge_collection = plt.pie(rate, colors=colors, startangle=65, shadow=False)
#
# # 设置边框线
# for pie_wedge in pie_wedge_collection[0]:
#     pie_wedge.set_edgecolor('black')
#
# # 修改字体大小
# for t in l_text:
#     t.set_size(15)
# for t in p_text:
#     t.set_size(15)
#
# # plt.legend(loc='upper left',bbox_to_anchor=(-0.1,1.1))
# plt.show()

# counts = [232, 305, 2021, 1882]
# plt.figure(figsize=(12, 7))
# plt.subplot(121)
# x = range(1, 5)
# y = [232, 305, 2021, 1882]
# labels = ['both none', 'only photo', 'only notes', 'both']
# plt.bar(x, y, label='counts', color='white', hatch='\\', edgecolor='k')
# for xx, yy in zip(x, y):
#     plt.text(xx, yy + 0.1, str(yy), ha='center', fontsize=12)
# plt.xticks(x, labels, fontsize=12)
# plt.xlabel('type', fontsize=14)
# plt.ylabel('counts', fontsize=14)
# plt.legend(loc='best')
#
# plt.subplot(122)
# colors = ['white']
# rate = [counts[0] / 4440, counts[1] / 4440, counts[2] / 4440, counts[3] / 4440]
# # patches, l_texts, p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本
# patches, l_text, p_text = plt.pie(rate, colors=colors, autopct='%3.1f%%', startangle=45, shadow=False,
#                                   labels=['both none', 'only photo', 'only notes', 'both'])
# pie_wedge_collection = plt.pie(rate, colors=colors, startangle=45, shadow=False)
#
# # 设置边框线
# for pie_wedge in pie_wedge_collection[0]:
#     pie_wedge.set_edgecolor('black')
#
# # 修改字体大小
# for t in l_text:
#     t.set_size(15)
# for t in p_text:
#     t.set_size(15)
#
# # plt.legend(loc='best')
# plt.show()

# counts = [3, 4, 12, 147, 747, 332, 891, 1440, 623, 241, 0, 0]
# plt.figure(figsize=(12, 7))
# # plt.subplot(121)
# x = range(1, 13)
# y = [3, 4, 12, 147, 747, 332, 891, 1440, 623, 241, 0, 0]
# # labels = ['both none', 'only photo', 'only notes', 'both']
# plt.bar(x, y, label='counts', color='white', hatch='\\', edgecolor='k')
# for xx, yy in zip(x, y):
#     plt.text(xx, yy + 0.1, str(yy), ha='center', fontsize=12)
# plt.xticks(fontsize=15)
# plt.yticks(fontsize=15)
# plt.xlabel('month', fontsize=18)
# plt.ylabel('counts', fontsize=18)
# plt.legend(loc='best')
# plt.show()
# x = range(14)
# y1 = [2, 1, 1, 1, 0, 0, 0, 0, 2, 1, 0, 1, 4, 1]
# y2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1.1, 1, 1]
# labels = ['Sep 2019', 'Oct 2019', 'Nov 2019', 'Dec 2019', 'Jan 2020', 'Feb 2020', 'Mar 2020', 'Apr 2020',
#           'May 2020', 'Jun 2020', 'Jul 2020', 'Aug 2020', 'Sep 2020', 'Oct 2020']
# plt.figure(figsize=(8, 6))
# plt.plot(x, y1, c='r', label='Observed')
# plt.plot(x, y2, c='b', label='Fitted')
# plt.xlabel("Date")
# plt.ylabel("#Number")
# plt.xticks(x, labels, fontsize=10, rotation=20)
# plt.legend()
# plt.show()


# x = range(14)
# y1 = [-122.54, -122.54, -124, -122.538, -122.56, -122.515, -122.49, -122.54, -122.51, -122.509, -122.508,
#       -122.507, -122.506, -122.505 ]
# y2 = [-122.56, -122.565, -122.57, -122.575, -122.505, -122.515, -122.52, -122.525, -122.53, -122.535,
#       -122.54, -122.545, -122.55, -122.555]
# labels = ['Sep 2019', 'Oct 2019', 'Nov 2019', 'Dec 2019', 'Jan 2020', 'Feb 2020', 'Mar 2020', 'Apr 2020',
#           'May 2020', 'Jun 2020', 'Jul 2020', 'Aug 2020', 'Sep 2020', 'Oct 2020']
# plt.figure(figsize=(8, 6))
# plt.plot(x, y1, c='r', label='Observed')
# plt.plot(x, y2, c='b', label='Fitted')
# plt.xlabel("Date")
# plt.ylabel("#Longitude")
# plt.xticks(x, labels, fontsize=10, rotation=20)
# plt.legend()
# plt.show()
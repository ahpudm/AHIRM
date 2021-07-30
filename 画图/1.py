from matplotlib import pyplot
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# douban_K
palette = pyplot.get_cmap('Set1')
# plt.rcParams['font.family'] = ['Times New Roman']
plt.rcParams.update({'font.size': 12})
names = [2, 3, 4, 5, 6, 7, 8, 9, 10]
x = range(len(names))
precision = [0.129725, 0.147325, 0.15909, 0.163255, 0.17013, 0.18489, 0.165575, 0.156945, 0.148495]
recall = [0.05904, 0.06102, 0.063915, 0.0666, 0.070485, 0.07231, 0.066075, 0.061465, 0.06055]
f1 = []
ndcg = [0.172795, 0.18183, 0.19407, 0.205005, 0.20956, 0.22912, 0.19103, 0.186505, 0.18052]
for i in range(len(precision)):
    f1.append(2 * precision[i] * recall[i] / (precision[i] + recall[i]))
plt.figure(figsize=(10, 6))
plt.plot(x, ndcg, color=palette(9), marker='s', label='NDCG', markerfacecolor='k', markersize=15)
plt.plot(x, precision, color=palette(9), marker='o', label='Precison', markerfacecolor='k', markersize=15)
plt.plot(x, recall, color=palette(9), marker='^', label='Recall', markerfacecolor='k', markersize=15)
plt.plot(x, f1, color=palette(9), marker='*', label='F1', markerfacecolor='k', markersize=15)

plt.xlabel("$s$", fontsize=15)
plt.ylabel("$Score@$10(%)", fontsize=15)
plt.ylim(0.04, 0.26)


def to_percent(temp, position):
    return '%4.0f' % (100 * temp)


plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
plt.gca().xaxis.set_major_formatter(FuncFormatter(to_percent))

# plt.ylabel("#Number")
# plt.xlim(0)

plt.margins(0)
# plt.title('lastfm')
plt.subplots_adjust(bottom=0.10)
plt.xticks(x, names, fontsize=15)
plt.yticks(fontsize=15)
plt.legend(fontsize=15)
plt.show()


# douban_f
palette = pyplot.get_cmap('Set1')
# plt.rcParams['font.family'] = ['Times New Roman']
plt.rcParams.update({'font.size': 12})
names = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1]
x = range(len(names))
precision = [0.1334412, 0.151526, 0.153195, 0.15993, 0.172854, 0.18902, 0.170088, 0.1581278, 0.15611, 0.1443125]
recall = [0.0483588, 0.0512368, 0.05544, 0.061635, 0.0752992, 0.081615, 0.061152, 0.059133, 0.054495, 0.05526]
f1 = []
ndcg = [0.1669647, 0.1870947, 0.194665, 0.195875, 0.20227692, 0.225405, 0.200412, 0.1977667, 0.1890105, 0.1874375]
for i in range(len(precision)):
    f1.append(2 * precision[i] * recall[i] / (precision[i] + recall[i]))
plt.figure(figsize=(10, 6))
plt.plot(x, ndcg, color=palette(9), marker='s', label='NDCG', markerfacecolor='k', markersize=15)
plt.plot(x, precision, color=palette(9), marker='o', label='Precison', markerfacecolor='k', markersize=15)
plt.plot(x, recall, color=palette(9), marker='^', label='Recall', markerfacecolor='k', markersize=15)
plt.plot(x, f1, color=palette(9), marker='*', label='F1', markerfacecolor='k', markersize=15)
plt.xlabel("$f$", fontsize=15)
plt.ylabel("$Score@$10(%)", fontsize=15)
plt.ylim(0.04, 0.28)


def to_percent(temp, position):
    return '%4.0f' % (100 * temp)


plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
plt.gca().xaxis.set_major_formatter(FuncFormatter(to_percent))

# plt.ylabel("#Number")
# plt.xlim(0)

plt.margins(0)
# plt.title('lastfm')
plt.subplots_adjust(bottom=0.10)
plt.xticks(x, names, fontsize=15)
plt.yticks(fontsize=15)
plt.legend(fontsize=15)
plt.show()


# douban_w1
palette = pyplot.get_cmap('Set1')
# plt.rcParams['font.family'] = ['Times New Roman']
plt.rcParams.update({'font.size': 12})
names = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
x = range(len(names))
precision = [0.15571, 0.16833, 0.17196, 0.194605, 0.17653, 0.16934, 0.154595, 0.1415, 0.13596, 0.134275, 0.127085]
recall = [0.05376, 0.06057, 0.068835, 0.07268, 0.06875, 0.06254, 0.058955, 0.052525, 0.05038, 0.048795, 0.04734]
f1 = []
ndcg = [0.190225, 0.195165, 0.206375, 0.231925, 0.225885, 0.2151, 0.1880855, 0.180884, 0.16949, 0.16717, 0.16565]
for i in range(len(precision)):
    f1.append(2 * precision[i] * recall[i] / (precision[i] + recall[i]))
plt.figure(figsize=(10, 6))
plt.plot(x, ndcg, color=palette(9), marker='s', label='NDCG', markerfacecolor='k', markersize=15)
plt.plot(x, precision, color=palette(9), marker='o', label='Precison', markerfacecolor='k', markersize=15)
plt.plot(x, recall, color=palette(9), marker='^', label='Recall', markerfacecolor='k', markersize=15)
plt.plot(x, f1, color=palette(9), marker='*', label='F1', markerfacecolor='k', markersize=15)

plt.xlabel("$w_1$", fontsize=15)
plt.ylabel("$Score@$10(%)", fontsize=15)
plt.ylim(0.03, 0.252)


def to_percent(temp, position):
    return '%4.0f' % (100 * temp)


plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
plt.gca().xaxis.set_major_formatter(FuncFormatter(to_percent))

# plt.ylabel("#Number")
# plt.xlim(0)

plt.margins(0)
# plt.title('lastfm')
plt.subplots_adjust(bottom=0.10)
plt.xticks(x, names, fontsize=15)
plt.yticks(fontsize=15)
plt.legend(fontsize=15)
plt.show()




# lastfm_K
palette = pyplot.get_cmap('Set1')
# plt.rcParams['font.family'] = ['Times New Roman']
plt.rcParams.update({'font.size': 12})
names = [2, 3, 4, 5, 6, 7, 8, 9, 10]
x = range(len(names))
precision = [0.08475, 0.09481, 0.10549, 0.099755, 0.091785, 0.090935, 0.08498, 0.07514, 0.067321]
recall = [0.1415505, 0.15288, 0.16785, 0.158665, 0.150535, 0.14891, 0.140725, 0.13213, 0.123355]
f1 = []
ndcg = [00.14185, 0.152305, 0.1613, 0.158305, 0.15204, 0.1487525, 0.147435, 0.13887, 0.131685]
for i in range(len(precision)):
    f1.append(2 * precision[i] * recall[i] / (precision[i] + recall[i]))
plt.figure(figsize=(10, 6))
plt.plot(x, ndcg, color=palette(9), marker='s', label='NDCG', markerfacecolor='k', markersize=15)
plt.plot(x, precision, color=palette(9), marker='o', label='Precison', markerfacecolor='k', markersize=15)
plt.plot(x, recall, color=palette(9), marker='^', label='Recall', markerfacecolor='k', markersize=15)
plt.plot(x, f1, color=palette(9), marker='*', label='F1', markerfacecolor='k', markersize=15)

plt.xlabel("$s$", fontsize=15)
plt.ylabel("$Score@$10(%)", fontsize=15)
plt.ylim(0.05, 0.20)


def to_percent(temp, position):
    return '%4.0f' % (100 * temp)


plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
plt.gca().xaxis.set_major_formatter(FuncFormatter(to_percent))

# plt.ylabel("#Number")
# plt.xlim(0)

plt.margins(0)
# plt.title('lastfm')
plt.subplots_adjust(bottom=0.10)
plt.xticks(x, names, fontsize=15)
plt.yticks(fontsize=15)
plt.legend(fontsize=15)
plt.show()


# lastfm_F
palette = pyplot.get_cmap('Set1')
# plt.rcParams['font.family'] = ['Times New Roman']
plt.rcParams.update({'font.size': 12})
names = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1]
x = range(len(names))
precision = [0.09367, 0.10396, 0.11549, 0.120915, 0.11683, 0.110375, 0.108625, 0.107605, 0.08945, 0.086765]
recall = [0.147455, 0.15183, 0.165415, 0.171445, 0.164329, 0.16005, 0.15637, 0.15237, 0.1372, 0.135295]
f1 = []
ndcg = [0.148825, 0.150185, 0.157945, 0.163015, 0.16005, 0.15637, 0.15087, 0.14878, 0.13755, 0.136755]
for i in range(len(precision)):
    f1.append(2 * precision[i] * recall[i] / (precision[i] + recall[i]))
plt.figure(figsize=(10, 6))
plt.plot(x, ndcg, color=palette(9), marker='s', label='NDCG', markerfacecolor='k', markersize=15)
plt.plot(x, precision, color=palette(9), marker='o', label='Precison', markerfacecolor='k', markersize=15)
plt.plot(x, recall, color=palette(9), marker='^', label='Recall', markerfacecolor='k', markersize=15)
plt.plot(x, f1, color=palette(9), marker='*', label='F1', markerfacecolor='k', markersize=15)
plt.xlabel("$f$", fontsize=15)
plt.ylabel("$Score@$10(%)", fontsize=15)
plt.ylim(0.08, 0.19)


def to_percent(temp, position):
    return '%4.0f' % (100 * temp)


plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
plt.gca().xaxis.set_major_formatter(FuncFormatter(to_percent))

# plt.ylabel("#Number")
# plt.xlim(0)

plt.margins(0)
# plt.title('lastfm')
plt.subplots_adjust(bottom=0.10)
plt.xticks(x, names, fontsize=15)
plt.yticks(fontsize=15)
plt.legend(fontsize=15)
plt.show()


# lastfm_w1
palette = pyplot.get_cmap('Set1')
# plt.rcParams['font.family'] = ['Times New Roman']
plt.rcParams.update({'font.size': 12})
names = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
x = range(len(names))
precision = [0.080455, 0.0842365, 0.09122, 0.095065, 0.10369, 0.11577, 0.109355, 0.103925, 0.09168, 0.078925, 0.07318]
recall = [0.12571, 0.13233, 0.138495, 0.143775, 0.151985, 0.173445, 0.158725, 0.151905, 0.137545, 0.120429, 0.119745]
f1 = []
ndcg = [0.129105, 0.13162, 0.14003, 0.142725, 0.151605, 0.163835, 0.15641, 0.14928, 0.137515, 0.129175, 0.12148]
for i in range(len(precision)):
    f1.append(2 * precision[i] * recall[i] / (precision[i] + recall[i]))
plt.figure(figsize=(10, 6))
plt.plot(x, ndcg, color=palette(9), marker='s', label='NDCG', markerfacecolor='k', markersize=15)
plt.plot(x, precision, color=palette(9), marker='o', label='Precison', markerfacecolor='k', markersize=15)
plt.plot(x, recall, color=palette(9), marker='^', label='Recall', markerfacecolor='k', markersize=15)
plt.plot(x, f1, color=palette(9), marker='*', label='F1', markerfacecolor='k', markersize=15)

plt.xlabel("$w_1$", fontsize=15)
plt.ylabel("$Score@$10(%)", fontsize=15)
plt.ylim(0.05, 0.20)


def to_percent(temp, position):
    return '%4.0f' % (100 * temp)


plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
plt.gca().xaxis.set_major_formatter(FuncFormatter(to_percent))

# plt.ylabel("#Number")
# plt.xlim(0)

plt.margins(0)
# plt.title('lastfm')
plt.subplots_adjust(bottom=0.10)
plt.xticks(x, names, fontsize=15)
plt.yticks(fontsize=15)
plt.legend(fontsize=15)
plt.show()
from matplotlib import pyplot
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# pyplot.figure(figsize=(6, 4.5))
palette = pyplot.get_cmap('Set1')
# # plt.rcParams['font.family'] = ['Times New Roman']
# plt.rcParams.update({'font.size': 12})

names = ['Sep 2019', 'Oct 2019', 'Nov 2019', 'Dec 2019', 'Jan 2020', 'Feb 2020', 'Mar 2020', 'Jun 2020', 'Jul 2020',
         "Jun 2020", "Jul 2020", "Aug 2020", "Sep 2020", "Oct 2002", ]
x = range(len(names))
y_Supervised = [48.99, 49.00, 49.01, 49.02, 48.95, 48.955, 48.96, 48.965, 48.97, 48.975, 48.98, 48.985, 48.99, 48.995]
y_Self = [48.97, 48.96, 49.15, 48.95, 49.03, 49.07, 48.77, 48.99, 48.93, 48.97, 48.96, 48.96, 48.96, 48.96]
plt.figure(figsize=(8, 6))
plt.plot(x, y_Supervised, color=palette(1), marker='o', label='Fitted')
plt.plot(x, y_Self, color=palette(0), marker='^', label='Observed')
plt.xlabel("Date")
plt.ylabel("#Longitude")
plt.xlim(0)
plt.ylim(48.75, 49.19)
plt.margins(0)
plt.subplots_adjust(bottom=0.10)
plt.xticks(x, names, fontsize=10, rotation=15)
plt.legend()
plt.show()

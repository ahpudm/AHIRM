import matplotlib.pyplot as plt

name_list = ['Global1', 'Global2', 'Global3', 'Global4', 'Global5', 'Global6', 'Global7', 'Global8', 'Global9',
             'Global10']
num_list = [4, 4, 4, 4, 4, 4, 4, 3.5, 3.5, 3.5]
# num_list = [4.5,4.5,4.5,4.5,4.5]
# num_list2 = [4,4,4,4,4]
# num_list3 = [4.5,4.5,4.5,4.5,4.5]
# num_list4 = [5,5,5,5,5]
x = list(range(len(num_list)))
total_width, n = 0.8, 2
width = total_width / n
plt.figure(figsize=(8, 6))
plt.ylim(2, 4.1)
plt.xlabel("Global ID")
plt.ylabel("Score")
plt.bar(x, num_list, width=width, align='center', label='Initial', tick_label=name_list, fc='white', hatch="/",
        edgecolor='k')
# for i in range(len(x)):
#     x[i] = x[i] + width
# plt.bar(x, num_list, width=width, label='Season', tick_label=name_list, fc='r')
# for i in range(len(x)):
#     x[i] = x[i] + width
# plt.bar(x, num_list2, width=width, label='Longitude', tick_label=name_list, fc='b')
# for i in range(len(x)):
#     x[i] = x[i] + width
# plt.bar(x, num_list3, width=width, label='Latitude', tick_label=name_list, fc='g')
# for i in range(len(x)):
#     x[i] = x[i] + width
# plt.bar(x, num_list4, width=width, label='Lab status', tick_label=name_list, fc='pink')
plt.legend()
plt.show()

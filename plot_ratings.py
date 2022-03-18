import matplotlib.pyplot as plt
import numpy as np

handles = []; ratings = []
f = open('/Users/charansrikar/Documents/Automation/Codeforces API/CF_User_ratings.txt', 'r')
lines = f.readlines()
for line in lines:
    a , b = line.split(' ')
    handles.append(a)
    ratings.append(b.strip())

freq = {}
for j in range(-50, 4001):
    freq[j] = 0

for j in ratings:
    freq[int(j)] = freq[int(j)] + 1

x = []; y = []
for keys in freq:
    x.append(keys)
    y.append(freq[keys])

f = open('Rating_vs_Freq.txt', 'x')
for i in range(0, len(x)):
    s = str(x[i]) + ' ' + str(y[i]) + '\n'
    f.write(s)

plt.plot(x,y)
plt.xlim([-50, 3950])
plt.ylim([0, 1950])
plt.xticks(np.arange(-50, 3950, 400))
plt.yticks(np.arange(0, 1950, 150))
plt.xlabel('Rating')
plt.ylabel('frequency')
plt.title('User Ratings vs Freq')
#plt.show()
plt.savefig('/Users/charansrikar/Documents/Automation/Codeforces API/CF_ratings_plot.png', dpi= 1200)
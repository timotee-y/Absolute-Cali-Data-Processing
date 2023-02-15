import matplotlib.pyplot as plt
import numpy as np

rx = ['TL04', 'TL06']
freq = ['B1I', 'B3I', 'B1C', 'B2a']
satnum = [0] * 37
for i in range(0, 37):
    satnum[i] = 'C' + str(i + 1)


for i in range(1, 2):
    for j in range(0, 4):
        for k in range(0, 37):
            try:
                filename = rx[i] + '_' + freq[j] + '_' + satnum[k]
                # print(filename + '.txt')
                data = np.loadtxt('./Raw/' + filename + '.txt')
                x = data[:, 0]
                y = data[:, 1]
                mean1 = np.mean(y)
                std1 = np.std(y)
                newx = []
                newy = []
               
                for i1 in range (0, len(x) - 1):
                    if(np.abs(y[i1] - mean1) <= 3 * std1):
                        newx.append(x[i1])
                        newy.append(y[i1])              
                
                tomean = str(round(np.mean(newy), 2))
                tostd = str(round(np.std(newy), 2))
                m = 'mean = ' + tomean + ' ns, '
                s = 'std = ' + tostd + ' ns'

                plt.plot(newx, newy)
                plt.xlabel('TOW /s')
                plt.ylabel('Time Offset /ns')
                plt.title(filename)
                ax = plt.gca()
                plt.text(0.5, 0.92, m + s, bbox = dict(fc = 'white', ec = 'black'), transform = ax.transAxes)
                plt.savefig('./Plot/' + filename + '.png', dpi = 500)
                plt.close()
                print('{} plot done.'.format(filename))
            except:
                print('{} not found !!!'.format(filename + '.txt'))   
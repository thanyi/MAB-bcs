import os
import datetime
import numpy as np
import matplotlib.pyplot as plt
from utils import *

def get_from_log(log, r):
    list_rate = []
    with open(log, 'r') as fp:
        for line in fp:
            if 'skip' in line:
                line = line.strip()
                rate = float(line.split(' ')[-1].replace('%', ''))
                rate = round(rate * r, 2)
                list_rate.append(rate)
                total = int(line.split(' ')[4].split('/')[-1])
    return list_rate + [rate]*(total-len(list_rate)), total

def main():
    av = 'nonnegmalconv'
    r1 = 1
    r2 = 1
    r3 = 1

    y1_list_rate, _ = get_from_log('/home/wei/code/adversarial_malware/output_' + av + '_1000_random/rewriter.log', r1)
    y2_list_rate, _ = get_from_log('/home/wei/code/adversarial_malware/output_' + av + '_1000_TS/rewriter.log', r2)
    y3_list_rate, total = get_from_log('/home/wei/code/adversarial_malware/output_' + av + '_1000_TS_parent/rewriter.log', r3)

    x1 = np.array(range(len(y1_list_rate)))
    x2 = np.array(range(len(y2_list_rate)))
    x3 = np.array(range(len(y3_list_rate)))
    
    fig, ax = plt.subplots()
    ax.plot(x1, y1_list_rate, fillstyle='none', linewidth=1, color='blue', label='Random')
    ax.plot(x2, y2_list_rate, fillstyle='none', linewidth=1, color='red', label='TS')
    ax.plot(x3, y3_list_rate, fillstyle='none', linewidth=1, color='green', label='TS (p)')
    axes = plt.gca()
    #axes.set_ylim([0,60])
    axes.set_xlim([0, total * 1.1])
    
    plt.annotate(str(y1_list_rate[-1]), (total,y1_list_rate[-1]), color='blue', textcoords="offset points", xytext=(15,0), ha='center', fontsize=9)
    plt.annotate(str(y2_list_rate[-1]), (total,y2_list_rate[-1]-3), color='red', textcoords="offset points", xytext=(15,0), ha='center', fontsize=9)
    plt.annotate(str(y3_list_rate[-1]), (total,y3_list_rate[-1]), color='green', textcoords="offset points", xytext=(15,0), ha='center', fontsize=9)

    print(str(y2_list_rate[-1]))
    print(str(y3_list_rate[-1]))

    plt.xlabel('total number of attempts', fontsize=12)
    plt.ylabel('evasion rate %', fontsize=12)
    ax.legend(loc='lower right', ncol=2)#, framealpha=0)
    
    #plt.show()
    matplotlib.pyplot.title(av);
    plt.savefig("/home/wei/Share/evasion_rate_of_attempts_%s.pdf" %av)

if __name__ == '__main__':
    main()


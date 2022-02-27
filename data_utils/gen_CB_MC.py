# -*- coding: utf-8 -*-
"""
Created on Fri Jul 05 22:40:29 2019

@author: Xueyu Shi
"""

import numpy as np
import os

file_path = 'dataset/Max_MonoSub_PM'
if not os.path.exists(file_path):
    os.mkdir(file_path)

r = 5
#for n in [10, 15, 20, 25, 30, 35, 40, 45, 50]:
for n in [100, 150, 200, 300]:
    for m in [50, 100]:
        for j in range(10):
            file_name_pre = 'CB_' + 'n' + str(n) + 'm' + str(m)
            
            
            weight = (np.random.uniform(0, 0.2, n))
#            weight = np.ones(n) / float(budget)
            alpha = np.random.uniform(0.05, 0.1, n)
            beta = np.random.uniform(0, 1, n)
            lnf = np.random.normal(0.05, 0.0025, m)
            
            vmatrix = np.zeros((m, n))
            for i in range(m):
                eps = np.random.normal(0, 0.0025, n)
                vmatrix[i] = (np.exp(alpha + beta * lnf[i] + eps) * weight)
            
            # partition constraints
            pmatrix = []
            budgets = np.random.randint(1, 6, r)
            set_size = np.random.uniform(0.15, 0.25, r)
            set_size = set_size / sum(set_size)
            set_size = [np.floor(n*a) for a in set_size]
            set_size[-1] +=  n - sum(set_size)
                
            
            N = np.array(range(n))
            np.random.shuffle(N)
            MC_set = np.zeros((r, n))
            index = 0
            for i in range(r):
                MC_set[i, N[index:index+int(set_size[i])]] = 1
                index += int(set_size[i])
            

            
            for ld in [4, 6, 8, 10]:
                file_name = file_name_pre + 'ld' + str(ld)  + 'j' + str(j) + '.txt'
                out_file = open(os.path.join(file_path, file_name), 'w')
                
                out_file.write(str(n) + '\t' + str(m) + '\t' + str(ld / 10.0) + '\t' + str(r) +  '\n')
                
                out_file.write('budget\t' + '\t'.join(str(e) for e in budgets)+ '\n')
                out_file.write('partition\n')
                for i in range(r):
                    out_file.write('\t'.join(str(e) for e in MC_set[i])+ '\n')
                    
                out_file.write('cost\n')
                for i in range(m):
                    out_file.write('\t'.join(str("{0:.4f}".format(e)) for e in vmatrix[i])+ '\n')

                out_file.close()
                
                
                
                
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 05 22:40:29 2019

@author: Xueyu Shi
"""

import numpy as np
import os

file_path = 'Dataset/SubM_Quad_PM'
if not os.path.exists(file_path):
    os.mkdir(file_path)

r = 5
for n in [50, 100]:
    for m in [25, 50, 100]:
        for j in range(10):
            file_name_pre = 'CB_' + 'n' + str(n) + 'm' + str(m)
            
            alpha = np.random.uniform(0.05, 0.1, n)
            beta = np.random.uniform(0, 1, n)
            lnf = np.random.normal(0.05, 0.0025, m)
            
            vmatrix = np.zeros((m, n))
            for i in range(m):
                eps = np.random.normal(0, 0.0025, n)
                vmatrix[i] = (alpha + beta * lnf[i] + eps) 
            
#            vmatrix = (np.random.uniform(0, 0.2, (m, n)))
            bvector = np.random.uniform(1, 2) + np.random.uniform(0, 1) * np.random.normal(0.1, 0.0025, m)
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
            

            
            for ld in [8, 10, 20, 40]:
            
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
                
                out_file.write('\t'.join(str("{0:.4f}".format(e)) for e in bvector)+ '\n')

                out_file.close()
                
                
                
                
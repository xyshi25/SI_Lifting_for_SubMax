# -*- coding: utf-8 -*-
"""
Created on Fri Jul 05 22:40:29 2019

@author: Xueyu Shi
"""

import numpy as np
import os



file_path = 'dataset/Max_MonoSub_Car'
if not os.path.exists(file_path):
    os.mkdir(file_path)

for n in [100, 150, 200, 300]:
    for m in [50, 100, 150]:
        for j in range(10):
            
            budget = np.random.randint(10, np.floor(0.75*n));
            
            weight = (np.random.uniform(0, 0.2, n))
#            weight = np.ones(n) / float(budget)
            alpha = np.random.uniform(0.05, 0.1, n)
            beta = np.random.uniform(0, 1, n)
            lnf = np.random.normal(0.05, 0.0025, m)
            
            vmatrix = np.zeros((m, n))
            for i in range(m):
                eps = np.random.normal(0, 0.0025, n)
                vmatrix[i] = (np.exp(alpha + beta * lnf[i] + eps) * weight)
            
            for ld in [4, 6, 8, 10]:
            
                file_name = 'CB_n' + str(n) + 'm' + str(m) + 'ld' + str(ld)  + 'j' + str(j) + '.txt'
                out_file = open(os.path.join(file_path, file_name), 'w')
                
                out_file.write(str(n) + '\t' + str(m) + '\t' + str(ld / 10.0) +  '\n')
               
                out_file.write('weight\t' + '\t'.join(str("{0:.2f}".format(e)) for e in weight)+ '\n')             
                out_file.write('cost\n')
                
                for i in range(m):
                    out_file.write('\t'.join(str("{0:.4f}".format(e)) for e in vmatrix[i])+ '\n')

                out_file.close()
                
                
                
                
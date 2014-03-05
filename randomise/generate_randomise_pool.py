import os as os

nperms=10000
ncores=100

pool='/Users/rmuetzel/list.pool.data'

nperms_per_core = int((nperms / ncores) + 1)

pFile = open(pool, 'w')

for n in range(1, ncores+1):
    pFile.write(str(n) + ' ' + str(nperms_per_core) + '\n')

pFile.close()
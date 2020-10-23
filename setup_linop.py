
from distutils.core import setup, Extension
import os
import re
import sys

import numpy as np

#os.environ['CC'] = 'gcc-mp-6'

BART_PATH = os.environ['TOOLBOX_PATH']

omp = 'gomp'
if sys.platform == 'darwin':
       omp = 'omp'

module = Extension('_linop',
                     extra_compile_args=['-fopenmp'],
                     extra_link_args=[f'-l{omp}'],
                     include_dirs=[f'{BART_PATH}/src/', '/opt/local/include/', '/opt/local/lib/',
                                   np.get_include()],
                     sources=[f'{BART_PATH}/src/linops/linop.c',
                            f'{BART_PATH}/src/linops/someops.c',
                            f'{BART_PATH}/src/linops/grad.c', 
                            'linop_wrap.c'],
                     libraries=['box', 'calib', 'dfwavelet', 'geom',
                                   'grecon', 'iter', 'linops', 'lowrank', 
                                   'misc', 'moba', 'nlops', 'noir', 'noncart',
                                   'num', 'sake', 'sense', 'simu', 'wavelet',
                                   'openblas', 'fftw3f', 'fftw3', 'fftw3f_threads',],
                     library_dirs=['/Users/malits/bart_work/bart/lib/', '/opt/local/include/', '/opt/local/lib/'],
                     )

setup (name = 'linop',
       version = '0.1',
       author      = "BART",
       description = 'Linear Operators in BART',
       ext_modules = [module],
       py_modules = ["linop"]
       )
       
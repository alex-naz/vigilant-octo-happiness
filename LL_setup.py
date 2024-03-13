from distutils.core import setup
from Cython.Build import cythonize
import numpy as np

setup(name="LL_cython", ext_modules=cythonize("LL_cython.pyx"), include_dirs=[np.get_include()])
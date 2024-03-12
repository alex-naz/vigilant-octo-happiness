from distutils.core import setup
from Cython.Build import cythonize

setup(name="LL_cython",
      ext_modules=cythonize("LL_cython.pyx"))
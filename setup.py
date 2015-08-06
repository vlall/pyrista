from setuptools import setup, find_packages

setup(name='pyrista',
      version='0.1',
      description='Applying PyeAPI for Arista',
      author='V Lall, Data Tactics',
      license='MIT',
    packages=(['pyrista', 'pyrista/tools']),
      install_requires = ['pandas>=0.16.0',
          'bokeh>=0.9.0',
          'pyeapi>=0.3',
          ],
      zip_safe=False,)

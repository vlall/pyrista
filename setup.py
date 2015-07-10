from setuptools import setup, find_packages

setup(name='pyrista',
      version='0.1',
      description='Applying PyeAPI for Arista',
      url='https://gitlab.xdataproxy.com/rjacobs/dsra-networking',
      author='Vishal Lall, Data Tactics',
      author_email='vishal.h.lall@gmail.com',
      license='MIT',
    packages=(['pyrista', 'pyrista/tools', 'pyrista/tests' ]),
      install_requires = ['pandas>=0.16.0',
          'bokeh>=0.9.0',
          'pyeapi>=0.3',
          ],
      zip_safe=False,)
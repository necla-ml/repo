from setuptools import setup, find_packages
#from distutils.core import setup, Extension
#import distutils.command.bdist_conda

import os
print(os.environ)

setup(
    name="repo",
    version="0.0.1",
    author='Farley Lai',
    author_email='farleylai@nec-labs.com',
    description='Easy to use repository utilities',
    url='https://nj-gitlab.nec-labs.com/farleylai/repo',
    entry_points = {
        'console_scripts': [ 'repo = repo.__main__:cli' ]
    },
    #install_requires = [
    #    'click',
        #'make',
    #],
    packages = find_packages(),
    #data_files = [ ('repo', ['Makefile']) ],
    include_package_data=True,
    zip_safe=False,
    #distclass=distutils.command.bdist_conda.CondaDistribution,
    #conda_buildnum=1,
    #conda_features=[],
)

from setuptools import setup, find_packages
from os.path import basename
from os.path import splitext
from glob import glob

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='databricks_helpers',
    version='0.1.0',
    description='Data Derp databricks_helpers',
    author='Kelsey Mok',
    author_email='kelseymok@gmail.com',
    url='https://github.com/data-derp/databricks_helpers',
    packages=find_packages('src', exclude=('tests')),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    install_requirements=required
)

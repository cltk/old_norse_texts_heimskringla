"""Config for PyPI."""

from setuptools import find_packages
from setuptools import setup


setup(
    author='Clément Besnier',
    author_email='clemsciences@aol.com',
    description='Old Norse Eddas',
    keywords=['nlp', 'old norse', "philology"],
    license='MIT',
    long_description='',
    name='old_norse_texts_heimskringla',
    packages=find_packages(),
    url='https://github.com/clemsciences/old_norse_texts_heimskringla',
    version='1.2.0',
    zip_safe=True, install_requires=['bs4', 'cltk', 'nltk']
    # test_suite='cltk.tests.test_cltk',
)

"""Config for PyPI."""

from setuptools import find_packages
from setuptools import setup


setup(
    author='Clément Besnier',
    author_email='clemsciences@aol.com',
    classifiers=[
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Old Norse',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing',
    ],
    description='Old Norse Eddas',
    # install_requires=['gitpython',
    #                   'bs4'],
    keywords=['nlp', 'old norse'],
    license='MIT',
    long_description='',
    name='old_norse_texts_heimskringla',
    packages=find_packages(),
    url='https://github.com/clemsciences/old_norse_texts_heimskringla',
    version='1.1.0',
    zip_safe=True, install_requires=['bs4', 'cltk']
    # test_suite='cltk.tests.test_cltk',
)

from setuptools import setup, find_packages

setup(
    name='word-count',
    version='0.0.1',
    description='This project will list top word frequencies for given text.',
    url='https://github.com/alysivji/word-count',
    author='Aly Sivji',
    author_email='alysivji@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(exclude=['tests', ]),
    install_requires=[''],
    download_url='https://github.com/alysivji/word-count',
)

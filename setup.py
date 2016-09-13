# coding=utf8
from setuptools import setup, find_packages
__author__ = 'hellflame'


setup(
    name='YoudaoDict',
    version="3.1.0",
    keywords=('Youdao', 'youdao', 'dict', 'youdao api', 'partly offset dict'),
    description="适用于在linux or mac 终端通过有道api查询单词或者翻译词句",
    license='MIT',
    author='hellflame',
    author_email='hellflamedly@gmail.com',
    url="https://github.com/hellflame/youdao",
    packages=find_packages(),
    install_requires=[
        'paramseeker>=0.3'
    ],
    platforms="UNIX like",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        "Environment :: Console",
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX'
    ],
    entry_points={
        'console_scripts': [
            'youdao=youdao.run:runner'
        ]
    }
)



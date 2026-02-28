from setuptools import setup, find_packages 

setup(
    name='cortex-chatbot',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'wikipedia==1.4.0',
        'nltk==3.8.1',
    ],
    entry_points={
        'console_scripts': [
            'cortex = src.main:main',
        ]
    },
    author='AridsWolfgangX',
    description='A comprehensive multi-domain chatbot with cross-domain reasoning capabilities.',   
    license='MIT',
)
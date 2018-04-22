from setuptools import setup, find_packages


setup(
    name='useful',
    version='0.1',
    packages=find_packages(),
    package_data={},
    install_requires=[
        'pandas',
        'numpy',
        'biopython',
        'matplotlib'
        ]
    )
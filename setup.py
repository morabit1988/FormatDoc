from setuptools import setup, find_packages

setup(
    name='formatdoc',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'python-docx',
    ],
    entry_points={
        'console_scripts': [
            'formatdoc = formatdoc.cli:main',
        ],
    },
)

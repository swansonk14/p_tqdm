from setuptools import find_packages, setup

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='p_tqdm',
    version='1.3.3',
    author='Kyle Swanson',
    author_email='swansonk.14@gmail.com',
    description='Parallel processing with progress bars',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/swansonk14/p_tqdm',
    download_url='https://github.com/swansonk14/p_tqdm/v_1.3.3.tar.gz',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'tqdm>=4.45.0',
        'pathos>=0.2.5',
        'six>=1.13.0'
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    keywords=[
        'tqdm',
        'progress bar',
        'parallel'
    ],
)

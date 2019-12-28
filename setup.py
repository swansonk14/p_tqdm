from setuptools import find_packages, setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='p_tqdm',
    version='1.2',
    author='Kyle Swanson',
    author_email='swansonk.14@gmail.com',
    description='Parallel processing with progress bars',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/swansonk14/p_tqdm',
    download_url='https://github.com/swansonk14/p_tqdm/v_1.2.tar.gz',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'tqdm',
        'pathos'
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    keywords=[
        'tqdm',
        'progress bar',
        'parallel'
    ],
)

import io
import os
import sys


from setuptools import setup, find_packages

long_description = ''  # TODO: add
install_requires = ['ccxt', 'pandas', 'structlog']
tests_require = ['pytest', 'pytest-watch']

setup(
    name='fomo-superfilter',
    version='0.0.3',
    description='Filters the shit out of shitcoins.',
    long_description=long_description,
    author='run2dev',
    author_email='run2devtest@gmail.com',
    url='https://github.com/run2dev',
    packages=find_packages(),
    install_requires=install_requires,
    python_requires='>=3.6.0',
    tests_require=tests_require,
    # cmdclass = {'test': PyTest},
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: System :: Monitoring',
    ],
)

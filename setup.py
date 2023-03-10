from setuptools import setup

setup(
    name='admixasia',

    version='1.0.4',

    description='An admixture analysis tool add EastAsia3 that supports raw data from 23andme, AncestryDNA, etc.',
    long_description=open('admix/README.rst',encoding='UTF-8').read(),

    url='https://github.com/Ueda00Ryota/admixasia',

    author='Ryota Ueda',
    author_email='killertcell428@gmail.com',

    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Natural Language :: Japanese(Simplified)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],

    keywords='bio DNA SNP ancestry admixture',

    install_requires=['numpy','scipy'],

    packages=['admix'],

    package_data={
        'admix':['data/*', 'README.rst']
    },

    entry_points={
        'console_scripts': ['admix=admix.admix:main'],
    },
)

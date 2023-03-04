from setuptools import setup

setup(
    name='admixasia',

    version='1.0',

    description='An admixture analysis tool add EastAsia3 that supports raw data from 23andme, AncestryDNA, etc.',
    long_description=open('admix/README.rst','r').read(),

    url='https://github.com/Ueda00Ryota/admixasia',

    author='Ryota Ueda',
    author_email='killertcell428@gmail.com',

    license='GNU General Public License v3.0',

    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Natural Language :: Chinese (Simplified)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],

    keywords='bio DNA SNP ancestry admixture',

    install_requires=['numpy','scipy'],

    packages=['admixasia'],

    package_data={
        'admix':['data/*', 'README.rst']
    },

    entry_points={
        'console_scripts': ['admixasia=admixasia.admixasia:main'],
    },
)

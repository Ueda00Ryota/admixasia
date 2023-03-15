#!/usr/bin/env python
# -*- coding: utf-8 -*-

# yapf: disable

# all models
def models():
    return ['EastAsia3',
            'K7b',
            'K12b',
            ]

# population names for all models
def populations(model):
    if model == 'K7b':
        return [('South Asian','南アジア'),
                ('West Asian','西アジア'),
                ('Siberian','シベリア'),
                ('African','アフリカ'),
                ('Southern','オーストラリア'),
                ('Atlantic Baltic','大西洋、バルト海'),
                ('East Asian','東アジア')]
    elif model == 'K12b':
        return [('Gedrosia','ゲドロシア'),
                ('Siberian','シベリア'),
                ('Northwest African','西北アフリカ'),
                ('Southeast Asian','東南アジア'),
                ('Atlantic Med','大西洋、地中海'),
                ('North European','北欧'),
                ('South Asian','南アジア'),
                ('East African','東アフリカ'),
                ('Southwest Asian','南西アジア'),
                ('East Asian','東アジア'),
                ('Caucasus','コーカサス'),
                ('Sub Saharan','サハラ南部')]
    elif model == 'EastAsia3':
        return [("Han",'中国'),
                ('Japanese','日本'),
                ('Korean','韓国')]
    else:
        print('Model does not exist!')
        return None

# yapf: enable


# number of populations in all models
def n_populations(model):
    return len(populations(model))


# model alleles file names
def snp_file_name(model):
    return model + ".alleles"


# model frequency matrix file names
def frequency_file_name(model):
    return model + "." + str(n_populations(model)) + ".F"

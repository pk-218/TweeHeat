import os

from django.contrib.gis.utils import LayerMapping

from .models import States

# Auto-generated `LayerMapping` dictionary for States model
states_mapping = {
    'fid': 'FID',
    'program': 'Program',
    'state_code': 'State_Code',
    'state_name': 'State_Name',
    'flowing_st': 'Flowing_St',
    'fid_1': 'FID_1',
    'geom': 'MULTIPOLYGON',
}

states_shape = 'data/shape files/States_shapefile.shp'


def run(verbose=True):
    lm = LayerMapping(States, states_shape, states_mapping, transform=False, encoding='utf-8')
    lm.save(strict=True, verbose=verbose)

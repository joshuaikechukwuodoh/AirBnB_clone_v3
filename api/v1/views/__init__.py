#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on sun may 1 14:42:23 2023
@author: joshua ikechukwu odoh
         Mark Nkugwa
"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


if (__name__ == 'api.v1.views'):
    from api.v1.views.index import *
    from api.v1.views.states import *
    from api.v1.views.cities import *
    from api.v1.views.amenities import *
    from api.v1.views.users import *
    from api.v1.views.places import *
    from api.v1.views.places_reviews import *

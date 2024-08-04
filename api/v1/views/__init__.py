#!/usr/bin/python3
""" initializes view of directory  """
from flask import Blueprint


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.amenities import *
from api.v1.views.places import *
from api.v1.views.cities import *
from api.v1.views.users import *
from api.v1.views.places_reviews import *

#to enable christina commit

# Adding changes for task 6 (new view of state objects)
# Adding changes for task 7 (new view of user objects)
# Adding changes for task 8 (new view of amenity objects)
# Adding changes for task 9(new view of user objects handle restful api)
# Adding changes for task 10 (new view of place objects)
# Adding changes for task 11 (new view of review objects)
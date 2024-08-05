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

#To see change
# TASK 6 Create a new view for State objects that handles all default RESTFul API actions:
# TASK 7 create a new view for City objects 
# TASK 8 Create a new view for Amenity objects that handles all default RESTFul API actions:
#TASK 9 Create a new view for USER objects that handles all default RESTFul API actions:
# TASK 10 Create a new view for PLACE objects that handles all default RESTFul API actions:
# TASK 11 Create a new view for Amenity objects that handles all default RESTFul API actions:
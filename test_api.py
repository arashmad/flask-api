
#**********************************
# Interpreter   => Python 3.7.x
# Framwork      => Flask Framework
#**********************************
# API works on TAGs (Wirepas API)
# Hanatech IOT Halifax, Canada
#**********************************

from flask import Blueprint, request, Response
from flask_jwt_extended import jwt_required, get_jwt_identity

import test

bp = Blueprint(test, __name__)

@bp.route('/message/get', methods=['GET'])
def test_function():
    print('\n====================== Request Type => GET')
    print('====================== Request path => /test/message/get')
    return test.test_function()
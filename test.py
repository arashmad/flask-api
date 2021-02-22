
#**********************************
# Interpreter   => Python 3.7.x
# Framwork      => Flask Framework
#**********************************
# API works on TAGs (Wirepas API)
# Hanatech IOT Halifax, Canada
#**********************************

import os
import json
from flask import Response
from flask_api import status
from utils import print_message

def test_function():
    print_message()
    try:
        return Response(
            json.dumps({'msg': 'OK!'}),
            status=status.HTTP_200_OK,
            mimetype='application/json')

    except Exception as e:
        return Response(
            json.dumps({'msg':e}),
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            mimetype='application/json')

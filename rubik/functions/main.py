import json

from flask import make_response

from rubik.rubik import random_cube, validate_cube, Cube


def random(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
    """
    cube = random_cube()
    return make_response(cube.to_json(), 200)


def validate(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
    """
    if request.is_json:
        data = request.json
        if 'cube' in data:
            cube = Cube(json.dumps(data['cube']))
            is_valid = validate_cube(cube)
            message = {"valid": is_valid}
            response = make_response(json.dumps(message), 200)
        else:
            response = make_response('Missing cube parameter', 404)
    else:
        response = make_response('Invalid request', 404)
    return response


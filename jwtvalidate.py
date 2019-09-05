""" JWTValidate Plugin """
from .jwtvalidate_logic.jwtvalidate_logic import JwtTokenValidator


def execute(args):
    """ Execute Command Interface """
    ign = JwtTokenValidator()
    ign.execute(args)

def helptext():
    """ Basic Plugin Helptext Display """
    return "Validate JWT tokens"

def register(app):
    """ Register Plugin with Forge """
    app.register_plugin('jwtvalidate', execute, helptext())

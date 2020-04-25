""" JWTValidate Plugin """
from typing import List, Any
from .jwtvalidate_logic.jwtvalidate_logic import JwtTokenValidator


def execute(args: List[str]) -> None:
    """ Execute Command Interface """
    ign = JwtTokenValidator()
    ign.execute(args=args)

def helptext() -> str:
    """ Basic Plugin Helptext Display """
    return "Validate JWT tokens"

def register(app: Any) -> None:
    """ Register Plugin with Forge """
    app.register_plugin('jwtvalidate', execute, helptext())

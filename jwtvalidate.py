from .jwtvalidate_logic.jwtvalidate_logic import JwtTokenValidator


def execute(args):
	ign = JwtTokenValidator()
	ign.execute(args)

def helptext():
	return "Validate JWT tokens"

def register(app):
	app.register_plugin('jwtvalidate', execute, helptext())

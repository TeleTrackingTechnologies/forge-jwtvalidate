""" JWTValidate Logic """
import argparse
import jwt

class JwtTokenValidator:
    """ JWT Token Validator Class """

    def __init__(self):
        self.arg_parser = self.init_arg_parser()

    def execute(self, args):
        """ Execute """
        parsed_args = self.arg_parser.parse_args(args)

        secret = ''
        with open(parsed_args.publicKey, 'r') as file:
            secret = file.read()

        alg = 'RS256'
        if parsed_args.algorithm is not None:
            alg = parsed_args.algorithm.upper()

        decoded = jwt.decode(parsed_args.token, secret, algorithms=alg)
        print(decoded)

    @staticmethod
    def init_arg_parser():
        """ Initialize Argument Parser """
        parser = argparse.ArgumentParser(prog='forge jwtvalidate')
        parser.add_argument('-t', '--token', action='store', dest='token', required=True,
                            help='jwt token to validate')
        parser.add_argument('-p', '--publickey', action='store', dest='publicKey', required=True,
                            help='the public key to decode token')
        parser.add_argument('-alg', '--algorithm', action='store', dest='algorithm',
                            help='the algorithm used to sign the token, the default is RS256')
        return parser
